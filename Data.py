import pandas as pd

df = pd.read_csv('C:\\Users\\ap4ln\\PycharmProjects\\DataWorkflow\\finance_liquor_sales 2016-2019.csv')

print(df.info())

print(df.head())

popular_item_per_zip = df.groupby(['zip_code', 'item_description']).size().reset_index(name='count').sort_values(by='count', ascending=False).groupby('zip_code').head(1)

df['percentage_of_sales'] = df.groupby('store_name')['sale_dollars'].transform(lambda x: x / x.sum() * 100)


print("\nPercentage of Sales per Store:")
print(df[['store_name', 'percentage_of_sales']].drop_duplicates())

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(df['store_name'], df['percentage_of_sales'])
plt.xlabel('Store Name')
plt.ylabel('Percentage of Sales')
plt.title('Percentage of Sales per Store')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()
