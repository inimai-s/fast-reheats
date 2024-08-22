# LINE_PLOT.PY
# outputs line plot that provides recommendation for shortening fast reheat time from 300 sec to 28 sec to provide 90% burning

import numpy as np
import matplotlib.pyplot as plt


# output line plot graph
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y,label='100(1 - (1.7x+30)/774.385)')
    plt.xlabel('Reheat Duration (sec)') 
    plt.ylabel('% Time of Burn Window Spent Burning')
    plt.xlim([0,455])
    plt.ylim([0,100])
    plt.grid()
    plt.legend()
    x_pts = [27.905,300]
    y_pts = [my_formula(27.905),my_formula(300)]
    for x,y in zip(x_pts,y_pts):
        l = "{:.2f}".format(y)
        if x == 300:
            label = f'({x}, {l}) - TODAY'
        else:
            label = f'({x}, {l})'
        plt.annotate(label, (x,y), textcoords='offset points',xytext=(0,10),ha='left')
    plt.scatter(x_pts,y_pts,c='r')
    plt.title('% Burning vs Reheat Duration')
    plt.show()  

def my_formula(x):
    return 100*(1-(1.7*x+30)/774.385)

graph(my_formula, range(0,455))
