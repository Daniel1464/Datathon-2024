import pandas as pd
import math
import numpy as np
import csv

data = pd.read_csv("datacleaning\\data\\CSV_Test.csv")

data.row_

cleaned_data = pd.DataFrame()

counter: int = 0

#with open()
for i in data.index:
    row: pd.Series = data.iloc[i]
    is_valid = True
    for category in row.keys():
        try:
            if math.isnan(float(row[category])):
                is_valid = False
                break
        except:
            continue
    if is_valid:
        pd.concat([])
        counter += 1

cleaned_data.to_csv("datacleaning\\data\\CSV_Test_cleaned.csv")
    
        
        
