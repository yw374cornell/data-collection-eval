# Timelines for data collection in spring 2017

This is a less structured template than the previous data collection, mainly
because we are doing ongoing data collection anyway. It's all currently human
readable, so it doesn't really matter.

## Setup
### Android

- Factory reset
- Connected to WiFi at home, not at school
- Location history turned off
- Anonymous location updates turned on
- Android 6.0.1 with March 2016 patches (installs stupid Verizon app)
- Developer options turned on
- Allow google to check for harmful activity periodically = off

### iOS

- Erase all settings and data
- Connected to WiFi at home, not at school
- Send anonymous data to Apple turned on
- iOS 9.3

## Experiments:

- All four phones sitting on a desk, no sampling, no user interaction. Compute
  divergence.

- Baseline power and accuracy. All four phones running the same regime - high
  accuracy, fast sampling, sample user interaction (the alert) on
    - android: PRIORITY_HIGH_ACCURACY, 1 sec
    - iOS: kCLLocationAccuracyBest, 1 meter

    - Test scenarios
        - Tue, March 29
            - Trip from home to Berkeley and back, can be ground truthed via
              GTFS file for BART and Caltrain and BART and Caltrain schedules
            - Sitting in the living room next to each other overnight

- Compare various accuracy settings, simulate user interaction always = YES
    - Have one high accuracy fast sampling for baseline
    - Other phones have different settings
    - Compared wrt baseline rather than ground truth

    - Test scenarios
        - Wed 30th March 9am to 11pm (Stevenson and dance)
            android 1: high accuracy, 1 sec
            android 2: medium accuracy, 1 sec
            android 3: high accuracy, 30 sec
            android 4: medium accuracy, 30 sec

            ios 1: best, 1 sec
            ios 2: 10 meters, 1 meter
            ios 3: best, 30 meters
            ios 4: 10 meters, 30 meters
    
        - Plugged in overnight, so not very interesting

        - Thu 31st March 9am to 9pm (Berkeley)
            android 1: high accuracy, 1 sec
            android 2: medium accuracy, 1 sec
            android 3: high accuracy, 30 sec
            android 4: medium accuracy, 30 sec

            ios 1: best, 1 sec
            ios 2: 10 meters, 1 meter
            ios 3: best, 30 meters
            ios 4: 10 meters, 30 meters

        - Fri 1st Apr 9am to Sat 2nd Apr 8am
            android 1: high accuracy, 1 sec
            android 2: medium accuracy, 1 sec
            android 3: high accuracy, 15 sec
            android 4: medium accuracy, 15 sec

            ios 1: best, 1 sec
            ios 2: hundred meters, 1 meter
            ios 3: best, 30 meters
            ios 4: hundred meters, 30 meters

        - Sat 2nd Apr ... to Sun ... 
            android 1: no tracking, unplugged
            android 2: no tracking, unplugged
            android 3: no tracking, unplugged
            android 4: no tracking, unplugged

            ios 1: no tracking, unplugged
            ios 2: no tracking, unplugged
            ios 3: no tracking, unplugged
            ios 4: no tracking, unplugged

        - Sun 3rd Apr ... to Mon 4th Apr ...
            android 1: no tracking, unplugged
            android 2: no tracking, unplugged
            android 3: no tracking, unplugged
            android 4: no tracking, unplugged

            ios 1: no tracking, unplugged
            ios 2: no tracking, unplugged
            ios 3: no tracking, unplugged
            ios 4: no tracking, unplugged


        - Mon 3rd Apr
            android 1: high accuracy, 1 sec
            android 2: high accuracy, 1 sec
            android 3: high accuracy, 1 sec
            android 4: high accuracy, 1 sec

            ios 1: high accuracy, 1 sec
            ios 2: high accuracy, 1 sec
            ios 3: high accuracy, 1 sec
            ios 4: high accuracy, 1 sec

        - Mon 28th Apr

high-vs-balanced-vs-none+1sec-vs-30sec
android 1: high accuracy, 1 sec
android 2: balanced accuracy, 1 sec
android 3: high accuracy, 30 sec
android 4: no data collection

best-vs-10m-vs-100m-vs-none+1m
ios 1: best accuracy, 1m
ios 2: 10m accuracy, 1m
ios 3: 100m accuracy, 1m
ios 4: no data collection

best-vs-10m-vs-100m-vs-none+100m
ios 1: best accuracy, 1m
ios 2: 100m accuracy, 100m
ios 3: 100m accuracy, 30m
ios 4: no data collection

best-vs-10m-vs-100m-vs-none+1m
ios 1: best accuracy, 1m
ios 2: 10m accuracy, 1m
ios 3: 100m accuracy, 1m
ios 4: no data collection

5th Apr: on the way back, iphone tracking was not restarted on phones 3 and 4,
so they stayed at 10m accuracy
7th Apr: on the way back, several android phones appeared "frozen". Location
8th Apr: similar. also android phone3 turned itself off for an hour from 
343662,1460151017.95,2016-04-08 15:23:17.950000-07:00,BuiltinUserCache : Added value for key background/location at time 1.460151017935E9
343663,1460154177.22,2016-04-08 16:15:57.220000-07:00,BootReceiver : BootReceiver.onReceive called
12th Apr: similar even after just rebooting and reinstalling

1460042110,2016-04-07T08:15:10.875548-07:00,moving,high-vs-balanced-vs-none+1sec-vs-30sec,best-vs-10m-vs-100m-vs-none+1m

1461078509,2016-04-19T08:09:41.422978-07:00,


12th Apr: android 2 reinstall and restart:
04-12 07:41:56.560    9874-9874/edu.berkeley.eecs.emission D/LocationHandler﹕ default request is Request[PRIORITY_BALANCED_POWER_ACCURACY requested=3600000ms fastest=600000ms]
04-12 07:41:56.566    9874-9874/edu.berkeley.eecs.emission D/LocationHandler﹕ after applying config, value is Request[PRIORITY_BALANCED_POWER_ACCURACY requested=1000ms fastest=166ms]

android 4 reinstall with tracking off:
04-12 07:51:52.493    7436-7436/? I/System.out﹕ logger == null, lazily creating new logger
04-12 07:51:52.690    7436-7436/? I/System.out﹕ During plugin initialize, created usercacheedu.berkeley.eecs.emission.cordova.usercache.BuiltinUserCache@5bf390d
04-12 07:51:52.716    7436-7436/? D/DataCollectionPlugin﹕ google play services available, initializing state machine
04-12 07:51:52.720    7436-7496/? I/System.out﹕ All preferences are {setup_complete=62, bgsync_launch_next_online=false, TripDiaryCurrState=local.state.tracking_stopped}
04-12 07:51:52.725    7436-7496/? D/TripDiaryStateMachineReceiver﹕ Setup complete, skipping initialize
04-12 07:51:52.726    7436-7436/? I/System.out﹕ mAccount = Account {name=dummy_account, type=eecs.berkeley.edu}

high-30s-v-geofenced, high-10m-v-geofenced
android 1: high accuracy, 1 sec
android 2: high accuracy, 30 sec
android 3: high accuracy, 30 sec, geofencing
android 4: none

ios 1: high accuracy, 1 m
ios 2: high accuracy, 10 m
ios 3: high accuracy, 10 m, geofencing
ios 4: high accuracy, none
