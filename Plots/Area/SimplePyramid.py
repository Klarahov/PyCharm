import matplotlib.pyplot as plt
import pandas as pd

# Here I am defining the heights of the pyramid. x=the base for the pyramid.
# The optimal automation levels depends on their relation (unit 100% --> integration 67%, unit 90% --> integration 60%)

data = pd.read_csv('automatedareaplot.csv')

a1 = data.iloc[0, 2]
a2 = data.iloc[1, 2]
a3 = data.iloc[2, 2]
x = 6

x_array = []
i = 0
# define the x axis
while i <= x:
    x_array.append(i)
    i = i + 1

h_level1 = a1 / x
h_level2 = a2 / (x * 2 / 3)
h_level3 = a3 * 2 / (x * 1 / 3)

h1 = h_level1
h2 = h_level2
h3 = h_level3

df = pd.DataFrame({
    'x': x_array,  # need to match x above
    'Unit': [0, h1, h1, h1, h1, h1, 0],
    'Integration': [0, 0, h2, h2, h2, 0, 0],
    'UI': [0, 0, 0, h3, 0, 0, 0]
})
ax = df.plot.area(x='x')
plt.show()
