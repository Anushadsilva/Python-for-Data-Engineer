import pandas as pd
from sklearn.preprocessing import OneHotEncoder

x = pd.DataFrame({"input1": [1,2,3,4,5],
                  "input2": ["A","A","B","B","C"],
                  "input3": ["X","X","X","Y","Y"]})

categorical_vars = ["input2", "input3"]

one_hot_encoder = OneHotEncoder(sparse_output= False , drop = "first")
encoder_vars_array = one_hot_encoder.fit_transform(x)
encoder_vars_array = one_hot_encoder.fit_transform(x[categorical_vars])
print(encoder_vars_array)

encoder_features_names = one_hot_encoder.get_feature_names_out(categorical_vars)
print(encoder_features_names)

encoder_vars_df = pd.DataFrame(encoder_vars_array, columns = encoder_features_names)
print(encoder_vars_df)

X_new = pd.concat([x.reset_index(drop=True), encoder_vars_df.reset_index(drop=True)], axis=1)
print(X_new)

X_new.drop(categorical_vars, axis=1, inplace=True)
print(X_new)

