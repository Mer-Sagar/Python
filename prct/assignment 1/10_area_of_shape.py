'''
Write a program to calculate the area of circle/rectangle/triangle.
    C indicate circle , 
    R indicate rectangle, 
    T indicate triangle. 
use symbolic constant to define the value of pie.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
PI=3.14

print("\n C for Circle")
print("\n R for Ractangle")
print("\n T for Triangle")

ch = input("Which area of Shape you want to find : ")

if(ch == 'C'):
    r = int(input("Enter Radius of Circle : "))
    area = PI * r * r;
    print("Area of Circle : ",area)
    
elif (ch == 'R'):
    w = int(input("Enter Width of rectangle : "))
    h = int(input("Enter Heigth of rectangle : "))
    area = w * h;
    print("Area of Rectangle : ",area)
    
elif(ch == 'T'):
    b = int(input("Enter Base of triangle : "))
    h = int(input("Enter Heigth of triangle : "))
    area = (h * b)/2;
    print("Area of Triangle : ",area)
    
else:
    print("Please, enter valid indicator")

    
   
    
    
    

        
    
    
    





