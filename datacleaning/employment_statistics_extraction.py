import pandas as pd

data = pd.read_csv("datacleaning\\data\\Employment Data.csv")



'''
for year in [2017, 2018, 2019, 2020, 2021, 2022]:
    print("Year " + str(year))
    data_for_year = data[ data["Year"] == year ]
    data_for_year = data_for_year.sort_values(by = "Unemployment Rate(%)", ascending = False)
    
    for i in range(0,3):
        county_data = data_for_year.iloc[i]
        print("Rank #" + str(i+1) + ": " + county_data["Area Name"])
        print("Unemployment percent: " + str(county_data["Unemployment Rate(%)"]) + "%")
'''

data_for_2019 = data[ data["Year"] == 2019 ]
data_for_2019 = data_for_2019.sort_values(by = "Unemployment Rate(%)", ascending = False)
unemployment_percent_data: pd.DataFrame = data_for_2019.loc[:, ["Area Name", "Unemployment Rate(%)"] ]


percentage_to_counties_dict: dict[float, list[str]] = {}

for row_label, row in unemployment_percent_data.iterrows():
    try:
        percentage_to_counties_dict[row["Unemployment Rate(%)"]].append(row["Area Name"])
    except:
        percentage_to_counties_dict[row["Unemployment Rate(%)"]] = [row["Area Name"]]

for percentage in percentage_to_counties_dict.keys():
    print("Counties with " + str(percentage) + "% unemployment: " + str(percentage_to_counties_dict[percentage]))
    print("---------")


