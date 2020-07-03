import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


data = pd.read_csv('../resources/research.csv', encoding="utf_16_le")
print(data.describe())
y = data.maths
X = data[['language', 'science', 'history']]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

model = RandomForestRegressor(random_state=1)
model.fit(train_X, train_y)

preds = model.predict(val_X)
print(mean_absolute_error(val_y, preds))
