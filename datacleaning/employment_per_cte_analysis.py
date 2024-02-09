import pandas as pd

employment_data = pd.read_csv("datacleaning\\data\\Employment To NAICS code per county.csv")
naics_to_cte_code = pd.read_csv("datacleaning\\data\\NAICS to CTE Code.csv")


def process(county_name: str) -> None:
    RESULT_FILE = "CTE code to employment for " + county_name + ".csv"
    
    county_data_final: dict[str, list] = {
        'CTE': [],
        'Employment': []
    }

    employment_data_for_county = employment_data[
        employment_data['Area Name'] == (county_name.capitalize() + " County")
    ]
    for row_label, row in employment_data_for_county.iterrows():
        naics_code = str(row["NAICS Code"])
        industry_code_col = naics_to_cte_code["Industry Code"].astype('str')
        print(naics_code + "0000")
        try:
            cte_code = naics_to_cte_code[ industry_code_col == (naics_code + "0000") ].iloc[0].at["CTE"]
        except:
            continue
        employment = row["Average Employment"]
        if employment == "*":
            employment = float('nan')
        county_data_final['CTE'].append(cte_code)
        county_data_final['Employment'].append(employment)
    
    pd.DataFrame(county_data_final).to_csv(RESULT_FILE)

process("Cabarrus")


        
    

