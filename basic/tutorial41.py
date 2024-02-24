'''
ในไฟล์นี้เราจะมาเรียนรู้การทำ Data Visualization ด้วย Seaborn ซึ่งเป็น Library ที่ใช้สำหรับการทำ Data Visualization ที่สามารถทำได้ง่ายและสวยงาม
'''

import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("insurance.csv")
print(df.head())

# Data visualization
sb.relplot(x="charges", y="region", data=df) # Scatterplot
plt.show()

sb.relplot(x="charges", y="region", hue="age", data=df) # Scatterplot with hue
plt.show()

charges = df['charges'].values # Select only col=='charges' and converts to numpy
sb.displot(charges, color='r') # Distribution plot
plt.title("Distribution of charges")
plt.show()


sb.countplot(x='sex', data=df) # Count plot
plt.title("Count of Gender")
plt.show()

'''
Numerical features against numerical features
'''
sb.scatterplot(x='age', y='charges', data=df) # Scatterplot
plt.title("Scatterplot of age vs. charges")
plt.show()


sb.scatterplot(x='age', y='charges', hue='smoker', data=df) # Scatterplot with hue
plt.title("Scatterplot of age vs. charges")
plt.show()


sb.jointplot(x='age', y='charges', data=df) # Joint plot
plt.show()


sb.jointplot(x='age', y='charges', data=df, kind='hex', color='r') # Joint plot with hex kind
plt.show()


sb.barplot(x='sex', y='charges', data=df, hue='smoker') # Bar plot with hue
plt.show()

sb.pairplot(df, hue='sex', diag_kind='hist') # Pair plot with hue
plt.show()


'''
Numerical features against categorical features
'''
sb.boxplot(x='sex', y='age',  data=df) # Box plot
plt.show()

sb.boxplot(x='sex', y='children', data=df, hue='smoker') # Box plot with hue
plt.show()

sb.violinplot(x='sex', y='children', data=df) # Violin plot
plt.show()

sb.violinplot(x='age', y='sex', data=df) # Violin plot
plt.show()

sb.stripplot(x='sex', y='charges', data=df, hue='smoker') # Strip plot
plt.show()

sb.swarmplot(x='sex', y='charges', data=df, hue='smoker') # Swarm plot
plt.show()