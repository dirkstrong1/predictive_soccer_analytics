import pandas as pd
from math import pi
import matplotlib.pyplot as plt
%matplotlib inline


def createRadar(league, data, league2, data2):

   
    Attributes = ["Win %","Draw %","Goals","GD",]
    
    data += data [:1]
    data2 += data2 [:1]
    angles = [n / 4 * 2 * pi for n in range(4)]
    angles += angles [:1]

    angles2 = [n / 4 * 2 * pi for n in range(4)]
    angles2 += angles [:1]
    
    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1],Attributes)
    ax.plot(angles,values)
    ax.fill(angles, values, 'teal', alpha=0.1)

    ax.plot(angles2,values2)
    ax.fill(angles2, values2, 'red', alpha=0.1)

    a plt.figtext(0.2,0.9,league,color="teal")
    plt.figtext(0.2,0.85,"v")
    plt.figtext(0.2,0.8,league2,color="red")
    plt.show()
   