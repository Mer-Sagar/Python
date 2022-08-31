'''
Write a program to accept number of days and print year, month and remaining days.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

ndays = int(input("Enter Number of Days : "))

year = int(ndays//365);
	
ndays = int(ndays-365*year);     #return remaining day after year 
		
month = int(ndays//30);           #return month calculate by remain day

day = ndays-(month*30);          #remain day after year - remain month*30

print("\nYear : ",year)
print("Month : ",month)
print("Days : ",day)