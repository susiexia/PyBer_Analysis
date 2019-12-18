# %%
%matplotlib inline

import matplotlib.pyplot as plt 

import statistics
import numpy as np 

# %% [markdown]
## errorbar__line use .errorbar()

# %%
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

# %%
fig, (ax1,ax2) = plt.subplots(nrows=2,figsize=(8,8))
stdev = statistics.stdev(y_axis)
ax1.errorbar(x_axis,y_axis, yerr =stdev, 
            capsize=3 , mec = 'g',mfc='red',
            marker ='s',markersize = 20)

ax2.barh(x_axis,y_axis)
ax2.set_xticks(np.arange(51,step =5.0))

# %%
