import pandas as pd
import matplotlib.pyplot as plt

def secs_to_hour(secs):
    return secs/(60 * 60)

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
    return diff_df[diff_df.value < 0].apply(lambda(arr): arr[1]/(arr[0]/(60 * 60)), axis=1)

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
        curr_state_diff_df = curr_state_drain_df[["ts","value"]].diff()
        state_diff_df_map[row.state] = state_diff_df_map[row.state].append(curr_state_diff_df[curr_state_diff_df.value < 0].apply(lambda(arr): arr[1]/secs_to_hour(arr[0]), axis=1))
    state_diff_df = pd.DataFrame({"state": ["moving"] * len(state_diff_df_map["moving"]), "rate": state_diff_df_map["moving"]}).append(
                    pd.DataFrame({"state": ["active"] * len(state_diff_df_map["active"]), "rate": state_diff_df_map["active"]})).append(
                    pd.DataFrame({"state": ["passive"] * len(state_diff_df_map["passive"]), "rate": state_diff_df_map["passive"]}))
    return state_diff_df

def display_per_state_drain(drain_df_map, ground_truth_df, regime_map):
    drain_df_keys = sorted(drain_df_map.keys())
    fig, axes = plt.subplots(nrows=1, ncols=len(drain_df_keys), figsize=(15,3), sharey=True)
    for i, key in enumerate(drain_df_keys):
        print "displaying %d" % i
        drain_df = drain_df_map[key]
        state_diff_df = get_state_diff_df(drain_df, ground_truth_df)
        state_diff_df.boxplot(column='rate', by='state', ax=axes[i], grid=True)
        axes[i].set_title("%s (%s)" % (key, regime_map[key]))

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
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,3))
    axes[0].set_title("android")
    axes[1].set_title("iOS")

    for i, key in enumerate(sorted(drain_df_map.keys())):
        if "android" in key:
            drain_df_map[key].plot(x="fmt_time", y="value", label=regime_map[key], ax=axes[0])
        else:
            drain_df_map[key].plot(x="fmt_time", y="value", label=regime_map[key], ax=axes[1])

    for ax in axes:
        for idx, row in ground_truth_df.iterrows():
            print "adding annotations for %s, %s, %s" % (idx, row.start_fmt_time, row.end_fmt_time)
            ax.axvspan(xmin=row.start_fmt_time, xmax=row.end_fmt_time, color=get_state_color(row.state), alpha=0.2, label=row.state)
            ax.annotate(row.state, xy=(row.start_fmt_time, 50), xycoords='data', fontsize=10, color=get_state_color(row.state))
    return (fig, axes)
