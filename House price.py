import pandas as pd
from sklearn.tree import DecisionTreeRegressor


melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price


melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features


X.describe()
X.head()

melbourne_model.fit

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

