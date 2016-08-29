# Evaluate the e-mission data collection library

Here's where we check in the timeline and the associated scripts. The idea is
that this will eventualy turn into the "benchmark" that others can use as well.

### Working with Android Batterystats

1. Connect your android device to a computer, run the command below to make sure you see your device number listed 
> $ adb devices

2. Dump battery data from the device by running the command below 
> $ adb shell dumpsys batterystats > batterystats.txt

### Parsing Batterystats

1. Replace the `batterystats.txt` you just generated with the one in the `batterystats_parser` directory

2. Open `batt_script.ipynb`, choose run all cells

3. The parsed battery level info is saved in `batterystats_parsed.csv`

### Running Analysis for Summer'16 Experiments 

1. Follow the instructions [here](https://github.com/e-mission/e-mission-server) to install the required dependencies

2. Start the database 
> $ mongod

3. Start the local server in your cloned repo of [e-mission-server](https://github.com/e-mission/e-mission-server) 
> $ ./e-mission-py.bash emission/net/api/cfc_webapp.py

4. Find `experiment_analysis.ipynb` in the `analysis_summer_2016` directory, open it in Jupyter notebook

5. Pull data from the server and load it to your local server (note: you only need to do this once for each experiment, unless you have erased your entire database)

 - in  `experiment_analysis.ipynb`, set`load_exp_index` to your desired experiment index (can be found in `experiments.csv`) to pull data for a single experiment 
 - or set `exp_index` to -1 to pull data for all the experiments (given the large amount of data collected from the experiments, this may take up to an hour to finish)

6.  Running analysis for an experiment 

 - in `experiment_analysis.ipynb`, set `exp_index` to an experiment of your choice, plots & analysis for the selected experiment will be automatically generated when you run the rest of the script
