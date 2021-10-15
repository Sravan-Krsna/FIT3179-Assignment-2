import pandas as pd

data_2021 = pd.read_csv("Data/index2021_data.csv")
data_2019 = pd.read_csv("Data/index2019_data.csv")
print(data_2021.columns)
unemployment = data_2021[['Country Name', 'Unemployment (%)']]
unemployment_2019 = data_2019[['Country Name','Unemployment (%)']]
#unemployment.rename(columns={'Unemployment (%)':'2021'}, inplace=True)
unemployment.to_csv("unemployment2021.csv")
unemployment_2019.to_csv("unemployment2019.csv")
