import numpy as np
import pandas as pd

def transform_float_col(input: pd.Series) -> pd.Series:
    return input.replace(',', '', regex=True).astype('float')

data = pd.read_csv("datacleaning\\data\\Dataset 1 - Employment Projections by Industry.xlsx - Sheet1.csv").replace("*", float('nan'))

net_growth = transform_float_col(data["Annualized"].replace("%", "", regex = True))

print(net_growth.mean())
print(net_growth.median())
# print(net_growth.std())