# Multiple Linear Regression


# =============================================================================
# 此代碼與原作"機器學習A-Z"有差別，差別如下:
# 1. 新增 columntransformer 來轉換onehotencoder
# 2. import statsmodels.regression.linear_model as sm --> import statsmodels.regression.linear_model as sm
# 3. 新增 X_opt = np.array(X_opt,dtype=float)，為了餵進去OLS模型當中(需同一型態)。
# =============================================================================

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
ct=ColumnTransformer(transformers=[('onehotencoder',OneHotEncoder(),[3])],remainder='passthrough')
X = ct.fit_transform(X)

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)




# Building the optimal model using Backward Elimination 反向淘汰實作
import statsmodels.regression.linear_model as sm
X_train = np.append(arr = np.ones((40, 1)).astype(int), values = X_train, axis = 1)
X_opt = X_train [:, [0, 1, 2, 3, 4, 5]]
X_opt = np.array(X_opt,dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train [:, [0, 1, 3, 4, 5]]
X_opt = np.array(X_opt,dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train [:, [0, 3, 4, 5]]
X_opt = np.array(X_opt,dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train [:, [0, 3, 5]]
X_opt = np.array(X_opt,dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train [:, [0, 3]]
X_opt = np.array(X_opt,dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()





