number = int(input('enter a number and you get all the twin primes below it--'))

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


counter = 15
twi_primes = '3 and 5\n11 and 13'#we'll check after 15

if(number < 15):
    print('Only twin primes below 15:-\n'+twi_primes)

while (number >= counter):
    if(isprime(counter)):
        counter+=2
        if(isprime(counter)):
            first_num = counter-2
            second_num = first_num +2
            twi_primes+='\n'+str(first_num)+' and '+str(second_num)
        else:
            counter+=1
            continue
    else:
        counter+=1
        continue

if(counter > 15):
    print(twi_primes)

