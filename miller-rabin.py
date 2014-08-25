# Miller-Rabin Probabilistic Primality Test.
#
# It's a primality test, an algorithm which determines whether a given number is prime.
# 
# Theory
# 
# 1. Fermat's little theorem states that if p is a prime and 1<=a<p then a^p-1 = 1(mod p)
#
# 2. If p is a prime x^2 = 1(mod p) or(x-1)(x+1) = 0 (mod p), then x = 1 (mod p) or x = -1 (mod p)
#
# 3. If n is an add prime then n-1 is an even number and can be written as 2^s*d. By Fermat's Little Theorem 
#    either a^d = 1 (mod n) or a^2^r*d = -1 (mod n) for some 0<=r<=s-1
#
# 4. The Rabin-Miller primality test is base on contrapositive of the above claim. That is, if we can find an
#    a(witness) such that a^d != 1 (mod n) and a^2^r*d != -1 (mod p) for all 0<=r<=s-1 then a is witness of compositeness
#    of n and we can say n is not prime, otherwise n may be prime.  
#
# 5. We test our number P for some numbers random a and either declare that p is definitely a composite or probably 
#    a prime. 
#
#    The probably that a composite number is returned as prime after k iterations is 1/4^k.
#  
# The Running Time: O(k log 3 n)
#

import random

def decompose(n):

    d = n
    exponentOfTwo = 0 

    while d%2 == 0:
           
          exponentOfTwo += 1 
          d /= 2  
    return exponentOfTwo, d

def modexp(x, y, mod):
 
    sol = 1

    i = 0

    while (1<<i) <= y:

           if (1<<i)&y:

               sol = (sol * x) % mod

           x = (x * x) % mod

           i = i + 1    

    return sol

def isWitness(witness, exponent, d, p):
 
    possibleWitness = modexp(witness, d, p) 
   
    if possibleWitness == 1 or possibleWitness == p - 1:

       return False

    for __ in range(exponent):

       possibleWitness = modexp(possibleWitness, 2, p)

       if possibleWitness == p - 1:

          return False

    return True 


#
# @param n, n > 3, an odd integer to be tested for primality
# @param accuracy, a parameter that determines the accuracy of the test
# @return false, if n is composite, otherwise probably prime
#
def isPrime(p, accuracy):

     # If the number is 2 or 3, then return True  
     if p == 2 or p == 3:
        return True

     # if the number is negative or oven then I have to return False
     if p<=1 or p&1 == 0:
        return False 

     exponent, d = decompose(p-1)
     
     for __ in range(accuracy):

           witness = random.randint(2,p-2) 
    
           if isWitness(witness, exponent, d, p):
              return False

     #probably prime 
     return True        

print isPrime(19, 3)       