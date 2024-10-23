
 # Railway Station Vector Dataset

import json
import pandas as pd

# Open the JSON file and load its contents
with open('/Users/umut/Downloads/Rayl_ Sistem _stasyon Alanlar_ Verisi.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Process the data from 'records'
records = json_data['records']  # This path may vary depending on your JSON structure

# Code to process the data:
output_data = []
for i in range(len(records)):
    if "\"properties\" :" in records[i][1]:
        properties_dict = {}
        j = i + 1
        while "}" not in records[j][1]:
            prop_line = records[j][1].strip().replace('\t', '').replace(',', '')
            if ':' in prop_line:
                key, value = prop_line.split(':', 1)
                key = key.replace('"', '').strip()
                value = value.replace('"', '').strip()
                properties_dict[key] = value
            j += 1

        # Convert properties information into a JSON string
        properties_str = json.dumps(properties_dict, ensure_ascii=False)
        output_data.append({'Information': 'Properties', 'Data': properties_str})

        # Collect coordinates information
        coordinates_list = []
        k = j + 1  # Start at the beginning of the coordinates block
        while ']' not in records[k][1]:  # Continue until all coordinates are collected
            coord_line = records[k][1].strip().replace('\t', '').replace(',', '')
            if '[' in coord_line and ']' not in coord_line:
                coord_value = coord_line.split('[')[1].strip()
                if coord_value:  # Exclude empty values
                    coordinates_list.append(float(coord_value))
            k += 1
        output_data.append({'Information': 'Coordinates', 'Data': coordinates_list})

# Create a DataFrame from the processed data
output_df = pd.DataFrame(output_data)
print(output_df.head(50))  # Display the first few entries
