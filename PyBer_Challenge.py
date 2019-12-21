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
urban_ride_numbers_Series = urban_cities_df.groupby(urban_cities_df['city']).ride_id.count()
rural_ride_numbers_Series = rural_cities_df.groupby(rural_cities_df['city']).ride_id.count()
suburban_ride_numbers_Series = suburban_cities_df.groupby(suburban_cities_df['city']).ride_id.count()

urban_fare_Series = urban_cities_df.groupby(urban_cities_df['city']).fare.agg('sum')
rural_fare_Series = rural_cities_df.groupby(["city"]).sum()["fare"]
suburban_fare_Series =suburban_cities_df.groupby(["city"]).sum()["fare"]

urban_driver_Series = city_data_df[(city_data_df['type'] == 'Urban')].sum()['driver_count']
rural_driver_Series = city_data_df[(city_data_df['type'] == 'Rural')].sum()['driver_count']
suburban_driver_Series = city_data_df[(city_data_df['type'] == 'Suburban')].sum()['driver_count']

# %%


# %%
