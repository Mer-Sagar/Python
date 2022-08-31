'''
5.  Write a program to create a line graph to show the profit of a
    company in various years.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("TCS.csv") 

x= df["Year"]
y=df["Profit"]

plt.title("Tata Consultancy & Services")
plt.xlabel("Years")
plt.ylabel("Profit in Crs.")

plt.plot(x,y)
plt.scatter(x, y)

plt.show()