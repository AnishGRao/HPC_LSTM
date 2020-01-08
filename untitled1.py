import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("test.csv")
df.plot()  # plots all columns against index
df.plot(kind='scatter',x='Time',y='Failures') # scatter plot
df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram