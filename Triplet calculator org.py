print("A program that calculates co-prime pythagorean triplets")
a1 = 3
tfound = 0
nos = int(input("Number of tripets to calculate---"))


while tfound < nos:
    a2 = ((a1**2)-1)/2
    a3 = ((a1**2)+(a2**2))**(0.5)
    if (a3 == a3//1):#to check if a3 is an integer
        print(a1," ",int(a2)," ",int(a3))
        tfound += 1
        a1 += 2
    else:
        continue
    
