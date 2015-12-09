import pandas as pd
import matplotlib.pyplot as plt
import random
import logging
import numpy as np
import datetime as pydt

def insert_transition_strings(df_list):
    import emission.core.wrapper.transition as ecwt
    for df in df_list:
        if len(df) > 0:
            df["transition_str"] = df.transition.map(lambda(tval): ecwt.TransitionType(tval))

def generate_fake_dataframe(start, end, fill_val):
    x_axis = np.arange(start,end,30)
    y_axis = np.empty(len(x_axis))
    y_axis.fill(fill_val)
    print "Fake data length = %d, fill_val = %s" % (len(x_axis), fill_val)
    # logging.debug("after filling, array is %s" % y_axis)
    return pd.DataFrame({"ts": x_axis, "latitude": y_axis})

def get_fill_val(location_dfs):
    # Find the mean latitudes so that we can create a dummy dataframe when there is no data
    np_array = np.empty(len(location_dfs))
    np_array.fill(float('nan'))
    lat_means = pd.Series(np_array)
    print "length of lat_means = %d" % len(lat_means)
    # logging.debug("before setting, lat_means = %s" % lat_means)
    for i, df in enumerate(location_dfs):
        if len(df) > 0:
            lat_means[i] = df.latitude.mean()
    # logging.debug("lat_means = %s, mean = %s" % (lat_means, lat_means.mean()))
    return lat_means.mean()

def plot_for_transition(label, location_df, transition_df, ax, lat_mean, ground_truth_start_ts, ground_truth_end_ts):
    print "Considering phone %s" % label
    ax.axvline(x=ground_truth_start_ts, linewidth=1, color="purple")
    ax.axvline(x=ground_truth_end_ts, linewidth=1, color="purple")
    ax.set_title(label)

    if len(location_df) == 0:
        print "No data to plot for dataframe %s" % label
        generate_fake_dataframe(ground_truth_start_ts, ground_truth_end_ts, lat_mean).plot(x="ts", y="latitude", kind="scatter", ax=ax)
        ax.annotate("No data for dataframe", xy=(0.3, 0.5), xycoords='axes fraction', fontsize=12, color="red")
    else:
        location_df[(location_df.ts > ground_truth_start_ts) & (location_df.ts < ground_truth_end_ts)].plot(x="ts", y="latitude", kind="scatter", ax=ax)

        if len(transition_df) == 0 or np.count_nonzero(transition_df.transition == 1) == 0:
            print("len(transition_df) = %d, ground_truth_start_ts = %d, geofence was not exited!!" % 
                  (len(transition_df), ground_truth_start_ts))
            ax.annotate("Geofence was not exited!", xy=(0.3, 0.2), xycoords='axes fraction', fontsize=12, color="blue")            
        else:
            trip_geofence_exit_entry = transition_df[transition_df.transition == 1].iloc[0]
            trip_geofence_exit_ts = trip_geofence_exit_entry["ts"]
            ax.axvline(x=trip_geofence_exit_ts, linewidth=1, color="green")
            if len(location_df) > 0:
                after_geofence_exit_points = location_df[(location_df.ts >= trip_geofence_exit_ts) & (location_df.ts <= ground_truth_end_ts)]
                if len(after_geofence_exit_points) > 0:
                    first_location_entry = after_geofence_exit_points.iloc[0]
                    print("ground truth exit = %s, geofence_exit_ts = +%5f, first location point = +%5f" %
                          (pydt.datetime.fromtimestamp(ground_truth_start_ts),
                         (trip_geofence_exit_ts - ground_truth_start_ts),
                         (first_location_entry.ts - ground_truth_start_ts)))
                    ax.axvline(x=first_location_entry.ts, linewidth=1, color="green", linestyle='-')

def plot_for_transitions(label, location_df_list, transition_df_list, axes_array, ground_truth_start_ts, ground_truth_end_ts):
    lat_mean = get_fill_val(location_df_list)
    logging.debug("Caluldated fill_val = %s" % lat_mean)
    for i, (location_df, transition_df, ax) in enumerate(zip(location_df_list, transition_df_list, axes_array)):
        plot_for_transition(label + str(i), location_df, transition_df, ax, lat_mean, ground_truth_start_ts, ground_truth_end_ts)

def evaluate_trip_accuracy(iphone_ts_list, android_ts_list, label, start_ts, end_ts):
    import emission.net.usercache.abstract_usercache as enua
    print "Generating trip for %s" % label
    iphone_df_list = [ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", start_ts, end_ts)) for ts in iphone_ts_list]
    android_df_list = [ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", start_ts, end_ts)) for ts in android_ts_list]
    iphone_transition_df_list = [ts.get_data_df("statemachine/transition", enua.UserCache.TimeQuery("write_ts", start_ts, end_ts)) for ts in iphone_ts_list]
    android_transition_df_list = [ts.get_data_df("statemachine/transition", enua.UserCache.TimeQuery("write_ts", start_ts, end_ts)) for ts in android_ts_list]
    insert_transition_strings(iphone_transition_df_list)
    insert_transition_strings(android_transition_df_list)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15,5), sharex=True, sharey=True)
    fig.suptitle("%s -> %s" % (pydt.datetime.fromtimestamp(start_ts),
                               pydt.datetime.fromtimestamp(end_ts)))
    plot_for_transitions(label + " android", android_df_list, android_transition_df_list, axes[0], start_ts, end_ts)
    plot_for_transitions(label + " iphone", iphone_df_list, iphone_transition_df_list, axes[1], start_ts, end_ts)
    return fig

def get_ground_truth_loc(row, ongoing_iphone_ts, ongoing_android_ts):
    import emission.net.usercache.abstract_usercache as enua
    start_location_iphone_df = ongoing_iphone_ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", row.start_ts - 60, row.start_ts + 60))
    start_location_android_df = ongoing_android_ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", row.start_ts - 60, row.start_ts + 60))
    start_location_df = start_location_iphone_df.append(start_location_android_df)
    points_before = start_location_df[(start_location_df.metadata_write_ts <= row.start_ts) &
                                       (start_location_df.accuracy < 200)]
    points_after = start_location_df[(start_location_df.metadata_write_ts >= row.start_ts) &
                                      (start_location_df.accuracy < 200)]
    if len(points_before) > 0:
        logging.debug("sel point is before")
        sel_point = points_before.tail(1).iloc[0]
    else:
        if len(points_after) > 0:
            logging.debug("sel point is after")
            sel_point = points_after.head(1).iloc[0]
        else:
            raise RuntimeError("No points in ongoing tracking either")
    assert(sel_point is not None)
    # return {"latitude": sel_point.latitude, "longitude": sel_point.longitude, "ts": sel_point.ts, "accuracy": sel_point.accuracy}
    return sel_point[["latitude", "longitude", "ts", "accuracy", "fmt_time"]]

def get_ground_truth_loc_df(ground_truth_time_df, ongoing_iphone_ts, ongoing_android_ts):
    ground_truth_loc_list = []
    for idx, row in ground_truth_time_df.iterrows():
        ground_truth_loc_list.append(get_ground_truth_loc(row, ongoing_iphone_ts, ongoing_android_ts))
    return pd.DataFrame(ground_truth_loc_list)

def get_geofence_trigger_summary(location_df, transition_df, ground_truth_start_ts, ground_truth_end_ts):
    retVal = {}
    if len(location_df) == 0:
        retVal["error"] = "no data"
    else:
        if len(transition_df) == 0 or np.count_nonzero(transition_df.transition == 1) == 0:
            print("len(transition_df) = %d, ground_truth_start_ts = %d, geofence was not exited!!" % 
                  (len(transition_df), ground_truth_start_ts))
            retVal["error"] = "no geofence"
        else:
            trip_geofence_exit_entry = transition_df[transition_df.transition == 1].iloc[0]
            trip_geofence_exit_ts = trip_geofence_exit_entry["ts"]
            retVal["exit_delay"] = trip_geofence_exit_ts - ground_truth_start_ts
            retVal["error"] = None
            if len(location_df) > 0:
                after_geofence_exit_points = location_df[(location_df.ts >= trip_geofence_exit_ts) & (location_df.ts <= ground_truth_end_ts)]
                if len(after_geofence_exit_points) > 0:
                    first_location_entry = after_geofence_exit_points.iloc[0]
                    retVal["geofence_exit_to_first_point"] = first_location_entry.ts - trip_geofence_exit_ts
                    retVal["trip_start_to_first_point"] = first_location_entry.ts - ground_truth_start_ts
    return retVal

def get_geofence_trigger_summary_df(ground_truth_df, iphone_ts, android_ts):
    import emission.net.usercache.abstract_usercache as enua
    iphone_geofence_trigger_summary_list = []
    android_geofence_trigger_summary_list = []

    iphone_location_df_list = [iphone_ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", row.start_ts, row.end_ts)) for idx, row in ground_truth_df.iterrows()]
    android_location_df_list = [android_ts.get_data_df("background/location", enua.UserCache.TimeQuery("write_ts", row.start_ts, row.end_ts)) for idx, row in ground_truth_df.iterrows()]
    
    iphone_transition_df_list = [iphone_ts.get_data_df("statemachine/transition", enua.UserCache.TimeQuery("write_ts", row.start_ts, row.end_ts)) for idx, row in ground_truth_df.iterrows()]
    android_transition_df_list = [android_ts.get_data_df("statemachine/transition", enua.UserCache.TimeQuery("write_ts", row.start_ts, row.end_ts)) for idx, row in ground_truth_df.iterrows()]

    moving_df = ground_truth_df[ground_truth_df.state == "moving"]
    for idx, row in moving_df.iterrows():
        iphone_geofence_trigger_summary_list.append(get_geofence_trigger_summary(
            iphone_location_df_list[idx],
            iphone_transition_df_list[idx],
            row.start_ts, row.end_ts))
        android_geofence_trigger_summary_list.append(get_geofence_trigger_summary(
            android_location_df_list[idx],
            android_transition_df_list[idx],
            row.start_ts, row.end_ts))

    return (pd.DataFrame(iphone_geofence_trigger_summary_list),
            pd.DataFrame(android_geofence_trigger_summary_list))
