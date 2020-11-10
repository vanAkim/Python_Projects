import matplotlib.pyplot as plt
import numpy as np

set_name = ['a','b','c']
dico = {'a': {'x': [1,2,3], 'y':[1,2,3]},
        'b': {'x': [1,2,3], 'y':[4,5,6]},
        'c': {'x': [4,5,6], 'y':[4,5,6]}}

for name in set_name:
    plt.plot(dico[name]['x'],
             dico[name]['y'],
             label=name)

plt.legend()
plt.show()