'''
2.  Write a program to display student information like ID on x-
    axis and Age on y-axis in the form of line graph.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

# from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd

mer = pd.read_csv("student.csv")

x=mer["Id"]
y=mer["Age"]

plt.xlabel("Student Id")
plt.ylabel("Age")

plt.scatter(x,y)
plt.plot(x,y)

plt.show()


