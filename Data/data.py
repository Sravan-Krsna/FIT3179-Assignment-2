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

df1 = data_2021[['Country Name', 'Property Rights']]
df1['right'] = 'Property Rights'
df1.columns = ['Country', 'Score', 'Right']
#print(df1)

#print(data_2021['Judical Effectiveness'])
df2 = data_2021[['Country Name', 'Judical Effectiveness']]
df2['right'] = 'Judical Effectiveness'
df2.columns = ['Country', 'Score', 'Right']
#print(df2)

df3 = data_2021[['Country Name', 'Government Integrity']]
df3['right'] = 'Government Integrity'
df3.columns = ['Country', 'Score', 'Right']

df4 = data_2021[['Country Name', 'Tax Burden']]
df4['right'] = 'Tax Burden'
df4.columns = ['Country', 'Score', 'Right']

df5 = data_2021[['Country Name', "Gov't Spending"]]
df5['right'] = "Gov't Spending"
df5.columns = ['Country', 'Score', 'Right']

df6 = data_2021[['Country Name', "Fiscal Health"]]
df6['right'] = "Fiscal Health"
df6.columns = ['Country', 'Score', 'Right']

df7 = data_2021[['Country Name', "Business Freedom"]]
df7['right'] = "Business Freedom"
df7.columns = ['Country', 'Score', 'Right']

df8 = data_2021[['Country Name', "Labor Freedom"]]
df8['right'] = "Labor Freedom"
df8.columns = ['Country', 'Score', 'Right']

df9 = data_2021[['Country Name', "Monetary Freedom"]]
df9['right'] = "Monetary Freedom"
df9.columns = ['Country', 'Score', 'Right']

df10 = data_2021[['Country Name', "Trade Freedom"]]
df10['right'] = "Trade Freedom"
df10.columns = ['Country', 'Score', 'Right']

df11 = data_2021[['Country Name', "Investment Freedom "]]
df11['right'] = "Investment Freedom"
df11.columns = ['Country', 'Score', 'Right']

df12 = data_2021[['Country Name', "Financial Freedom"]]
df12['right'] = "Financial Freedom"
df12.columns = ['Country', 'Score', 'Right']

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)

df.to_csv("factors.csv")


