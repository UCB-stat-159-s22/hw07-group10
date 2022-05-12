FIGURES=$(wildcard figures/*.png)
NOTEBOOKS=$(wildcard *.ipynb)
CLEANED=data/Algerian_forest_fires_dataset_CLEANED.csv

# Intermediate data csv
data/Algerian_forest_fires_dataset_CLEANED.csv : data_cleaning.ipynb data/Algerian_forest_fires_dataset_UPDATE.csv
	jupyter execute $<

figures/figure_1.png : EDA.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_2.png : EDA.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_3.png : EDA.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_4.png : EDA.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_5.png : models.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_6.png : models.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_7.png : models.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_8.png : models.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_9.png : models.ipynb $(CLEANED)
	jupyter execute $<

figures/figure_10.png : models.ipynb $(CLEANED)
	jupyter execute $<

.PHONY : env
env : 
	bash -i envsetup.sh

.PHONY : models
models : models.ipynb $(CLEANED)
	jupyter execute $<

.PHONY : eda
eda : EDA.ipynb $(CLEANED)
	jupyter execute $<

.PHONY : all
all : $(NOTEBOOKS) $(CLEANED)
	jupyter execute EDA.ipynb
	jupyter execute models.ipynb
	jupyter execute main.ipynb

.PHONY : test
test : $(CLEANED)
	pytest tools

.PHONY : clean
clean :
	rm -f $(CLEANED)
	rm -f $(FIGURES)
	rm -f models/random_forest.pkl
	
.PHONY : nuke
nuke :
	rm -f $(CLEANED)
	rm -f $(FIGURES)
	rm -f models/random_forest.pkl
	rm -f models/random_forest_gridcv.pkl