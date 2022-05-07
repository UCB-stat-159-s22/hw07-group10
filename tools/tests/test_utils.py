import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

from tools import utils


def test_normalize_1():
    '''
    Simple test for correct dimension and value
    '''
    dummy = pd.DataFrame({"1": [1, 2], "2": [3, 4]})
    utils.normalize(dummy, ["1"])

    try:
        assert np.isclose(dummy["1"].values, [-1, 1]).all()
    except AssertionError as detail:
        msg = "The normalization is not correct."
        raise AssertionError(detail.__str__() + "\n" + msg)

    try:
        assert dummy.shape == (2, 2)
    except AssertionError as detail:
        msg = "The dimension of the data should not be changed"
        raise AssertionError(detail.__str__() + "\n" + msg)