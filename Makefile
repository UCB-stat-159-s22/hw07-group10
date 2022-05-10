FIGURES=$(wildcard figures/*.png)

# Intermediate data csv
data/Algerian_forest_fires_dataset_CLEANED.csv : data_cleaning.ipynb data/Algerian_forest_fires_dataset_UPDATE.csv
	jupyter execute $<
	
.PHONY : models
models : models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

.PHONY : eda
eda : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

.PHONY : all
all : EDA.ipynb models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute EDA.ipynb
	jupyter execute models.ipynb

.PHONY : env
env : 
	bash -i envsetup.sh
	pip install .

.PHONY : test
test : data/Algerian_forest_fires_dataset_CLEANED.csv
	pytest tools

.PHONY : clean
clean :
	rm -f data/Algerian_forest_fires_dataset_CLEANED.csv
	rm -f $(FIGURES)
	rm -f models/random_forest.pkl
	
.PHONY : nuke
nuke :
	rm -f data/Algerian_forest_fires_dataset_CLEANED.csv
	rm -f $(FIGURES)
	rm -f models/random_forest.pkl
	rm -f models/random_forest_gridcv.pkl