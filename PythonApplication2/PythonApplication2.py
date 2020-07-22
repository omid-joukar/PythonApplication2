
def controlprime(n):
    if n==1:
        return False
    for x in range(2,n):
        if n%x ==0:
            return False
        else:
            return True
def primes(n =1):
    while(True):
        if controlprime(n): yield n
        n+=1
def main():
   for n in primes():
       if n > 100:
           break;
       print(n)
if __name__=="__main__":main()