# Timelines for data collection in spring 2016

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

        - Fri 1st Apr 9am to midnight
            android 1: high accuracy, 1 sec
            android 2: medium accuracy, 1 sec
            android 3: high accuracy, 15 sec
            android 4: medium accuracy, 15 sec

            android 1: best, 1 sec
            android 2: hundred meters, 1 meter
            android 3: best, 30 meters
            android 4: hundred meters, 30 meters

