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
# Rename columns
newname_pyber_data_df = pyber_data_df.rename(columns = {'city': 'City', 'date':'Date',
                    'fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 
                    'type':'City Type'} )
# Set the index to the Date column, make a copy and drop extra columns
DateAsIndex_newname_pyber_data_df = newname_pyber_data_df.set_index('Date')

fare_pyber_data_df = DateAsIndex_newname_pyber_data_df.copy().drop(columns = ['Ride Id','City','No. Drivers'])

#Set the index to the datetime data type
fare_pyber_data_df_new_index = fare_pyber_data_df.index.astype('datetime64[ns]')
fare_pyber_data_df.index = pd.Index(fare_pyber_data_df_new_index)

fare_pyber_data_df.info()
 values= 'Fare'

# %%
# Create a pivot table and get information of total fares by city type
TotalFare_pivot_df = pd.pivot_table(fare_pyber_data_df, index = fare_pyber_data_df.index, values = 'Fare', columns='City Type', aggfunc=np.sum)

# Create a new DataFrame on a given date
April_TotalFare_pivot_df = TotalFare_pivot_df.loc['2019-01-01':'2019-04-28']
April_TotalFare_pivot_df

# Create a new DataFrame by resample fuction in weekly bins
weekly_April_TotalFare_pivot_df = April_TotalFare_pivot_df.resample('W').sum()
weekly_April_TotalFare_pivot_df


# %%
