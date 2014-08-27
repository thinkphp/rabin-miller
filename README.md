# Miller-Rabin Probabilistic Primality Test.

  It's a primality test, an algorithm which determines whether a given number is prime.
 
## Theory
 
 * Fermat's little theorem states that if p is a prime and 1<=a<p then a^p-1 = 1(mod p)

 * If p is a prime x^2 = 1(mod p) or(x-1)(x+1) = 0 (mod p), then x = 1 (mod p) or x = -1 (mod p)

 * If n is an add prime then n-1 is an even number and can be written as 2^s*d. By Fermat's Little Theorem 
    either a^d = 1 (mod n) or a^2^r*d = -1 (mod n) for some 0<=r<=s-1

 * The Rabin-Miller primality test is base on contrapositive of the above claim. That is, if we can find an
    a(witness) such that a^d != 1 (mod n) and a^2^r*d != -1 (mod p) for all 0<=r<=s-1 then a is witness of compositeness
    of n and we can say n is not prime, otherwise n may be prime.  

 * We test our number P for some numbers random a and either declare that p is definitely a composite or probably 
    a prime. 

    The probably that a composite number is returned as prime after k iterations is 1/4^k.
  
     The Running Time: O(k log 3 n)

###  Algorithm
### 
###  Input: A number N to be tested and a variable that determines the accuracy of the test.

###  Output: 0 if N is definitely composite or 1 if N is probably a prime.
###
###  Write N as 2^s*d
###  For each iteration
###        Pick a random witness in [2,N-2]
###        q = witness^d mod N
###        if q == 1 || q == N-1 got to nextIteration
###         for each i=1,s-1
###            q = q^2 mod N
###             if q == 1 return composite
###            if q == N-1 return nextIteration      
###         return composite
###  return probably prime                      