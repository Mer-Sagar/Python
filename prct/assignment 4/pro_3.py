'''
3. Write a program store each word from file and count how many time a particular word is in the file.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

# namedict = dict()

# with open("pro_2file.txt","r") as f:
#     for i in f:
#         words= f.split(" ")

#         for j in words:
#             j=j.rstrip("\n")

#             if j in namedict:
#                 namedict[j]=namedict + 1
                



try:
    namedict = dict()

    with open("pro_2file.txt", "r") as f:
        for fileline in f:
            words = fileline.split(" ")

            for w in words:
                w = w.rstrip("\n")

                if w in namedict:                              
                    namedict[w] = namedict[w] + 1    
                else:
                    namedict[w] = 1 

    for word, count in namedict.items():
            print(word, " : ", count)

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)

