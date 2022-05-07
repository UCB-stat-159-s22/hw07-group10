import pandas as pd


def normalize(data, norm_features=[]):
    '''
    Normalize data across specified features.

    Inputs:
    - data: data matrix
    - norm_features: list of column names to normalize

    Outputs:
    - None. Normalizing is done in place.
    '''
    if type(norm_features) != list:
        raise TypeError('norm_features must be a list')

    for feat in norm_features:
        data[feat] = (data[feat] - data[feat].mean())/data[feat].std()


def preprocess_data(data, features_to_drop=[]):
    '''
    Preprocess data by dropping specified features and encoding categorical features.

    Inputs:
    - data: data matrix
    - features_to_drop: list of column names to drop

    Outputs:
    - X: cleaned feature matrix
    - y: y vector where 1 = fire and 0 = notfire
'''
    if type(features_to_drop) != list:
        raise TypeError('norm_features must be a list')

    y = data['Classes'].values
    X = data.drop(["Unnamed: 0"], axis=1)
    X = X.drop(features_to_drop, axis=1)

    # One hot encode categorial variables
    X['Region'].loc[X['Region'] == 'Bejaia'] = 0
    X['Region'].loc[X['Region'] == 'Sidi-Bel Abbes'] = 1

    y[y == "notfire"] = 0
    y[y == "fire"] = 1
    y = y.astype(int)

    return X, y


def restructure_data(data, header_index, column_names):
    '''
    Restructure the forest_fire dataframe. Originaly the spreadsheet have two
    seperate table vertically stacked on top of each other. The two tables
    represent data collected from two different region. The function
    restructures the data so all information is contianed in one table, with
    an additional column "Region".

    Inputs:
        - data: original data matrix (with two tables stacked vertically)
        - header_index: list of index which indicate the header of each
            table.
        - column_names: the column_names of each table.

    Outputs:
        - cleaned: restructured data.
    '''
    # Locate first and second table
    first_half = data.iloc[header_index[0] + 1:header_index[1]-1, :]
    second_half = data.iloc[header_index[1]+1:, :]
    # Rename first and second table
    col_name_dict = dict(zip(first_half.columns, column_names))
    first_half = first_half.rename(col_name_dict, axis=1)
    second_half = second_half.rename(col_name_dict, axis=1)
    # Concatinate first and second table
    first_half["Region"] = "Bejaia"
    second_half["Region"] = "Sidi-Bel Abbes"
    cleaned = pd.concat([first_half, second_half], axis=0)
    cleaned = cleaned.dropna()

    return cleaned


