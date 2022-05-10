FIGURES=$(wildcard figures/*.png)

# Intermediate data csv
data/Algerian_forest_fires_dataset_CLEANED.csv : data_cleaning.ipynb data/Algerian_forest_fires_dataset_UPDATE.csv
	jupyter execute $<

figures/figure_1.png : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_2.png : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_3.png : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_4.png : EDA.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_5.png : models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_6.png : models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_7.png : models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

figures/figure_8.png : models.ipynb data/Algerian_forest_fires_dataset_CLEANED.csv
	jupyter execute $<

.PHONY : env
env : 
	bash -i envsetup.sh

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
	jupyter execute main.ipynb

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