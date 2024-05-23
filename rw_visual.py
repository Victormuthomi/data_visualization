import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk 

while True:
    rw = RandomWalk()
    rw.fill_walk()
    #plot the random work points
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s = 15)
    ax.set_aspect = ('equal')
    plt.show()

    keep_running = input("Make another walk(y/n): ")
    if keep_running == 'n':
        break 


