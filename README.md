# YZV 202E TERM PROJECT

## Project Description

M2 Metro line of Istanbul is one of the busiest metro lines in Europe.
Being one of the busiest, it is crucial to schedule and optimize the
operations of the metro line. 

Here, we try to optimize for the "effectiveness", for the M2 metro line. 
Effectiveness is an abstract term by itself. It represents here the 
combined optimization of traffic near the metro stations, density of the 
crowd in the metro stations and the cost of operation. The main goal is 
to minimize all said factors together. Traffic and density data is pulled 
from datasets. Cost of operation is measured through the frequency of 
metro services.

## Datasets and Data Preprocessing

3 main datasets are found for this project. The objective of the preprocessing
of these datasets are to prepare them for the optimization algorithms. 

- Preprocessed datasets need to include only needed sections of the data.
- Used preprocessing methods need to return Dataframes.
- Create a "Preprocessing" class and provide methods under it.

Above 2 requirements are valid through all datasets. However, there are
exclusive requirements for each of the 2 datasets.

### Hourly Public Transport Dataset

[Hourly Public Transport Dataset](https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set)
is a dataset of Istanbul Municipality, including the payment records of
public transport users by their transport cards. The dataset includes hourly
counts of people that use a specific transport line.

- Collect data for only April 2024.
- Collect data for only M2 metro line.
- Provide hourly data for only user counts throughout April 2024.
- Provide plots for the count of users, hour by hour, throughout April 2024.
- Create a reduced dataset as a .csv file.

### Railway Station Vector Dataset

[Railway Station Vector Dataset](https://data.ibb.gov.tr/dataset/rayli-ulasim-istasyonlari-vektor-verisi)
is a dataset of Istanbul Municipality, providing the area information
for each of the metro, tram, etc. stations in Istanbul.

- Calculate the total area of each M2 metro station.
- Provide a total feasible number of people index for each of the stations.
- Collect above information in a .json file.

## Methods

For data preprocessing; Numpy, and Pandas is recommended. 
