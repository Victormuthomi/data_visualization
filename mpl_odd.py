import matplotlib.pyplot as plt

odd_numbers = [1, 3, 5, 7, 9, 11, 13]

fig, ax = plt.subplots()

#plot the odd numbers and set a line width
ax.plot(odd_numbers, linewidth = 3)

#set the title and the axix labels
ax.set_title("Prime Numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Value of odd number",  fontsize = 14)

#set the tick label size
ax.tick_params(labelsize = 14)

plt.show()
