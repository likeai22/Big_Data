import opendatasets as od
import pandas as pd
from pathlib import Path


dataset_path = Path('new-york-city-airbnb-open-data', 'AB_NYC_2019.csv')
if not dataset_path.is_file():
    od.download('https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data')

df = pd.read_csv(dataset_path)

print(df.head())

mean_price = df['price'].mean()
variance_price = df['price'].var()

print(f"Mean price: {mean_price}")
print(f"Variance price: {variance_price}")
