'''
Admission to a professional course is subject to the following conditions :
(a) marks in mathematics >= 60
(b) marks in physics >= 50
(c) marks in chemistry >= 40
(d) total in all three subjects >= 200
or
total in mathematics and physics >= 150
given the marks in the three subjects , write a program to process
the applications to list an eligible candidate.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

math = int(input("Enter Marks of Mathematics : "))
phy = int(input("Enter Marks of Physics : "))
chem = int(input("Enter Marks of Chemistry : "))

total=math+phy+chem

if (math >= 60) and (phy >= 50) and (chem >= 40):
    if (phy+math>=150)or(total>=200):
        print("Yes candidate is eligible")
    else:
        print("sorry, candidate is not eligible")
else:
    print("sorry, candidate is not eligible")



