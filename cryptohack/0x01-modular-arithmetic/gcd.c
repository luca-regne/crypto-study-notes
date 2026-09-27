// This algorithm is my implementation of Euclid's Algorithm to calculate 
// gcd(66528, 52920)
// The theorem say
#include <stdio.h>


int gcd(int a, int b) {
    printf("gcd(%i, %i)\n", a, b);
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int main(char** args, char** kwargs) {
    int a = 66528, b = 52920;
    int d = gcd(a, b);
    printf("\n\ngcd(%i, %i) = %i", a, b, d);
    return 0;
}
