// This algorithm is my implementation of Euclid's Algorithm to calculate 
// gcd(66528, 52920)
#include <stdio.h>


int gcd(int a, int b) {
    printf("gcd(%i, %i)\n", a, b);
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

void main(char** args, char** kwargs) {
    int a = 66528, b = 52920;
    int gcd = euclids_algorithm(a, b);
    printf("\n\ngcd(%i, %i) = %i", a, b, gcd);
}
