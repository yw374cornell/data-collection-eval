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
-------------------------- | ------------------  | ---------- | --------- | -----------| ----------------------- | ----------------- 
2015-11-08 18:09:20.739536 | 1447034960.74       | nd        | nd        | nd      | 2015-11-09 09:04:08.971723 | 1447088648.97 |
2015-11-09 09:42:35.659353 | 1447090955.66       | geo100m   | geo100m   | geo100m | 2015-11-09 18:59:32.085172 | 1447124372.09 | went to state ongoing_trip at around 6pm, (6:03, 6:05 5:49) and never ended trip. Update! Ended trip at 7:30
2015-11-09 19:18:54.105137 | 1447125534.11       | noma30s | noma30s | noma30s | 2015-11-10 07:30:54.708202 | 1447169454.71 | Still mostly in doze mode. Only 46 and 70 wakeups
2015-11-10 07:30:54.708202 | 1447169454.71       | noha30s | noha30s | noha30s | 2015-11-10 20:00:12.112079 | 1447214412.11 | Power levels were fairly similar at the end (87%, 83%, 82%)
2015-11-10 20:10:22.500289 | 1447215022.5        | nohanf  | nohanf  | nohanf  | 2015-11-11 08:18:37.860248 | 1447258717.86 | Power levels low (warning) (9%, 9%, 9%)
2015-11-11 19:25:15.846526 | 1447298715.85       | nomanf  | nomanf  | nomanf  | 2015-11-12 08:18:24.066606 | 1447345104.07 | Starting at 100% after recharging
2015-11-12 08:18:24.066606 | 1447345104.07       | nd      | nd      | nd      | 2015-11-12 20:13:29.217236 | 1447388009.22 | Repeat without being connected to local WiFi
2015-11-12 20:59:58.726268 | 1447390798.73       | geo100m | geo100m | geo100m | | Repeat without being connected to local WiFi

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
2. geofence 100m, selected accuracy-time filter (geo100m-satf)
4. geofence 50m, selected accuracy-time filter (geo50m-satf)
4. geofence 5m, selected accuracy-time filter (geo5m-satf)


### Timeline
Human readable date        | Timestamp (s) | phone1     | phone2    | phone3 
-------------------------- | ------------- | ---------- | --------- | -----------
...