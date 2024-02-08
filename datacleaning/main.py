import pandas as pd
import numpy as np
import pandas as pd

def transform_float_col(input: pd.Series) -> pd.Series:
    return input.replace(',', '', regex=True).astype('float')

data = pd.read_csv("datacleaning\\data\\Dataset 1 - Employment Projections by Industry.xlsx - Sheet1.csv").replace("*", float('nan'))

data_2021 = data["2021"]
data_2021 = transform_float_col(data_2021)

print(data_2021.std())

    
        
        
