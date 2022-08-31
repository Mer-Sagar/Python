'''
Write a program that accept basic, HRA, and DA from the user and
 calculate total salary.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

 
basic =int(input(" Enter basic salary : "))   
p_hra =float(input(" Enter hra in percentage : "))       
p_da =float(input(" Enter da in percentage : "))       
  
hra = (basic * p_hra)/100  
da  = (basic * p_da)/100  
 
gs  = basic + hra + da  
  
print("Gross Salary = ", gs); 

    
   
    
    
    

        
    
    
    





