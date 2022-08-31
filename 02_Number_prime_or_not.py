# Natural Number = 1
# Which has only 2 factors 1 and itself only

# 19 ==> 1 and 19 --> prime
# 12 ==> 1,3,4,6,12 --> not prime

num = 5
falg=0

if num>1:
    for i in range(1,num+1):
        if (num/i) == 0:
            falg=100
    if falg == 100:
        print("\n\nNumber is prime ")
    else:
        print("\n\nNumber is not prime")

