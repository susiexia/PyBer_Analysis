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


# %%[markdown]

# %% 
# Create a summary DataFrame
summary_ride_numbers_ds = pyber_data_df.groupby(pyber_data_df['type']).ride_id.count()
summary_drivers_numbers_ds = city_data_df.groupby(city_data_df['type']).sum()['driver_count']
summary_fares_numbers_ds = pyber_data_df.groupby(pyber_data_df['type']).fare.sum()
summary_avg_Fare_per_ride = summary_fares_numbers_ds/summary_ride_numbers_ds
summary_avg_Fare_per_driver =summary_fares_numbers_ds/summary_drivers_numbers_ds

PyBer_summary_df = pd.DataFrame({'Total Rides':summary_ride_numbers_ds.map('{:,.0f}'.format),
            'Total Drivers':summary_drivers_numbers_ds.map('{:,.0f}'.format),
            'Total Fares':summary_fares_numbers_ds.map('${:,.2f}'.format),
            'Average Fare per Ride':summary_avg_Fare_per_ride.map('${:,.2f}'.format),
            'Average Fare per Driver':summary_avg_Fare_per_driver.map('${:,.2f}'.format)})
PyBer_summary_df.index.name = None
PyBer_summary_df


# %%

newname_pyber_data_df = pyber_data_df.rename(columns = {'city': 'City', 'date':'Date',
                    'fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 
                    'type':'City Type'} )
fare_pyber_data_df = newname_pyber_data_df.set_index('Date').copy().drop(columns = ['Ride Id','City','No. Drivers'])

fare_pyber_data_df



# %%
