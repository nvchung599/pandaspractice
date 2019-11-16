import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('1000 Sales Records.csv')

units_sold = df['Units Sold']
unit_cost = df['Unit Cost']

plt.title('corr')
plt.xlabel('units sold')
plt.ylabel('unit cost')
plt.scatter(units_sold, unit_cost)
plt.show()


