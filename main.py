import numpy as np
import pandas as pd

df = pd.read_csv('laptop_price.csv', encoding='ISO-8859-1')
print(df, "\n---------------------")

# *** PART A: Summarizing ***

print(df.info(), "\n---------------------")

print(df.describe(), "\n---------------------")

company_counts = df['Company'].value_counts()
print(company_counts, "\n---------------------")

# *** PART B: Modifying ***

df['Weight'] = df['Weight'].str.replace('kg', '')
df['Weight'] = df['Weight'].astype(float)
df.rename(columns={'Weight': 'Weight_kg'}, inplace=True)
print(df[['Weight_kg']].head(), "\n---------------------")

exchange_rate = 1.1 # 1 Euro = $1.10 USD
df['Price_usd'] = df['Price_euros'] * exchange_rate
print(df[['Price_euros', 'Price_usd']].head(), "\n---------------------")

# *** PART C: Filtering ***

apple_laptops = df[df['Company'] == 'Apple']
print("APPLE LAPTOPS: \n", apple_laptops, "\n---------------------")

large_screens = df[df['Inches'] > 15]
print("LARGE SCREENS: \n", large_screens, "\n---------------------")

mid_range_laptops = df[(df['Price_usd'] >= 500) & (df['Price_usd'] <= 1000)]
print("MID PRICE RANGE: \n", mid_range_laptops, "\n---------------------")

gaming_laptops = df[(df['Gpu'].str.contains('Nvidia|AMD', case=False)) & 
                    (df['TypeName'].str.contains('Gaming', case=False))]
print("GAMING LAPTOPS: \n", gaming_laptops, "\n---------------------")

