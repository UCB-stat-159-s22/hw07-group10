FIGURES=$(wildcard figures/*.png)

data/Algerian_forest_fires_dataset_CLEANED.csv : data_cleaning.ipynb data/Algerian_forest_fires_dataset_UPDATE.csv
	jupyter execute $<

.PHONY : EDA
EDA : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

.PHONY : env
env : 
	bash -i envsetup.sh
	pip install .

.PHONY : clean
clean :
	rm -f data/Algerian_forest_fires_dataset_CLEANED.csv
	rm -f $(FIGURES)
	
