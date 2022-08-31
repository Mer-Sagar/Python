'''
4.  Write a program to display employee information like ID on x-axis 
    and salary on y-axis in the form of bar graph for two or more departments.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("information.csv")          

specified1 = df.loc[df['dept'] == 'MCA']         
x1 = specified1['eid']
y1 = specified1['salary']

specified2 = df.loc[df['dept'] == 'MBA']
x2 = specified2['eid']
y2 = specified2['salary']

plt.xlabel("Employee Id")
plt.ylabel("Salary")
plt.bar(x1, y1,label = "MCA Department")
plt.bar(x2, y2,label = "MBA Department")

plt.legend()
plt.show()