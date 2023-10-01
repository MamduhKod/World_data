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
df.columns

# Clean columns and make them numeric
df['Density\n(P/Km2)'] = df['Density\n(P/Km2)'].str.replace(",",'.')
df['Density\n(P/Km2)'] = pd.to_numeric(df['Density\n(P/Km2)'])
df['Land Area(Km2)'] = df['Land Area(Km2)'].str.replace(',','')
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
df['Population: Labor force participation (%)'] = df['Population: Labor force participation (%)'].str.replace('%','')
df['Population: Labor force participation (%)'] = pd.to_numeric(df['Population: Labor force participation (%)'])
df['Unemployment rate'] = df['Unemployment rate'].str.replace('%','')

#Check out tertiary enrollment figures
df= df.sort_values(by='Gross tertiary education enrollment (%)',ascending=False)


# Highest enrollment
df_high_enroll = df.sort_values(by='Gross tertiary education enrollment (%)',ascending=False)
df_high_enroll.iloc[:10].plot(x='Country', y='Gross tertiary education enrollment (%)',kind='bar')
#Association betweeen labor participation and tertiary enrollment
df_high_enroll.iloc[:100].plot(x='Population: Labor force participation (%)', y='Gross tertiary education enrollment (%)',kind='scatter')

#tertiaryy education vs primary education enrollment
plt.figure(figsize=(20,10))
plt.plot(df_high_enroll.iloc[:20]['Country'],df_high_enroll.iloc[:20]['Gross tertiary education enrollment (%)'], marker='o',linestyle='-',label='Tertiary education enrollment')
plt.plot(df_high_enroll.iloc[:20]['Country'],df_high_enroll.iloc[:20]['Gross primary education enrollment (%)'], marker='o',linestyle='-',label='Primary education enrollment')
plt.title('Difference in enrollment between primary and secondary')
plt.xlabel('Countries')
plt.ylabel('% of enrollment')
plt.legend()

# Top 10 lowest enrollment
df_low_enroll = df.sort_values(by='Gross tertiary education enrollment (%)',ascending=True)
df_low_enroll.iloc[:20].plot(x='Country', y='Gross tertiary education enrollment (%)',kind='bar')

#tertiaryy education vs primary education enrollment
plt.figure(figsize=(20,10))
plt.plot(df_low_enroll.iloc[:20]['Country'],df_low_enroll.iloc[:20]['Gross tertiary education enrollment (%)'], marker='o',linestyle='-',label='Tertiary education enrollment')
plt.plot(df_low_enroll.iloc[:20]['Country'],df_low_enroll.iloc[:20]['Gross primary education enrollment (%)'], marker='o',linestyle='-',label='Primary education enrollment')
plt.title('Educational enrollment for lowest tertiary enrollment populations')
plt.xlabel('Countries')
plt.ylabel('% of enrollment')
plt.legend()

#Association betweeen labor participation and tertiary enrollment
df.iloc[:100].plot(x='Population: Labor force participation (%)', y='Gross tertiary education enrollment (%)',kind='scatter')
df['Population: Labor force participation (%)'].describe()

plt.figure(figsize=(20,10))
plt.plot(df.iloc[:20]['Country'],df.iloc[:20]['Population: Labor force participation (%)'], marker='o',linestyle='-',label='Population labor participation')
plt.plot(df.iloc[:20]['Country'],df.iloc[:20]['Gross tertiary education enrollment (%)'], marker='o',linestyle='-',label='Tertiary education enrollment')
plt.title('Tertiary vs primary enrollment')
plt.xlabel('Countries')
plt.ylabel('% of enrollment')
plt.legend()




