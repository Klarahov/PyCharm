import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bar.csv')
data = df[["Project", "Testing Level", "Automated TC %"]]
y = df["Testing Level"]
xpos = df["Automated TC %"]
xneg = df["Negative"]

plt.barh(y, xpos, height=1, color='b')
plt.barh(y, xneg,height=1, color='b')
plt.title('TC something')
plt.show()