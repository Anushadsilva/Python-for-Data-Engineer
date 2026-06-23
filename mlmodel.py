#model validation

import pandas as pd
from matplotlib.pyplot import clf

my_df = pd.read_csv("../data/0015-Feature-Selection-Data.csv")
print(my_df)

#test/train

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

X = my_df.drop("output", axis=1)
Y = my_df["output"]

x_train, x_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print(x_train.shape, x_test.shape, Y_train.shape, Y_test.shape,X.shape,Y.shape)
regressor = LinearRegression()
regressor.fit(x_train, Y_train)
print(regressor.score(x_test, Y_test))

y_pred = regressor.predict(x_test)
print(y_pred)

print(r2_score(Y_test, y_pred))



#class model
#x_train, x_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42 ,stratify=Y)



#cross vali

from sklearn.model_selection import cross_val_score, KFold , StratifiedKFold

cv_scores =cross_val_score(regressor, X,Y, cv=4, scoring='r2')
print(cv_scores)

print(cv_scores.mean())


#regression

cv = KFold(n_splits=4, shuffle=True, random_state=42)
cv_scores =cross_val_score(regressor, X,Y, cv=cv, scoring='r2')
print(cv_scores)

print(cv_scores.mean())

#Classification

cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
cv_scores =cross_val_score(clf, X,Y, cv=cv, scoring="accuracy")
print(cv_scores)


print(cv_scores.mean())


