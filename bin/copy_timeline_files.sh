DAY=$1
TAG=$2
RESULT_DIR=$3

scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.1.$TAG.$DAY $RESULT_DIR/ucb.sdb.ios.1/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.2.$TAG.$DAY $RESULT_DIR/ucb.sdb.ios.2/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.3.$TAG.$DAY $RESULT_DIR/ucb.sdb.ios.3/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.4.$TAG.$DAY $RESULT_DIR/ucb.sdb.ios.4/timeseries/$TAG.$DAY.timeline

scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.1.$TAG.$DAY $RESULT_DIR/ucb.sdb.android.1/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.2.$TAG.$DAY $RESULT_DIR/ucb.sdb.android.2/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.3.$TAG.$DAY $RESULT_DIR/ucb.sdb.android.3/timeseries/$TAG.$DAY.timeline
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.4.$TAG.$DAY $RESULT_DIR/ucb.sdb.android.4/timeseries/$TAG.$DAY.timeline
