import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

from tools import utils


def test_normalize_simple():
    '''
    Simple test for correct dimension and value
    '''
    dummy = pd.DataFrame({"1": [1, 2], "2": [3, 4]})
    utils.normalize(dummy, ["1"])

    try:
        assert np.isclose(dummy["1"].values, [-0.70710678,  0.70710678]).all()
    except AssertionError as detail:
        msg = "The normalization is not correct."
        raise AssertionError(detail.__str__() + "\n" + msg)

    try:
        assert dummy.shape == (2, 2)
    except AssertionError as detail:
        msg = "The dimension of the data should not be changed"
        raise AssertionError(detail.__str__() + "\n" + msg)


def test_normalize_null():
    '''
    Test for null norm features.
    '''
    dummy = pd.DataFrame({"1": [1, 2]})
    utils.normalize(dummy, [])
    try:
        assert np.isclose(dummy["1"].values, [1, 2]).all()
    except AssertionError as detail:
        msg = "The original dataframe should not be changed."
        raise AssertionError(detail.__str__() + "\n" + msg)


def test_preprocess_data_shape():
    '''
    Test that the forest fire data have the correct shape after preprocessing
    '''
    data = pd.read_csv("data/Algerian_forest_fires_dataset_CLEANED.csv")
    X, y = utils.preprocess_data(data, ['Classes', 'year', 'DC', 'BUI'])
    try:
        assert X.shape == (243, 11)
    except AssertionError as detail:
        msg = "The X matrix have falsy dimension. The correct dimension should be (243, 11)."
        raise AssertionError(detail.__str__() + "\n" + msg)
    try:
        assert y.shape == (243,)
    except AssertionError as detail:
        msg = "The y matrix have falsy dimension. The correct dimension should be (243,)."
        raise AssertionError(detail.__str__() + "\n" + msg)


def test_restructure_data():
    '''
    Load in forest fire dataset and restructure the data.
    Check for the correct dimension.
    '''
    data = pd.read_csv("data/Algerian_forest_fires_dataset_UPDATE.csv")
    data["Bejaia Region Dataset "] = data["Bejaia Region Dataset "].str.replace(r'\s', '', regex=True)
    data = data.reset_index()
    column_names = data.iloc[0, :].str.replace(r'\s', '', regex=True).values
    header_index = data[data["Bejaia Region Dataset "] == "Classes"].index
    cleaned = utils.restructure_data(data, header_index, column_names)
    try:
        assert cleaned.shape == (243, 15)
    except AssertionError as detail:
        msg = "The restructured table have falsy dimension. The correct dimension should be (243, 15)."
        raise AssertionError(detail.__str__() + "\n" + msg)