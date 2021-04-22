import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots()

data = pd.read_csv('line.csv')

# Plot
sns.set_color_codes("pastel")
sns.lineplot(x="Automated TC %", y="Testing Level", linewidth =4, data=data, color="b")
# sns.barplot(x="Automated TC %", y="Testing Level", data=data, color="b")


# Add an informative axis label
ax.set(xlim=(-100, 100), xticklabels=[], ylabel="",
       xlabel="Automated test cases (%)")
sns.despine(left=True, bottom=True)

plt.show()
