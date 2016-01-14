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
2016-01-12 12:00:00.000000 | 1452628800.74       | nohafs      | nd        | nd        | 2016-01-12 09:06:50.942939 | 1452618437.64 |
2016-01-12 09:06:50.942939 | 1452618437.64       | nohafs      | nomafs    | geo100m-hafs | 2016-01-12 21:06:50.942939 | 1452661610.942 | Only recorded at start and end
2016-01-13 07:45:26.626450 | 1452699972.533      | nohafs      | nomafs    | geo100m-hafs | 2016-01-13 22:24:09.203 | 1452752649.203


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
2016-01-12 12:00:00.000000 | 1452628800.74       | nohafs      | nd        | nd      | 2016-01-12 09:06:50.942939 | 1452618437.64 |
2016-01-12 09:06:50.942939 | 1452618437.64       | nohafs      | nomafs    | geo100m-hafs | 
