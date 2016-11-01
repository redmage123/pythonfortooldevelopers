#include "libmymath.h"
#include <math.h>

/* Compute the greatest common divisor */
int gcd (int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}


/* Compute the fibonacci sequence */
int fib(int n) {
    if (n == 0){ 
        return 0;
    } else if (n == 1) {
        return 1;
    } else  {
        return (fib(n-1) + fib (n-2));
    }
}


/* Divide two numbers */
int divide (int a, int b, float * remainder) {
    int quot = a/b;
    *remainder = fmod(a,b);
    return quot;
}

/* Test if (x0,y0) is in the Mandelbrot set or not */
int in_mandel(double x0, double y0, int n) {
    double x=0, y=0, xtemp;
    while (n> 0) {
        xtemp = x * x - y * y + x0;
        y = 2 * x * y + y0;
        x = xtemp;
        n -=1;
        if (x * x + y * y > 4) {
            return (0);
        }
    }
    return 1;
}

/* Calculate the average value in an array of integers */
double avg(double *a, int n) {
    int i;
    double total = 0.0;
    for (i = 0; i<n; i++) {
        total += a[i];
    }
    return total /n;
}


typedef struct Point {
    double x,y;
} Point;

double distance (Point * p1, Point * p2) {
    return hypot(p1->x - p2 -> x, p1 -> y - p2 -> y);
}

/* Calculate chi squared */
double chi2(double m, double b, double *x, double *y, double *yerr, int N) {

    int n;
    double result = 0.0,diff;
    for (n = 0; n < N; n++) {
        diff = (y[n] - (m * x[n] + b)) / yerr[n];
        result += diff * diff;
    }
    return result;
}



