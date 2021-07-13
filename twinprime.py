number = int(input('enter a number and you get all the twin primes below it--'))
n=[3,5, 11,13]

def isprime(num):#will return true if number is prime
    num=int(num)
    st=2

    while(num//2 >= st):
        if(((num/st)-(int(num/st)))==0):#this is true when num/st is an integer which implies num cannot be a prime   
            isp = False
            break
        st+=1
        isp = True #if the above if condition doesn't run that would mean it was a prime
    
    return isp


counter = 15#we'll start from 15

while (number >= counter):
    if(isprime(counter)):
        counter+=2
        if(isprime(counter)):
            second_num = counter
            first_num = second_num-2
            n.append(first_num)
            n.append(second_num)
            counter+=1
            continue
        else:
            counter+=1
            continue
    else:
        counter+=1
        continue

dar= [] 
u = len(n)
c1 = 1
c2 = 2
finl = ''


def nthele(k, arr):
    return arr[k-1]

while c2 < u:
    dn = n[c2] - n[c1]
    dar.append(dn)
    c1+=2
    c2+=2

dar.append(' ')

m1, m2 = 1, 2
d1 = 1
while m2 <= u:
    finl+= str(nthele(m1, n))+' and '+str(nthele(m2, n))+'\n'+str(nthele(d1, dar))+'\n'
    m1+=2
    m2+=2
    d1+=1

print(finl)
print('The sequence-'," ".join(str(ko) for ko in dar))


