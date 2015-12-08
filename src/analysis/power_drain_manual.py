import pandas as pd
import matplotlib.pyplot as plt
import random
import logging

def secs_to_hour(secs):
    return float(secs)/(60 * 60)

def mins_to_hour(mins):
    return float(mins)/60

def get_ground_truth_df(drain_df, transitions):
    """
    transition is a 2-D array - first row is transition points, second is states
    len(first row) = len(second row) + 1
    """
    assert(len(transitions[0]) == len(transitions[1]) + 1)
    sel_df = drain_df[drain_df.index.isin(transitions[0])][["ts", "fmt_time", "value"]]
    state_df = pd.DataFrame(transitions[1], columns=["state"])
    ground_truth_df = pd.concat([sel_df.reset_index(), sel_df.iloc[1:].reset_index(), state_df], axis=1)[:-1]
    ground_truth_df.columns = ['start_index', 'start_ts', 'start_fmt_time', "start_value", "end_index", "end_ts", "end_fmt_time", "end_value", "state"]
    return ground_truth_df

def get_rate_df(drain_df):
    diff_df = drain_df[["ts","value"]].diff()
    # logging.debug("diff_df = %s" % diff_df)
    return diff_df[diff_df.value <= 0].apply(lambda(arr): arr[1]/(arr[0]/(60 * 60)), axis=1)

def display_overall_drain(drain_df_map, regime_map):
    drain_df_keys = sorted(drain_df_map.keys())
    fig, axes = plt.subplots(nrows=1, ncols=len(drain_df_keys), figsize=(15,3), sharey=True)
    for i, key in enumerate(drain_df_keys):
        print "displaying %d" % i
        drain_df = drain_df_map[key]
        rate_df = get_rate_df(drain_df)
        rate_df.plot(kind='box', label="%s (%s)" % (key, regime_map[key]), ax=axes[i])
    for ax in axes:
        ax.minorticks_on()
        ax.grid(which='both', color='purple')
    return (fig, axes)

def get_state_diff_df(drain_df, ground_truth_df):
    state_diff_df_map = {"moving": pd.Series(), "active": pd.Series(), "passive": pd.Series()}
    for idx,row in ground_truth_df.iterrows():
        # print row.start_fmt_time, row.end_fmt_time
        # print row.state, drain_df[(drain_df.ts >= row.start_ts) & (drain_df.ts <= row.end_ts)]
        curr_state_drain_df = drain_df[(drain_df.ts >= row.start_ts) & (drain_df.ts <= row.end_ts)]
        # logging.debug("curr_state_drain_df = %s" % curr_state_drain_df)
        curr_rate_df = get_rate_df(curr_state_drain_df)
        # logging.debug("rate_df = %s" % curr_rate_df)
        # logging.debug("About to merge %s and %s" % (state_diff_df_map[row.state].head(), curr_rate_df.head()))
        state_diff_df_map[row.state] = state_diff_df_map[row.state].append(curr_rate_df)
        # logging.debug("After merge, %s" % state_diff_df_map[row.state].head())
    state_diff_df = pd.DataFrame({"state": ["moving"] * len(state_diff_df_map["moving"]), "rate": state_diff_df_map["moving"]}).append(
                    pd.DataFrame({"state": ["active"] * len(state_diff_df_map["active"]), "rate": state_diff_df_map["active"]})).append(
                    pd.DataFrame({"state": ["passive"] * len(state_diff_df_map["passive"]), "rate": state_diff_df_map["passive"]}))
    return state_diff_df

def display_per_state_drain(drain_df_map, ground_truth_df, regime_map):
    drain_df_keys = sorted(drain_df_map.keys())
    fig, axes = plt.subplots(nrows=1, ncols=len(drain_df_keys), figsize=(15,3), sharey=True)
    for i, key in enumerate(drain_df_keys):
        print "displaying %d, %s (%s)" % (i, key, regime_map[key])
        drain_df = drain_df_map[key]
        state_diff_df = get_state_diff_df(drain_df, ground_truth_df)
        state_diff_df.boxplot(column='rate', by='state', ax=axes[i], grid=True)
        axes[i].set_title("%s (%s)" % (key, regime_map[key]))
        # print state_diff_df.groupby('state').rate.describe()

    for ax in axes:
        ax.minorticks_on()
        ax.grid(which='both', color='purple')

    # We set the label on only the first graph because we have shared Y
    axes[0].set_ylabel("battery % drain/hr")
    # By default, pandas adds a stupid label like "Boxplot grouped by state".
    # This overlaps with part of the per graph title and looks ugly. And 
    for t in fig.texts:
        t.set_text("")

    return (fig, axes)

def get_state_color(state):
    if state == "moving":
        return "red"
    if state == "active":
        return "blue"
    if state == "passive":
        return "green"

def display_drain_over_day(drain_df_map, ground_truth_df, regime_map):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,3), sharey=True)
    axes[0].set_title("android")
    axes[1].set_title("iOS")

    for i, key in enumerate(sorted(drain_df_map.keys())):
        if "android" in key:
            drain_df_map[key].plot(x="fmt_time", y="value", label=regime_map[key], ax=axes[0])
        else:
            drain_df_map[key].plot(x="fmt_time", y="value", label=regime_map[key], ax=axes[1])

    for ax in axes:
        drain_legend = ax.legend(loc=0)
        span_map = {}
        for idx, row in ground_truth_df.iterrows():
            print "adding annotations for %s, %s, %s" % (idx, row.start_fmt_time, row.end_fmt_time)
            span_map[row.state] = ax.axvspan(xmin=row.start_fmt_time, xmax=row.end_fmt_time, color=get_state_color(row.state), alpha=0.2, label=row.state)
            ax.legend(span_map.values(), span_map.keys(), bbox_to_anchor=(0., -0.45, 1., 1.5), loc=0, mode='expand', ncol=3)
            ax.add_artist(drain_legend)
    return (fig,axes)

def code_to_state(tier1_code):
    if tier1_code == 1:
        return "passive"
    else:
        if tier1_code == 18:
            return "moving"
        else:
            return "active"

def get_power_drain_for_regime(user_df, regime_model):
    with_power_df = user_df.merge(regime_model, on='state')
    # logging.debug("After merging, df = %s" % with_power_df)
    with_power_df["power"] = with_power_df.apply(lambda(arr): mins_to_hour(arr[5]) * arr[9], axis=1)
    return with_power_df.power.sum()

def get_regime_model(overall_model, regime):
    regime_model = overall_model[["state", regime]]
    regime_model.columns = ["state", "drain_rate"]
    # logging.debug("For regime %s, returning model %s" % (regime, regime_model))
    return regime_model

def get_power_drain_for_regimes(user_df, overall_model):
    power_drain_for_regimes = {}
    # First, figure out the time in each state
    user_df["state"] = user_df.TUTIER1CODE.map(lambda(c): code_to_state(c))

    # First get predicted power drain for no data collection
    power_drain_for_regimes["nd"] = get_power_drain_for_regime(user_df,
                                        get_regime_model(overall_model, "nd"))

    active_collection_regimes = ["nohafs", "nomafs", "nomass"]

    # Next, get predicted power drain for no geofenced collection
    for regime in active_collection_regimes:
        power_drain_for_regimes[regime] = get_power_drain_for_regime(user_df,
                                        get_regime_model(overall_model, regime))

    # Finally, get geofenced power drain with various regimes
    for regime in active_collection_regimes:
        # Combine geofencing with the specified regimes
        grm = get_regime_model(overall_model, "geofenced")
        label = "geo-%s" % regime.replace("no", "")
        moving_index = grm[grm.state == "moving"].index
        rrm = get_regime_model(overall_model, regime)
        # logging.debug("Before setting moving value, %s" % grm)
        grm.loc[moving_index, "drain_rate"] = rrm[rrm.state == "moving"].drain_rate
        # logging.debug("After setting moving value, %s" % grm)
        power_drain_for_regimes[label] = get_power_drain_for_regime(user_df, grm)

    # print "Returning power data %s " % power_drain_for_regimes
    return power_drain_for_regimes

def get_predicted_power_drain_df(atus_data_df, sel_user_list, power_drain_model):
    power_drain_dicts = []
    for user in sel_user_list:
        user_df = atus_data_df[atus_data_df.TUCASEID == user]
        power_drain_dict = get_power_drain_for_regimes(user_df, power_drain_model)
        # print power_drain_dict
        power_drain_dicts.append(power_drain_dict)
    power_drain_df = pd.DataFrame(power_drain_dicts)
    return power_drain_df

