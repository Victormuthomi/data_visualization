import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x **2 for x in x_values]

plt.style.use('seaborn-v0_8-dark')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,  s=10)

#set the title and axis labels
ax.set_title("Square numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("value of square numbers", fontsize = 14)

#set tick value for the parameters
ax.tick_params(labelsize = 14)

#set the axis range

ax.axis([1, 1100, 1, 1_100_000])
ax.ticklabel_format(style='plain')


plt.show()
