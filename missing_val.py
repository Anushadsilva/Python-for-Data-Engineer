import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

from sklearn.impute import KNNImputer


my_df = pd.DataFrame({"A":[1,2,3,np.nan,5,np.nan,7],
                     "B":[4,np.nan,7,np.nan,1,np.nan,2]})

#findidng missingval

print(my_df.isna())
print(my_df.isna().sum())


print(my_df.dropna())

print(my_df.dropna(how = "any"))
print(my_df.dropna(how = "all"))

print(my_df.dropna(how = "any", subset=["A"]))

print(my_df.dropna(how = "any", inplace=True))
print(my_df)

#filling rows:

my_df = pd.DataFrame({"A":[1,2,3,np.nan,5,np.nan,7],
                     "B":[4,np.nan,7,np.nan,1,np.nan,2]})

print(my_df.fillna(value = 100))

mean_value = my_df["A"].mean()
print(mean_value)
print(my_df["A"].fillna(value = mean_value))

print(my_df.fillna(value = mean_value, inplace = True))



#simpleimputer

my_df = pd.DataFrame({"A":[1,2,3,1,8],
                      "B":[3,6,9,np.nan,15],
                      "C":[4,np.nan,9,np.nan,15]})
imputer = SimpleImputer()

print(imputer.fit(my_df))
print(imputer.transform(my_df))


my_df1 = imputer.transform(my_df)
print(my_df1)

imputer.fit_transform(my_df)


#KNN imputer

my_df = pd.DataFrame({"A":[1,2,3,4,5],
                      "B":[4,5,6,7,8],
                      "C":[9,10,11,np.nan,13]})
print(my_df)

knn_imputer = KNNImputer()

knn_imputer = KNNImputer(n_neighbors = 1)
knn_imputer = KNNImputer(n_neighbors = 3)
nn_imputer = KNNImputer(n_neighbors = 3, weights = "distance")
print(knn_imputer.fit_transform(my_df))

my_df1 = pd.DataFrame(knn_imputer.fit_transform(my_df),columns=my_df.columns)
print(my_df1)



