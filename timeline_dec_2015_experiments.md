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
3. no geofence, medium accuracy, no filter (nomanf)
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
Human readable start date  | Start Timestamp (s) | phone1     | phone2    | phone3 | Human readable end date | End Timestamp (s)  
-------------------------- | ------------------  | ---------- | --------- | -----------| ----------------------- | ----------------- 
2015-11-08 18:09:20.739536 | 1447034960.74       | nd        | nd        | nd      | 2015-11-09 09:04:08.971723 | 1447088648.97  
2015-11-09 09:42:35.659353 | 1447090955.66       | geo100m   | geo100m   | geo100m | 

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
