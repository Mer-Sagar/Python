'''
1.  Write a program to display student information like ID on x-
    axis and percentage on y-axis in the form of bar graph.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student.csv")
x = df["Id"]                     
y= df["Percentage"]

plt.bar(x, y)

plt.title("Student Percentage graph")
plt.xlabel("Student Id")
plt.ylabel("Percentage")         

plt.show()
