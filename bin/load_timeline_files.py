DAY=$1
TAG=$2
RESULT_DIR=$3

# Change this to point to the location of your server code
EMISSION_SERVER_HOME=$HOME/e-mission/e-mission-server

echo "Loading file $RESULT_DIR/ucb.sdb.ios.1/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.ios.1/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.ios.2/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.ios.2/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.ios.3/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.ios.3/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.ios.4/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.ios.4/timeseries/$TAG.$DAY

echo "Loading file $RESULT_DIR/ucb.sdb.android.1/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.android.1/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.android.2/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.android.2/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.android.3/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.android.3/timeseries/$TAG.$DAY
echo "Loading file $RESULT_DIR/ucb.sdb.android.4/timeseries/$TAG.$DAY"
PYTHONPATH=$EMISSION_SERVER_HOME:$PYTHONPATH python $EMISSION_SERVER_HOME/bin/debug/load_timeline_for_day_and_user.py $PWD/$RESULT_DIR/ucb.sdb.android.4/timeseries/$TAG.$DAY
