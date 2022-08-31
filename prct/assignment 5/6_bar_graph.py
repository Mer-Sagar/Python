'''
6.  Write a program to display student information of admission of
    last three using bar graph. You need to take last three year
    information for three programs like MCA, M.Tech and M.Sc.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Student_program.csv")

x1 = df.Program.unique()
print(x1)
y1= df.groupby(['Program'])['Id'].count()

plt.xlabel("Programs or Departments")
plt.ylabel("Year")
plt.bar(x1,y1)

plt.show()
