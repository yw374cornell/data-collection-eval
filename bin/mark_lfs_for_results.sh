RESULT_DIR=$1

echo "Marking $RESULT_DIR/ucb.sdb.android.{1,4}/timeseries as LFS"
git lfs track $RESULT_DIR/ucb.sdb.android.1/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.android.2/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.android.3/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.android.4/timeseries/*

echo "Marking $RESULT_DIR/ucb.sdb.ios.{1,4}/timeseries as LFS"
git lfs track $RESULT_DIR/ucb.sdb.ios.1/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.ios.2/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.ios.3/timeseries/*
git lfs track $RESULT_DIR/ucb.sdb.ios.4/timeseries/*
