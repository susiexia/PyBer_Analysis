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
### create each scatter plot individually and add them all to one chart
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
### 3 individual scatter plot by MATLAB method then one bubble chart for 3 all cities
### put Series into x-axis and y-axis in scatter() parenthesis, no x=, y=(this is for line)
plt.figure(figsize=(12,7))

plt.scatter(urban_ride_numbers_Series, urban_avg_fare_Series, 
            s=10*urban_avg_driver_Series, c='coral', label ='Urban',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.scatter(rural_ride_numbers_Series, rural_avg_fare_Series, 
            s=10*rural_avg_driver_Series, c='gold', label ='Rural',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.scatter(suburban_ride_numbers_Series, suburban_avg_fare_Series, 
            s=10*suburban_avg_driver_Series, c='skyblue', label ='Suburban',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.xlabel('Total Number of Rides (Per City)', fontsize = 12)
plt.ylabel('Average Fare ($)', fontsize = 12)
plt.title('PyBer Ride-Sharing Data (2019)',fontsize =20)
plt.grid()

plt.text(41,35,'Note:\nCircle size\ncorrelates with\ndriver count per city.', fontsize = '8')
# manual legend's handles size, use attribute: legend.legendHandles[].set_sizes
lgnd = plt.legend(fontsize = '12', loc = 'upper right',scatterpoints=1, 
                   bbox_to_anchor=(1,1), title = 'City Types')
lgnd.get_title().set_fontsize(12)

# -------------------------important ---------------------------------
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]

# save fig first then show() it
plt.savefig('analysis/Fig1.png')

plt.show()

# %% [markdown]
### get statistics infor to show the relevance of data
# use Numpy mean(), median() and SciPy mode()

round(urban_ride_numbers_Series.mean(), 2) 
#print(f'The mode for ride counts for urban trips is {mode_suburban_ride_numbers_Series}')
#print(f"The mean fare price for urban trips is ${mean_urban_fares:.2f}.")
# %% [markdown]
### stats information for ride numbers per city type (without groupby city names)
mean_urban_ride_count = urban_ride_numbers_Series.describe()['mean']
mean_rural_ride_count = rural_ride_numbers_Series.describe()['mean']
mean_suburban_ride_count = suburban_ride_numbers_Series.describe()['mean']

median_urban_ride_count = urban_ride_numbers_Series.describe()['50%']
median_rural_ride_count = rural_ride_numbers_Series.describe()['50%']
median_suburban_ride_count = suburban_ride_numbers_Series.describe()['50%']

mode_urban_ride_count = sts.mode(urban_ride_numbers_Series)
mode_rural_ride_count = sts.mode(rural_ride_numbers_Series)
mode_suburban_ride_count = sts.mode(suburban_ride_numbers_Series)
mode_suburban_ride_count
# %% [markdown]
### stats information for fares per city type (without groupby city names)
#### get orginal dataset 
urban_fares = urban_cities_df['fare'] 
rural_fares = rural_cities_df['fare'] 
suburban_fares = suburban_cities_df['fare'] 

mean_urban_fares = urban_fares.describe()['mean']
mean_rural_fares = rural_fares.describe()['mean']
mean_suburban_fares = suburban_fares.describe()['mean']

median_urban_fares = urban_fares.describe()['50%']
median_rural_fares = rural_fares.describe()['50%']
median_suburban_fares = suburban_fares.describe()['50%']

mode_urban_fares = sts.mode(urban_fares)
mode_rural_fares = sts.mode(rural_fares)
mode_suburban_fares = sts.mode(suburban_fares)
mode_urban_fares
# %%[markdown]
### stats information for driver numbers per city type (without groupby city names)
### which cities need more driver support

urban_drivers = urban_cities_df['driver_count']
rural_drivers = rural_cities_df['driver_count']
suburban_drivers = suburban_cities_df['driver_count']

mean_urban_drivers = urban_drivers.describe()['mean']
mean_rural_drivers = rural_drivers.describe()['mean']
mean_suburban_drivers = suburban_drivers.describe()['mean']
print(f"The mean fare price for urban trips is ${mean_urban_drivers:.2f}.")
print(f"The mean fare price for rural trips is ${mean_rural_drivers:.2f}.")
print(f"The mean fare price for suburban trips is ${mean_suburban_drivers:.2f}.")

median_urban_drivers = urban_drivers.describe()['50%']
median_rural_drivers = rural_drivers.describe()['50%']
median_suburban_driverss = suburban_drivers.describe()['50%']

mode_urban_drivers = sts.mode(urban_drivers)
mode_rural_drivers = sts.mode(rural_drivers)
mode_suburban_drivers = sts.mode(suburban_drivers)


# %%
## TEST-------------------------------------------------------------------------
test_urban_driver = city_data_df.loc[(city_data_df['type']=='Urban'),:]
mean_test_urban = test_urban_driver['driver_count'].mean()
mean_test_urban

test_rural_driver = city_data_df.loc[(city_data_df['type']=='Rural'),:]
mean_test_rural = test_rural_driver['driver_count'].mean()
print(mean_test_rural)

test_suburban_driver = city_data_df.loc[(city_data_df['type']=='Suburban'),:]
mean_test_suburban = test_suburban_driver['driver_count'].mean()
mean_test_suburban
# TEST-----------------------------------------------------------------------------

# %%[markdown]
## BOX_and_Whisker Plot

fig, ax = plt.subplots()
ax.boxplot(urban_ride_numbers_Series,labels = ['Urban'],showmeans = True, showfliers = True)
ax.set_ylabel('Number of Rides')
ax.set_title('Ride Count Data (2019)')
ax.set_yticks(np.arange(0,41,step=2.0))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.grid()




# %%
