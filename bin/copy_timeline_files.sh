DAY=$1
TAG=$2

scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.1.$TAG.$DAY results_dec_2015/ucb.sdb.ios.1/timeseries/$TAG.$DAY
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.2.$TAG.$DAY results_dec_2015/ucb.sdb.ios.2/timeseries/$TAG.$DAY
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/iphone.3.$TAG.$DAY results_dec_2015/ucb.sdb.ios.3/timeseries/$TAG.$DAY

scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.1.$TAG.$DAY results_dec_2015/ucb.sdb.android.1/timeseries/$TAG.$DAY
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.2.$TAG.$DAY results_dec_2015/ucb.sdb.android.2/timeseries/$TAG.$DAY
scp -i ~/.ssh/amplab-us-east.pem ubuntu@aws-webapp:/tmp/android.3.$TAG.$DAY results_dec_2015/ucb.sdb.android.3/timeseries/$TAG.$DAY
