'''
2.  Write a program to search a word in to the file. If word is found count number
    of occurrence and print total no of occurrence for that word.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

fp=open("pro_2file.txt","r")

word1 = input("Enter the word to match : ")

count = 0

for i in fp:
    word = i.split(" ")

    for j in word:
        if(j.rstrip("\n")==word1):
            count+=1
print("Total No of time", word1,  "occurred in file : ", count)
    









# f=open("pro_2file.txt","r")  

# word=input("Enter the word to match : ")

# count=0

# for file1 in f:
#     w1=file1.split(" ")                                 # for word

#     for w in w1:        
#         if(w.rstrip("\n")==word): 
#             count+=1 

# print("Total No of time", word,  "occurred in file : ", count)