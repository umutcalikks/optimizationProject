# Hourly Public Transport (M2) Dataset

import pandas as pd
import numpy as np

def filter_m2_lines(file_path):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)
        
        # Filter records where 'Line' column contains 'M2'
        filtered_data = data[data['Line'] == 'M2']
        
        # Display the filtered data
        print(filtered_data)
    except Exception as e:
        print("An error occurred:", e)

# Update the file path 
filter_m2_lines('/Users/umut/Downloads/April 2024 Toplu Ula__m Verisi.csv')

# Define a date range for the month of April 2024
date_range = pd.date_range(start="2024-04-01", end="2024-04-30", freq='D')

# Create a dataframe for every hour of each day in April with random passenger numbers
all_dates_hours = pd.DataFrame({
    "transition_date": [date.strftime("%Y-%m-%d") for date in date_range for _ in range(24)],
    "transition_hour": [f"{hour:02}:00:00" for _ in date_range for hour in range(24)],
    "line": "YENIKAPI - HACIOSMAN",
    "number_of_passenger": [np.random.randint(100, 900) for _ in date_range for _ in range(24)],
    "transaction_type_desc": np.random.choice(["Tam Kontur", "Indirimli Abonman", "Ucretsiz"], size=len(date_range)*24, p=[0.5, 0.3, 0.2]),
    "town": "SISLI",
    "line_name": "M2"
})

# Remove the 'product_kind' column
all_dates_hours = all_dates_hours.drop(columns=['product_kind'])

# Preview the data to ensure it looks correct
all_dates_hours.head()




