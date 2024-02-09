import pandas as pd
import math

main_data: pd.DataFrame = pd.read_csv("datacleaning\\data\\# of Classes per County.csv")
agency_code_to_county_data = pd.read_csv("datacleaning\\data\\Agency Number to School Region.csv")
nonexistent_codes: list[int] = []

school_code_series = agency_code_to_county_data["School Code"]

#year = int
#county = str
#concentrators = int


county_to_concentrators_dict: dict[tuple[str, int], int] = {}


print("Started!")

def process(row_label, row: pd.Series) -> None:
    county_info = row["county"]
    if county_info == "" or (type(county_info) is float and math.isnan(county_info)):
        agency_code = str(row["agency_code"])
        # excludes single preceding zero if present
        if agency_code[0] == "0":
            agency_code = agency_code[1:]
        comparator = (school_code_series == agency_code) | (school_code_series == ("0" + agency_code))
        if not comparator.any():
            print("No data!")
            return
        
        filtered_data: pd.DataFrame = agency_code_to_county_data[comparator]

        if (filtered_data.empty):
            nonexistent_codes.append(row["agency_code"])
            return

        district_name_row = filtered_data.iloc[0]
        district_name: str = district_name_row["District Name"]

        dash_index = district_name.find("-")
        space_index = district_name.find(" ")

        if dash_index == -1:
            dash_index = 100
        if space_index == -1:
            space_index = 100

        try:
            county_name = district_name[0:min(dash_index, space_index)]
            county_to_concentrators_dict[
                (county_name, int(row["year"]))
            ] += int(row["num_concentrators"])
        except IndexError:
            print("Index error!")
        except KeyError:
            county_to_concentrators_dict[
                (county_name, int(row["year"]))
            ] = int(row["num_concentrators"])
        


for row_label, row in main_data.iterrows():
    process(row_label, row)


county_values: list[str] = []
year_values: list[int] = []
concentrator_values: list[int] = []

for county, year in county_to_concentrators_dict.keys():
    county_values.append(county)
    year_values.append(year)
    concentrator_values.append(
        county_to_concentrators_dict[ (county, year) ]
    )
    

#print(nonexistent_codes)
    
pd.DataFrame(
    [county_values, year_values, concentrator_values], columns = ['County', 'Year', 'Num Concentrators']
).to_csv("Num of ")


print("Done!")

