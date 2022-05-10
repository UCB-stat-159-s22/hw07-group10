#!/bin/bash -i

mamba env create -f environment.yml
conda activate fires
python -m ipykernel install --user --name fires --display-name "IPython - Forest Fires"
pip install .