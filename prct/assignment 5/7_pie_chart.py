'''
7.  Write a program to display a pie chart for number of bank
    accounts opened by five various bank in last five days.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

import matplotlib.pyplot as plt
import pandas as pd

mer = pd.read_csv("Bank.csv")

x=mer["Bank"]
y=mer["Account"]

plt.pie(y, labels = x)
plt.legend()
plt.show()