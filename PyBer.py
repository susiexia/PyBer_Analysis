# %%
%matplotlib inline
# %%
import os
import matplotlib.pyplot as plt 
import pandas as pd 
import statistics
import numpy as np 

# %%
city_file_load = os.path.join('Resources', 'city_data.csv')
ride_file_load = os.path.join('Resources','ride_data.csv')

city_data_df = pd.read_csv(city_file_load)
ride_data_df = pd.read_csv(ride_file_load)
ride_data_df.head()
ride_data_df.dtypes
ride_data_df.info()
city_data_df.info()
# %%
arr_city = city_data_df['city'].unique()
city_list = [name for name in arr_city]
city_list
# %%[markdown]
## inspect and clean datasets
#%%
# Get the unique values of the type of city
#unique() & sum
city_data_df['type'].value_counts()
# or
city_data_df['type'].unique()
sum(city_data_df['type'] == 'Urban')

ride_data_df['city'].value_counts()

# %% [markdown]
## Merge DataFrames
# %%
pyber_data_df = pd.merge(ride_data_df,city_data_df,how = 'left',on=['city','city'])
pyber_data_df.head(10)

# %%
# make sure wether the right dataframe info into marge
city_data_df.loc[(city_data_df['city']=='Lake Jonathanshire')]

# %% [markdown]
## BUBBLE PLOTS
# %% [markdown]
### Use filter to create 3 new DF for 3 citty types
urban_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Urban')]
rural_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Rural'),:]
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]

# %%[markdown]
### get x_axis array (the numbers of rides per city per type)
urban_ride_numbers_Series = urban_cities_df.groupby(urban_cities_df['city']).ride_id.count()
rural_ride_numbers_Series = rural_cities_df.groupby(rural_cities_df['city']).ride_id.count()
suburban_ride_numbers_Series = suburban_cities_df.groupby(suburban_cities_df['city']).ride_id.count()

# %% [markdown]
### get y_axis array (the average fare per city per type)
urban_avg_fare_Series = urban_cities_df.groupby(urban_cities_df['city']).fare.agg('mean')
rural_avg_fare_Series = rural_cities_df.groupby(["city"]).mean()["fare"]
suburban_avg_fare_Series =suburban_cities_df.groupby(["city"]).mean()["fare"]

# %% [markdown]
### get markersize array (the average driver per city per type)
urban_avg_driver_Series = urban_cities_df.groupby(urban_cities_df['city']).mean()['driver_count']
rural_avg_driver_Series = rural_cities_df.groupby(rural_cities_df['city']).mean()['driver_count']
suburban_avg_driver_Series = suburban_cities_df.groupby(suburban_cities_df['city']).mean()['driver_count']

# %% [markdown]
