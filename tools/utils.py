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
        data: data matrix
        features_to_drop: list of column names to drop
    
    Outputs: 
        X: cleaned feature matrix
        y: y vector where 1 = fire and 0 = notfire
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