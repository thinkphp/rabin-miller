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

def modexp(x, y, mod):
 
    sol = 1

    i = 0

    while (1<<i) <= y:

           if (1<<i)&y:

               sol = (sol * x) % mod

           x = (x * x) % mod

           i = i + 1    

    return sol
   
#
# @param n, n > 3, an odd integer to be tested for primality
# @param accuracy, a parameter that determines the accuracy of the test
# @return false, if n is composite, otherwise probably prime
#
def isPrime(n, accuracy):

     # If the number is 2 or 3, then return True  
     if n == 2 or n == 3:
        return True

     # if the number is negative or oven then I have to return False
     if n<=1 or n&1 == 0:
        return False 
     
     # next step we write n-1 as 2^s*d
     s = 0
     m = n - 1

     while m&1 == 0:
          s += 1
          m >>= 1 

     # now we have and s and d as well
     d = (n-1) / (1<<s)
       
     for i in range(1, accuracy + 1):     
 
         # next step we pick a random number between 2 and n-2
         # we call a a witness for compositeness of n, or is called 
         # strong liar when is n is probably prime to a base a. 
         witness = random.randint(2,n-2)
     
         q = modexp(witness, d, n)

         if q == 1 or q == n - 1:
            continue

         for i in range(0, s):

             q = modexp(q, 2, n)

             if q == 1:
                return False

             if q == n-1:
                break

         return False

     # return n is probably prime
     return True  


print isPrime(21, 3)


