# Import Data
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

df = pd.read_csv('violin.csv')

# Draw Plot
plt.figure(figsize=(13, 10), dpi=80)
sns.violinplot(x='Automated TC %', y='Testing Level', data=df, scale='width', inner='quartile')

# Decoration
plt.title('Violin Plot of Automated Testcases', fontsize=22)
plt.show()
