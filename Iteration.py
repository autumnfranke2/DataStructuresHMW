#Autumn Franke
#Iteration
#1-12-2018

for i in range(2,50):
    isPrime = True
    for j in range(2,int(i+1/2)):
        if i % j == 0:
            isPrime = False
            break

    if  isPrime:
        print(i)
 
