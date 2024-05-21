import matplotlib.pyplot as plt

squares = [1, 4, 8, 16, 25]

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


