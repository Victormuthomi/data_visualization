import matplotlib.pyplot as plt

input_values =[1, 4, 8, 15,25]
squares = [1, 4, 8, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()
# Increase the line width
ax.plot(squares)


#set the title and label for  the y and x axis
ax.set_title("Squares", fontsize =14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

#set the size of tick labesls

ax.tick_params(labelsize = 14)

plt.show()


