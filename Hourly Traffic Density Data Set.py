
# Hourly Traffic Density Data Set


import pandas as pd

def filter_and_save_csv(file_path):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path, delimiter=',')
        

        # Filter the data for the specified geohash
        filtered_data = data[data['GEOHASH'] == 'sxkcgj']
        
        # Sort the data by 'DATE_TIME'
        sorted_data = filtered_data.sort_values(by='DATE_TIME')


        # Select only the 'NUMBER_OF_VEHICLES', 'LONGITUDE', and 'LATITUDE' columns
        reduced_data = filtered_data[['DATE_TIME', 'NUMBER_OF_VEHICLES', 'LONGITUDE', 'LATITUDE']]
        
        # Save the reduced data to a new CSV file, without displaying the 'GEOHASH' column
        reduced_csv_path = 'Reduced_Trafik_Yogunluk_Verisi.csv'
        reduced_data.to_csv(reduced_csv_path, index=False)
        
        print("File saved successfully as:", reduced_csv_path)
    except Exception as e:
        print("An error occurred:", e)


def load_and_display_csv(file_path):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)
        
        # Display the data
        print(data)
    except Exception as e:
        print("An error occurred while loading the file:", e)

# The path to CSV file
filter_and_save_csv('Enter path of csv file here')

# The path to reduced CSV file
load_and_display_csv('Reduced_Trafik_Yogunluk_Verisi.csv')

