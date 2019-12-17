# %%
%matplotlib inline
# %%
import matplotlib.pyplot as plt 

x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

# %%
plt.plot(x_axis, y_axis, linewidth = 3,marker = '*',color = 'red',label='San jose')
plt.xlabel('Date')
plt.xlim('Jan','Dec')
plt.ylim(0,45)
plt.title('PyBer Fare by Month')
plt.legend()
plt.grid()
#plt.show()


# %%
fig, ax = plt.subplots()
ax.plot(x_axis,y_axis, color ='green', marker = 'D', linewidth = 2,label = 'Boston')
ax.plot([20,15,10,30,35,10,15,34,40,10,41,12])
ax.set_title('PyBer Fare by Month')
ax.set_label('hahaha')
ax.set_xlabel('Date')
ax.set_ylabel('Fare($)')
ax.grid()
ax.set_ylim(0,45)
ax.set_facecolor('red')

#ax.get_frame_on()
ax.legend()

#plt.show()

# %%
fig = plt.figure()
ax = fig.add_subplot()
# run now, only a enpty figure 
ax.plot(x_axis,y_axis)

# %%
ax = plt.axes()
ax.plot(x_axis,y_axis)

# %% [markdown]
### BAR CHART___vertical__MATLAB

plt.bar(x_axis,y_axis, color = 'm', align='edge', label = 'Boston')
plt.xlabel('Date')
plt.ylabel('Fare($)')
plt.legend()



# %% [markdown]
### BAR CHART___Horizontal__MATLAB

plt.barh(x_axis,y_axis,color='m',label='Boston')
plt.ylabel('Date')
plt.xlabel('Fare($)')
plt.legend()
plt.title('PyBer Fare by Month')

# ascanding Y axis order
plt.gca().invert_yaxis()

# %% [markdown]
### BAR CHART___Horizontal change parameter___MATLAB

plt.barh(x_axis,[-20,-15,-10,-30,-35,-10,-15,-34,-40,-10,-41,-12],color='black',label='Boston',align='edge')
plt.ylabel('Date')
plt.xlabel('Fare($)')
plt.legend()
plt.title('PyBer Fare by Month')

# ascanding Y axis order
plt.gca().invert_yaxis()



# %% [markdown]
### BAR CHART___vertical__OBJ-oriented
fig, ax = plt.subplots()
ax.bar(x_axis,y_axis,color ='c',label = 'Chicago')



# %%[markdown]
### BAR CHART___horizontal__OBJ-oriented
ax = plt.axes()
ax.barh(x_axis,y_axis,color = 'y')

## ascanding Y axis order
ax.invert_yaxis()


# %%
