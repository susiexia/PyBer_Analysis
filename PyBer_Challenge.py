# %%
%matplotlib inline
# %%
import os
import matplotlib.pyplot as plt 
import pandas as pd 
import statistics
import numpy as np 
import scipy.stats as sts 
from matplotlib.ticker import MultipleLocator

import matplotlib as mpl 

# %%
city_file_load = os.path.join('Resources', 'city_data.csv')
ride_file_load = os.path.join('Resources','ride_data.csv')

city_data_df = pd.read_csv(city_file_load)
ride_data_df = pd.read_csv(ride_file_load)
ride_data_df.info()
# %%[markdown]
## Merge two raw datasets into one 
pyber_data_df = pd.merge(ride_data_df,city_data_df,how = 'left',on=['city','city'])

### Use filter to create 3 new DF for 3 citty types
urban_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Urban')]
rural_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Rural'),:]
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]

# %%[markdown]
### generate information for create a summary DataFrame
urban_ride_numbers = urban_cities_df['ride_id'].count()
rural_ride_numbers = rural_cities_df['ride_id'].count()
suburban_ride_numbers = suburban_cities_df['ride_id'].count()

urban_fare_numbers = urban_cities_df['fare'].sum()
rural_fare_numbers = rural_cities_df['fare'].sum()
suburban_fare_numbers =suburban_cities_df['fare'].sum()

urban_driver_numbers = city_data_df[(city_data_df['type'] == 'Urban')].sum()['driver_count']
rural_driver_numbers = city_data_df[(city_data_df['type'] == 'Rural')].sum()['driver_count']
suburban_driver_numbers = city_data_df[(city_data_df['type'] == 'Suburban')].sum()['driver_count']

urban_avg_Fare_per_ride = urban_fare_numbers/urban_ride_numbers
rural_avg_Fare_per_ride = rural_fare_numbers/rural_ride_numbers
suburban_avg_Fare_per_ride = suburban_fare_numbers/suburban_ride_numbers

urban_avg_Fare_per_driver = urban_fare_numbers/urban_driver_numbers
rural_avg_Fare_per_driver = rural_fare_numbers/rural_driver_numbers
suburban_avg_Fare_per_driver = suburban_fare_numbers/suburban_driver_numbers


# %%[markdown]
### create a summary DataFrame

PyBer_summary_df = pd.DataFrame(
            {'Total Rides':[rural_ride_numbers, suburban_ride_numbers, urban_ride_numbers],
            'Total Drivers':[rural_driver_numbers, suburban_driver_numbers, urban_driver_numbers],
            'Total Fares':[rural_fare_numbers, suburban_fare_numbers, urban_fare_numbers],
            'Average Fare per Ride':[rural_avg_Fare_per_ride,suburban_avg_Fare_per_ride, urban_avg_Fare_per_ride],
            'Average Fare per Driver':[rural_avg_Fare_per_driver, suburban_avg_Fare_per_driver, urban_avg_Fare_per_driver]},
            index=['Rural','Suburban','Urban'])
PyBer_summary_df

# %%
