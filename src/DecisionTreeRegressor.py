import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


data = pd.read_csv('../resources/research.csv', encoding="utf_16_le")
print(data.describe())
y = data.maths
X = data[['language', 'science', 'history']]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

print()

best_leafs_count = 10
best_mae_result = 99999999999999999
for mln in range(4, 10):
    mae = get_mae(mln, train_X, val_X, train_y, val_y)
    if mae < best_mae_result:
        best_mae_result = mae
        best_leafs_count = mln

print(best_leafs_count)
