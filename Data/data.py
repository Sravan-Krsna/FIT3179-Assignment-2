import pandas as pd

data_2021 = pd.read_csv("Data/index2021_data.csv")
data_2019 = pd.read_csv("Data/index2019_data.csv")
#print(data_2021.columns)
#unemployment = data_2021[['Country Name', 'Unemployment (%)']]
#unemployment_2019 = data_2019[['Country Name','Unemployment (%)']]
#unemployment.rename(columns={'Unemployment (%)':'2021'}, inplace=True)
data = pd.read_csv("Data/unemployment2019.csv")
data2 = pd.read_csv("Data/Unemployment2021.csv")
data = data.append(data2, ignore_index=True)
data.to_csv("unemployment.csv")
