import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/mamduhhalawa/Desktop/World_data/world-data-2023.csv')

# Look at columns related to education and economy
df.info()
df.describe()
df.columns
df.value_counts()

# Drop unrelated columns
df = df.drop(columns=['Capital/Major City'])
df = df.drop(columns=['Armed Forces size'])
df = df.drop(columns=['Calling Code'])
df = df.drop(columns=['Currency-Code'])
df = df.drop(columns=['Agricultural Land( %)'])
df = df.drop(columns=['Co2-Emissions'])
df = df.drop(columns=['Forested Area (%)'])
df = df.drop(columns=['Gasoline Price'])
df = df.drop(columns=['Largest city'])
df = df.drop(columns=['Official language'])
df = df.drop(columns=['Out of pocket health expenditure'])
df = df.drop(columns=['Latitude'])
df = df.drop(columns=['Longitude'])
df = df.drop(columns=['Tax revenue (%)'])
df = df.drop(columns=['Total tax rate'])
df = df.drop(columns=['Urban_population'])
df.info()

# Clean columns and make them numeric
df['Density\n(P/Km2)'] = df['Density\n(P/Km2)'].str.replace(",",'.')
df['Density\n(P/Km2)'] = pd.to_numeric(df['Density\n(P/Km2)'])
df['Land Area(Km2)'] = df['Land Area(Km2)'].str.replace('.','')
df['Land Area(Km2)'] = pd.to_numeric(df['Land Area(Km2)'])
df['CPI'] = df['CPI'].str.replace(".",'')
df['CPI'] = df['CPI'].str.replace(",",'')
df['CPI'] = pd.to_numeric(df['CPI'])
df['CPI Change (%)'] = df['CPI Change (%)'].str.replace("%",'')
df['CPI Change (%)'] = pd.to_numeric(df['CPI Change (%)'])
df['CPI Change (%)']
df['GDP'] = df['GDP'].str.replace('$','')
df['GDP'] = df['GDP'].str.replace(',','')
df['GDP'] = pd.to_numeric(df['GDP'])
df['Gross primary education enrollment (%)'] = df['Gross primary education enrollment (%)'] .str.replace(',','')
df['Gross primary education enrollment (%)'] = df['Gross primary education enrollment (%)'].str.replace('%','')
df['Gross primary education enrollment (%)'] = pd.to_numeric(df['Gross primary education enrollment (%)'])
df['Gross tertiary education enrollment (%)'] = df['Gross tertiary education enrollment (%)'].str.replace('%','')
df['Gross tertiary education enrollment (%)'] = pd.to_numeric(df['Gross tertiary education enrollment (%)'])
df['Minimum wage'] = df['Minimum wage'].str.replace('$','')
df['Minumum wage'] = pd.to_numeric(df['Minimum wage'])
df['Population'] = df['Population'].str.replace(',','')
df['Population'] = pd.to_numeric(df['Population'])
df['Population'] = df['Population'].str.replace(',','')
df['Population'] = pd.to_numeric(df['Population'])
df['Population: Labor force participation (%)'] = df['Population: Labor force participation (%)'].str.replace('%','')
df['Population: Labor force participation (%)'] = pd.to_numeric(df['Population: Labor force participation (%)'])
df['Unemployment rate'] = df['Unemployment rate'].str.replace('%','')


df = df.sort_values(by='Gross tertiary education enrollment (%)')
df['Gross tertiary education enrollment (%)'].iloc[:3].plot(x='Country', y='Gross tertiary education enrollment (%)',kind='barh')



df.sort_values(by='Population: Labor force participation (%)')






