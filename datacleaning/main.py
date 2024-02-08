import pandas as pd
import numpy as np
import pandas as pd
import scipy

def transform_float_col(input: pd.Series) -> pd.Series:
    return input.replace(',', '', regex=True).astype('float')

data = pd.read_csv("datacleaning\\data\\GroupedDataset4.csv").replace("*", float('nan'))

data = data[data['Year'] == 2017]

print(data['Enrollment'])
# means
#2017: 8215
#2019: 3739.133333333333
#2022: 7291.6875

#medians
#2017: 6487
#2019: 3176.0
#2022: 5346.5








    
        
        
