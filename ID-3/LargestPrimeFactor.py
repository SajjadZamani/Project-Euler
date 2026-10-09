def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            return False
    return True

def BigIsPrime(n):
    for i in range(int(n ** 0.5), 1, -1):
        if (n % i == 0):
            if (IsPrime(i)):
                return i
    return 1                           
        
print(BigIsPrime(600851475143))