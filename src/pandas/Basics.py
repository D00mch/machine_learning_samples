import pandas as pd

# creating DataFrames
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
print(fruits)

fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=["2017 Sales", "2018 Sales"])
print(fruit_sales)

ingredients = pd.Series(
    ['4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'],
    name='Dinner'
)
print(ingredients)

# store
fruits.to_csv("../resources/animals.csv")

# get first item in first columng
print(fruits['Apples'][0])

# get first row
print(fruits.iloc[0])

# map
print(fruits.Apples.map(lambda p: p - 10))
# or shorter
print(fruits.Apples - 10)


