import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/mamduhhalawa/Desktop/World_data/world-data-2023.csv')
df.info()
df.describe()
df.columns

# Which factors are most associatd with high CO-2 emissions?
df.sort_values(by='Co2-Emissions')
df[['Co2-Emissions','Country']].sort_values(by='Co2-Emissions', ascending=True)
df[['Co2-Emissions']]





