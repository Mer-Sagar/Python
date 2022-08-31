'''
3.  Write a program to display employee information like ID on x-
    axis and salary on y-axis in the form of bar graph.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("information.csv")

x= df["eid"]
y=df["salary"]

plt.title("Employee Information")
plt.xlabel("Employee Id")
plt.ylabel("Salray")
plt.bar(x,y)

plt.show()
