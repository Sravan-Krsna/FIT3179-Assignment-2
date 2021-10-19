import pandas as pd

data_2021 = pd.read_csv("Data/index2021_data.csv")
data_2019 = pd.read_csv("Data/index2019_data.csv")
#print(data_2021.columns)
#unemployment = data_2021[['Country Name', 'Unemployment (%)']]
#unemployment_2019 = data_2019[['Country Name','Unemployment (%)']]
#unemployment.rename(columns={'Unemployment (%)':'2021'}, inplace=True)

"""
money = data_2021.groupby('Region')["Gov't Spending"].mean()
eu = money['Europe']
ap = money['Asia-Pacific']
mena = money['Middle East and North Africa']
ssa = money['Sub-Saharan Africa']
ame = money['Americas']
print(eu, mena, ssa, ame, ap)
print(money)

df = {'Region':['Asia-Pacific', 'Europe', 'Middle East and North Africa', 'Sub-Saharan Africa', 'Americas'],
    'Average Spending':[ap, eu, mena, ssa, ame]}

df = pd.DataFrame(df)

df.to_csv('Spending.csv')
"""

df = pd.read_csv("Data/regional_growth.csv")
growth_2021 = df[['Region', '2021']]
growth_2021.to_csv('growth_2021.csv')