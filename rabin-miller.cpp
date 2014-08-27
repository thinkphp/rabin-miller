#include <iostream.h>
#include <conio.h>
#include <stdlib.h>

//
//  Algorithm Rabbin-Miller Probabilistic Primality Test
// 
//  Input: A number N to be tested and a variable that determines the accuracy of the test.
//
//  Output: 0 if N is definitely composite or 1 if N is probably a prime.
//
//  Write N as 2^s*d
//  For each iteration
//         Pick a random witness in [2,N-2]
//         q = witness^d mod N
//         if q == 1 || q == N-1 got to nextIteration
//         for each i=1,s-1
//             q = q^2 mod N
//             if q == 1 return composite
//             if q == N-1 return nextIteration      
//         return composite
//  return probably prime                      

//prototype functions
int pick_random(int a,int b);


//function that determines modular exponentiation
long modexp(long x,int y,int mod) {

     long sol = 1;

     for(int i = 0; (1<<i) <= y; ++i) {

	 if( ((1<<i)&y) > 0 ) {

	     sol = (sol * x) % mod;
	 }

	 x = (x * x ) % mod;
     }

     return sol;
}


int isWitness(int possibleWitness, int exponent, int d, int p) {


    possibleWitness = modexp(possibleWitness, d, p);

    // if the possible witness is congruent with 1 and -1,
    // then go to next iteration and
    // pick up another possible witness for compositeness of n
    if(possibleWitness == 1 || possibleWitness == (p - 1)){

       return 0;
    }

    //possibleWitness = 2^r(0..s)*d
    for(int r = 0; r < exponent; r++) {

	    possibleWitness = modexp(possibleWitness, 2, p);

	    if(possibleWitness == 1) {

	       //return composite
	       return 1;

	    }

	    if(possibleWitness == (p-1)) {

	       //return nextIteration
	       return 0;
	    }

    }


    //return composite
    return 1;
}

//check whether a number > 3 and odd is probably prime or definitely composite.
int isPrime(int n, int accuracy) {

     //if the given number is 2 or 3, then return 1, because is obvious!
     if(n == 2 || n == 3) {

	return 1;
     }

     //if the given number is - or even, then return 0!
     if(n<=1 || !(n&1)) {

	return 0;
     }


     //first steps we must to write n-1 as 2^s*d, so s=? and d=?
     int s = 0,
	 exponent,
	 d;

     int possibleWitness;

     //step 1, compute exponent of two 2^s
     for(int m=n-1;!(m&1);s++,m >>=1);

     exponent = s;

     //step 2, compute d of 2^s*d that have to be odd
     d = (n-1)/(1<<s);


     for(int i = 1; i <= accuracy; i++) {

	 //pick a random number as possible witness for compositeness of n
	 possibleWitness = pick_random(2, n - 2);

	  if(isWitness(possibleWitness, exponent, d, n)) {

	       //return composite
	       return 0;
	  }

     }


     //probably n is prime
     return 1;

}

int pick_random(int a,int b) {

    randomize();

    int c = (rand()%(b-a)) + a;

  return c;
}

void main(){

     //given a number n>3 and odd
     int n;

     clrscr();

     cout<<"\n\n"<<"Miller-Rabin Probabilistic Primality Test"<<"\n\n";

     cout<<"n=";cin>>n;

     if(isPrime(n,3)){

	cout<<"Is, probably, prime!";

     }else{

	cout<<"Is composite, hence not prime!";
     }

     cout<<"\n\n\nPress any key for exit!";
     getch();

}