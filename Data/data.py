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
"""
countries = data_2021['Country Name'].to_list()
print(countries)
"""
countries = ["Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Cabo Verde", 
"Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the Congo", "Congo, Republic of", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
"Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
"Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North" , "Korea, South", "Kosovo", "Kuwait", "Kyrgyz Republic", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "North Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", 
"Mexico", "Micronesia", "Moldova", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", 
"São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", 
"Switzerland", "Syria", "Taiwan" , "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
"Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]


#print(data_2021.columns)

df1 = data_2021[['Country Name', 'Region', 'Property Rights', "Unemployment (%)"]]
df1['right'] = 'Property Rights'
df1.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']
#print(df1)

#print(data_2021['Judical Effectiveness'])
df2 = data_2021[['Country Name', 'Region', 'Judical Effectiveness', "Unemployment (%)"]]
df2['right'] = 'Judical Effectiveness'
df2.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']
#print(df2)

df3 = data_2021[['Country Name', 'Region', 'Government Integrity', "Unemployment (%)"]]
df3['right'] = 'Government Integrity'
df3.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df4 = data_2021[['Country Name', 'Region', 'Tax Burden', "Unemployment (%)"]]
df4['right'] = 'Tax Burden'
df4.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df5 = data_2021[['Country Name', 'Region', "Gov't Spending", "Unemployment (%)"]]
df5['right'] = "Gov't Spending"
df5.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df6 = data_2021[['Country Name', 'Region', "Fiscal Health", "Unemployment (%)"]]
df6['right'] = "Fiscal Health"
df6.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df7 = data_2021[['Country Name', 'Region', "Business Freedom", "Unemployment (%)"]]
df7['right'] = "Business Freedom"
df7.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df8 = data_2021[['Country Name', 'Region', "Labor Freedom", "Unemployment (%)"]]
df8['right'] = "Labor Freedom"
df8.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df9 = data_2021[['Country Name', 'Region', "Monetary Freedom", "Unemployment (%)"]]
df9['right'] = "Monetary Freedom"
df9.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df10 = data_2021[['Country Name', 'Region', "Trade Freedom", "Unemployment (%)"]]
df10['right'] = "Trade Freedom"
df10.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df11 = data_2021[['Country Name', 'Region', "Investment Freedom ", "Unemployment (%)"]]
df11['right'] = "Investment Freedom"
df11.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df12 = data_2021[['Country Name', 'Region', "Financial Freedom", "Unemployment (%)"]]
df12['right'] = "Financial Freedom"
df12.columns = ['Country', 'Region', 'Score', "Unemployment (%)", 'Right']

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)

#print(df)
df.to_csv("factors.csv")


