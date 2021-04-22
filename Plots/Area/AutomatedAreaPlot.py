from _ctypes_test import func

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Calculating the heights of the pyramid. x=the base for the pyramid.
# The optimal automation levels depends on their relation (unit 100% --> integration 67% | unit 90% --> integration 60%)

data = pd.read_csv('automatedareaplot.csv')
a = []
i = 0
while i < len(data):  # create an array with automation degree data --> a=[90,60,15,...]
    a.append(data.iloc[i, 2])
    i = i + 1

x = len(data) * 2
num_rows = x + 1
x_array = []
matrix = []
i = 0
while i <= x:  # define the x axis --> [0,1,2,3,4,5,6,...]
    x_array.append(i)
    i = i + 1

# calculate the heights into an array of the same size as a, for the pyramid to insert below instead of append(a[w])
heights = []
i = 0
for u in range(len(data) - 1):
    heights.append(a[u] / (x * (len(data) - i) / len(data)))
    u = u + 1
    i = i + 1
heights.append((a[len(data) - 1] * 2) / (
        x * (len(data) - i) / len(data)))  # the last one is shaped like a pyramid --> different area calculation

pyramid_matrix = []  # add zeros and data to create a matrix-->[[0, h1, h1, h1, h1, h1, 0],[0, 0, h2, h2, h2, 0, 0],...]
no_arrays = len(data)  # 3
no_values = num_rows  # 3
i = 0
r = 0
w = 0
for j in range(no_arrays):
    l = []
    i = i + 1
    r = num_rows - i * 2
    for k in range(i):  # until position 1,2,3,... (depending on the loop)
        l.append(0)
    for o in range(r):
        l.append(heights[w])
    for o in range(i):
        l.append(0)
    pyramid_matrix.append(l)
    w = w + 1

data_top = data.head()
level_array = []
for row in data['Testing Level']:
    level_array.append(row)

pyramid_matrix_transposed = [[pyramid_matrix[j][i] for j in range(len(pyramid_matrix))] for i in range(len(pyramid_matrix[0]))]
final_matrix = np.c_[pyramid_matrix_transposed,x_array]
level_array.append("x")
df = pd.DataFrame(final_matrix, columns=level_array)
print(df)
ax = df.plot.area(x='x')
plt.show()