import numpy as np
import pandas as pd
import scipy

def transform_float_col(input: pd.Series) -> pd.Series:
    return input.replace(',', '', regex=True).astype('float')

concentrator_data = pd.read_csv("datacleaning\\data\\GroupedDataset4.csv").replace("*", float('nan'))
employment_data = pd.read_csv("datacleaning\\data\\Dataset 6 - NC Occupational Outcomes 1 Year After Grad.xlsx - Sheet1.csv").replace("*", float('nan'))

for year in range(2017,2022):
    print("Year: " + str(year))
    year_concentrator_data = concentrator_data[concentrator_data['Year'] == year]
    year_concentrator_data = year_concentrator_data.sort_values(by = "NumConcentrators", ascending = False)

    year_employment_data = employment_data.iloc[year - 2017]
    if int(year_employment_data.at["Year"]) != year:
        raise Exception("Problems are occuring.")
    #print(year_employment_data.to_numpy())


    for i in range(0,3):
        concentrators = year_concentrator_data.iloc[i].at["NumConcentrators"]
        name: str = year_concentrator_data.iloc[i].at["CTEcode"]

        num_employed_str = year_employment_data.at[name]
        if type(num_employed_str) is str:
            num_employed_str = num_employed_str.replace(",", "")
        num_employed = float(num_employed_str)

        percent_concentrators_employed = 100.0 * num_employed / concentrators
        print("Industry " + name + " has " + str(percent_concentrators_employed) + " percent of concentrators employed.")
    











    
    

# 2017: AGNR



# means
#2017: 8215
#2019: 3739.133333333333
#2022: 7291.6875

#medians
#2017: 6487
#2019: 3176.0
#2022: 5346.5








    
        
        
