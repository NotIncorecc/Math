#Might improve the random number generator later

print("Program that calculates pi using random numbers from 1 up to 1million")
print("How?? because the probability that two random numbers are co-prime is 6/(pi)^2") 
import random
import math
itera = 0
does = int(input("How Many times to Iterate--:"))
co_prime = 0
not_co_prime = 0
first_6_pairs = 0

print("The First six pairs are:")

#while loop starts
while (does >= itera):
    itera += 1
    r1b = random.random()
    r1border = random.random()

    if (0 <= r1border < 0.000001):
       r1 = int((r1b*10)//1)
    elif (0.000001 <= r1border < 0.000010):
       r1 = int((r1b*100)//1)
    elif (0.000010 <= r1border < 0.000100):
       r1 = int((r1b*1000)//1)
    elif (0.000100 <= r1border < 0.001000):
       r1 = int((r1b*10000)//1)
    elif (0.001000 <= r1border < 0.010000):
       r1 = int((r1b*100000)//1)
    elif (0.010000 <= r1border < 0.100000):
       r1 = int((r1b*1000000)//1)
    elif (0.100000 <= r1border < 1):
       r1 = int((r1b*10000000)//1)
    else:
       r1 = "nulle"

    r2b = random.random()
    r2border = random.random()

    if (0 <= r2border < 0.000001):
       r2 = int((r2b*10)//1)
    elif (0.000001 <= r2border < 0.000010):
       r2 = int((r2b*100)//1)
    elif (0.000010 <= r2border < 0.000100):
       r2 = int((r2b*1000)//1)
    elif (0.000100 <= r2border < 0.001000):
       r2 = int((r2b*10000)//1)
    elif (0.001000 <= r2border < 0.010000):
       r2 = int((r2b*100000)//1)
    elif (0.010000 <= r2border < 0.100000):
       r2 = int((r2b*1000000)//1)
    elif (0.100000 <= r2border < 1):
       r2 = int((r2b*10000000)//1)
    else:
       r2 = "nulle"
       
    if first_6_pairs <= 6:
        print(r1,"  ",r2)
        first_6_pairs += 1
        
    while (r1 and r2):#check if they are co-prime
       m = r1%r2
       r1,r2 = r2,m
       if r2 != 0:
          continue
       else:
          hcf = int(r1)

    if hcf == 1:
       co_prime += 1
    else:
       not_co_prime += 1 

#while loop ends

tot = co_prime + not_co_prime
sixpi2 = co_prime/tot

PIexp = (6/sixpi2)**(0.5)
PI = math.pi
errorP = ((PI-(PIexp))/PI)*100


print("The Experimental value of Pi is",PIexp)
print("The Error Percentage is about",round(errorP,7),"%")


