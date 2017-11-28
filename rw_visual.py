import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    
    keep_running = raw_input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
    elif keep_running =='y':
        continue