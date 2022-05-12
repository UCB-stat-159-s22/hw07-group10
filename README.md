# Reproducible Research Project for Predicting Algerian Forest Fires.

Binder Link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw07-group10/HEAD?labpath=main.ipynb)

Github page: https://ucb-stat-159-s22.github.io/hw07-group10/

Dataset Link: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6515974.svg)](https://doi.org/10.5281/zenodo.6515974)

This is a project attempting to predict forest fires in a reproducible manner.  We conduct exploratory data analysis and use a random forest and logistic regression for prediction. The data is of two regions of Algeria, namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria. The time period is from June 2012 to September 2012.

## Repository Structure

- `/data`: original and intermediate data csv files.
- `/figures`: all generated figures as png files.
- `/models`: intermediate model object files for random forest classifier.
- Jupyter Notebooks:
  - `main.ipynb`: the main narrative notebook of the research project.
  - `data_cleaning.ipynb`: code for cleaning the original data and saving the intermediate cleaned data.
  - `EDA.ipynb`: code for exploratoring data analysis and generating EDA related figures.
  - `models.ipynb`: code for the random forest classifier and logistic regression model and their corresponding figures.
- Python utility package `tools`:
  - `/tools`: code and tests for python package.
  - Setup files: `setup.py`, `setup.cfg`, `pyproj.toml`.
- Environment files: `environment.yml`, `envsetup.sh`.
- Jupyter Book: `_config.yml`, `_toc.yml`, `conf.py`, `postBuild`, `requirements.txt`

## Dataset Attribute Information:

1. Date : (DD/MM/YYYY) Day, month ('june' to 'september'), year (2012) Weather data observations
2. Temp : temperature noon (temperature max) in Celsius degrees: 22 to 42
3. RH : Relative Humidity in %: 21 to 90
4. Ws :Wind speed in km/h: 6 to 29
5. Rain: total day in mm: 0 to 16.8 FWI Components
6. Fine Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5
7. Duff Moisture Code (DMC) index from the FWI system: 1.1 to 65.9
8. Drought Code (DC) index from the FWI system: 7 to 220.4
9. Initial Spread Index (ISI) index from the FWI system: 0 to 18.5
10. Buildup Index (BUI) index from the FWI system: 1.1 to 68
11. Fire Weather Index (FWI) Index: 0 to 31.1
12. Classes: two classes, namely fire and not fire.

Visit this link for more information about the fire index features:
https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system

## Makefile Commands

Before anything, we recommend creating a seperate environment. Make sure you have mamba installed, then simply run the following to setup:

```
make env
conda activate fires
```

### List of Convenient Makefile Commands

- `make clean`: delete all the intermediate data, model, and all the figures.
- `make nuke`: :warning: beside from doing everthing `make clean` does, this command will also delete the pretrained grid search cross validation file for the random forest model. This is not recommended because re-training might take more than 10 minutes.
- `make all`: reproduce all the figures and data needed by `main.ipynb`.
- `make test`: run tests for the utility functions.

### Reproducing the Figures

You can reproduce specific figures by typing `make figures/figure_x.png`. The `x` is a number from 1 ~ 10 which corresponds to the figure number you want to reproduce.
