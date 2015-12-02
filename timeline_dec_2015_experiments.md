# Timeline template

This is a template that can be used to record a timeline of when certain things were done.
Ideally this would be in the data as well, but the data will not contain
periods of no data collection.

## List of regimes being tested

## Android
### Passive regimes
1. no data collection (nd)
2. no geofence, high accuracy, no filter (nohanf)
2. no geofence, high accuracy, 30 secs (noha30s)
2. no geofence, medium accuracy, no filter (nomanf)
3. no geofence, medium accuracy, 2 secs (noma2s)
3. no geofence, medium accuracy, 30 secs (noma30s)
3. no geofence, medium accuracy, 60 secs (noma30s)
4. geofence 100m (geo100m)
4. geofence 50m (geo50m)
4. geofence 5m (geo5m)

### Active regimes
1. no data collection (nd)
2. no geofence, high accuracy, no filter (nohanf)
2. no geofence, high accuracy, 2 secs (noha2s)
2. no geofence, high accuracy, 30 secs (noha30s)
2. no geofence, high accuracy, 60 secs (noha60s)
3. no geofence, medium accuracy, 2 secs (noma2s)
3. no geofence, medium accuracy, 30 secs (noma30s)
3. no geofence, medium accuracy, 60 secs (noma30s)
2. geofence 100m, selected accuracy-time filter (geo100m-satf)
4. geofence 50m, selected accuracy-time filter (geo50m-satf)
4. geofence 5m, selected accuracy-time filter (geo5m-satf)

### Timeline


Human readable start date  | Start Timestamp (s) | phone1     | phone2    | phone3 | Human readable end date | End Timestamp (s)  | Notes
-------------------------- | ------------------  | ---------- | --------- | -----------| ----------------------- | ----------------- | ------
2015-11-08 18:09:20.739536 | 1447034960.74       | nd        | nd        | nd      | 2015-11-09 09:04:08.971723 | 1447088648.97 |
2015-11-09 09:42:35.659353 | 1447090955.66       | geo100m   | geo100m   | geo100m | 2015-11-09 18:59:32.085172 | 1447124372.09 | went to state ongoing_trip at around 6pm, (6:03, 6:05 5:49) and never ended trip. Update! Ended trip at 7:30
2015-11-09 19:18:54.105137 | 1447125534.11       | noma30s | noma30s | noma30s | 2015-11-10 07:30:54.708202 | 1447169454.71 | Still mostly in doze mode. Only 46 and 70 wakeups
2015-11-10 07:30:54.708202 | 1447169454.71       | noha30s | noha30s | noha30s | 2015-11-10 20:00:12.112079 | 1447214412.11 | Power levels were fairly similar at the end (87%, 83%, 82%)
2015-11-10 20:10:22.500289 | 1447215022.5        | nohanf  | nohanf  | nohanf  | 2015-11-11 08:18:37.860248 | 1447258717.86 | Power levels low (warning) (9%, 9%, 9%)
2015-11-11 19:25:15.846526 | 1447298715.85       | nomanf  | nomanf  | nomanf  | 2015-11-12 08:18:24.066606 | 1447345104.07 | Starting at 100% after recharging
2015-11-12 08:18:24.066606 | 1447345104.07       | nd      | nd      | nd      | 2015-11-12 20:13:29.217236 | 1447388009.22 | Repeat without being connected to local WiFi
2015-11-12 20:59:58.726268 | 1447390798.73       | geo100m | geo100m | geo100m | 2015-11-13 19:59:21.948885 | 1447473561.95 | Repeat without being connected to local WiFi
2015-11-13 20:22:54.807962 | 1447474974.81       | nd | nd | nd | 2015-11-14 20:48:59.322432 | 1447562939.32 | Repeat since previous collection had a couple of zero values
2015-11-14 21:05:22.509800 | 1447563922.51       | noma30s | noma30s | noma30s | 2015-11-15 21:38:37.464872 | 1447652317.46 | Fill in missing values
2015-11-15 21:55:16.859492 | 1447653316.86       | nomanf | nomanf | nomanf | 2015-11-18 21:49:13.563926 | 1447912153.56 | Retry the most surprising result
2015-11-24 23:14:30.548574 | 1448435670.55       | nohanf | nohanf | nohanf | 2015-11-25 07:18:52.145377 1448464732.15 | Retry the most surprising result
2015-11-25 09:11:39.169554 | 1448435670.55       | noha30s | geo100m-ma30s  | nd | 2015-11-25 20:09:48.206494 | 1448510988.21 | Active testing starts
2015-11-25 20:09:48.206494 | 1448510988.21       | noha30s | geo100m-ma30s  | nd | 2015-11-26 09:09:51.680674 | 1448557791.68 | Back to stationary at night
2015-11-27 08:12:42.725766 | 1448640762.73       | force-gps-30s | geo100m-ma30s | nd | 2015-11-27 20:00:00 | 1448688775.56 | Forcing the use of GPS versus the fused API, active regime
2015-11-27 20:00:00 | 1448683200.73       | force-gps-30s | geo100m-ma30s | nd | 2015-11-28 08:22:20.406719 | 1448727740.41 | Forcing the use of GPS versus the fused API, passive regime
2015-11-28 08:22:20.406719 | 1448727740.41 | force-gps-30s | geo100m-ma30s | nd | 2015-11-28 14:46:23.013716 | 1448750783.01 | Evaluating accuracy on a bike ride
2015-11-28 14:46:23.013716 | 1448750783.01 | force-gps-30s | geo100m-ma30s | geo50m-ha10s | 2015-11-29 07:57:20.395805 | 1448812640.41 | Evaluating accuracy on different geofences, accuracies and frequencies
2015-11-30 12:38:28.413130 | 1448915908.41 | geo100m-ma30s | geo100m-ma30s | noma30s | 2015-12-01 15:36:47.295005 | 1449013007.3 | Checking geofence triggers
2015-12-01 15:36:47.295005 | 1449013007.3 | geo100m-ma30s | geo100m-ma30s | noma30s | 2015-12-01 15:36:47.295005 | 1449013007.3 | Checking geofence triggers after resetting battery stats


## iOS
### Passive regimes
1. no data collection (nd)
2. no geofence, best accuracy, no filter (nohanf)
2. no geofence, best accuracy, 50m filter (noha50m)
3. no geofence, accuracy 100m, no filter (nomanf)
3. no geofence, accuracy 100m, 5m filter (noma5m)
3. no geofence, accuracy 100m, 50m filter (noma50m)
3. no geofence, accuracy 100m, 100m filter (noma100m)
4. geofence 100m (geo100m)
4. geofence 50m (geo50m)
4. geofence 5m (geo5m)

### Active regimes
1. no data collection (nd)
2. no geofence, best accuracy, no filter (nohanf)
2. no geofence, best accuracy, 5m filter (noha5m)
2. no geofence, best accuracy, 50m filter (noha50m)
2. no geofence, best accuracy, 100m filter (noha100m)
3. no geofence, accuracy 100m, 5m filter (noma5m)
3. no geofence, accuracy 100m, 50m filter (noma50m)
3. no geofence, accuracy 100m, 100m filter (noma100m)
2. geofence 100m, selected accuracy-dist filter (geo100m-satf)
4. geofence 50m, selected accuracy-dist filter (geo50m-satf)
4. geofence 5m, selected accuracy-dist filter (geo5m-satf)


### Timeline

Human readable start date  | Start Timestamp (s) | phone1     | phone2    | phone3 | Human readable end date | End Timestamp (s)  | Notes
-------------------------- | ------------------  | ---------- | --------- | -----------| ----------------------- | ----------------- | -----
2015-11-24 16:05:07.015886 | 1448410148.41 | geo100m-ma100m | nd          | nd        | 2015-11-24 22:20:34.012595 | 1448432434.01 | on the way back from berkeley
2015-11-24 23:14:30.548574 | 1448435670.55 | geo100m-ma100m | noma100m    | nd        | 2015-11-25 07:05:33.057023 | 1448463933.06 | when phones were stationary
2015-11-25 07:31:06.475876 | 1448465466.48 | geo100m-ma100m | noha100m    | nd        | 2015-11-25 20:09:48.206494 | 1448510988.21 | when phones are in motion
2015-11-25 20:09:48.206494 | 1448510988.21 | geo100m-ma100m | noha100m    | nd        | 2015-11-26 07:32:06.829330 | 1448551926.83 | when phones are stationary
2015-11-25 20:09:48.206494 | 1448510988.21 | geo100m-ma100m | noha100m    | nd        | 2015-11-26 07:32:06.829330 | 1448551926.83 | when phones are stationary
2015-11-27 10:00:00.407475 | 1448647200.00 | geo100m-ma100m | various    | nd        | 2015-11-27 20:13:07.443489 | 1448683987.44 | experimenting with using visits for data collection. ended up cleaning up the state machine instead
2015-11-27 22:01:04.668537 | 1448690464.67 | geo100m-ma100m | geo50m-ma100m | geo5m-ma100m | 2015-11-28 08:07:42.415973 | 1448726862.42 | looking at the power drain of various geofence regimes
2015-11-28 08:07:42.415973 | 1448726862.42 | geo100m-ma100m | geo50m-ma100m | geo5m-ma100m | 2015-11-28 14:45:31.512758 | 1448750731.51 | looking at the accuracy of various geofence regimes
2015-11-28 14:46:23.013716 | 1448750731.01 | geo100m-ma100m | geo50m-a10m-d50m | geo5m-ha5m | 2015-11-29 07:57:20.395805 | 1448812640.42 | looking at the accuracy of various geofence, accuracy and distance filter metrics
2015-11-30 12:38:28.413130 | 1448915908.41 | noma100m | geo100m-ma100m | geo100m-ma100m | 2015-12-01 12:38:28-08:00 | 1449002308 | checking geofence triggers
