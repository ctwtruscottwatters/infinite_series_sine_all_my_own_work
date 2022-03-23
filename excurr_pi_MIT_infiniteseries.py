# -*- coding: utf-8 -*-
"""
Extra-curricular study to complement my MIT units via edX
10:55 P.M. 23/03/2022 AEST

CHARLES THOMAS WALLACE TRUSCOTT

WOOOOOHOOOOOOOO

I'm sitting a unit from MIT and as part of my extra-curricular study just calculated an approximation to sine by using the Taylor polynomial

ALL MY OWN WORK

Byron Bay NSW 2481

"""
import math
import numpy
def find_sine():
    x = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                x.append(n)
    dummy_val = 45.0 * math.pi / 180
    num = dummy_val
    adding = False
    subtracting = False
    index = 0
    for n in x:
        print('guess: {} index: {} n: {}'.format(num, index, n))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
    num = dummy_val - num
    print('{} is the sine of {} evaluated with a Taylor polynomial, to compare: {} is the computer\'s inbuilt sine for {}'.format(num, dummy_val * 180 / math.pi, numpy.sin(dummy_val), dummy_val * 180 / math.pi))
    print('All my own work. Charles Thomas Wallace Truscott Watters')
    
# ALL MY OWN WORK, CHARLES TRUSCOTT, NUMERICAL INFINITE SERIES FOR SINE

            
#        x = n - (n ** (2 * n + 1))/(math.factorial(2 * n + 1))
#def find_pi():
    
def main():

    find_sine()

if __name__ == "__main__":main()


"""
Next Ramanujan's Infinite Series for Pi
guess: 0.7853981633974483 index: 0 n: 1
guess: 0.0 index: 1 n: 3
guess: 0.08074551218828077 index: 2 n: 5
guess: 0.07825511761808805 index: 3 n: 7
guess: 0.07829169382227023 index: 4 n: 9
guess: 0.07829138046058119 index: 5 n: 11
guess: 0.07829138221782886 index: 6 n: 13
guess: 0.0782913822108804 index: 7 n: 15
guess: 0.07829138221090082 index: 8 n: 17
guess: 0.07829138221090078 index: 9 n: 19
guess: 0.07829138221090078 index: 10 n: 21
guess: 0.07829138221090078 index: 11 n: 23
guess: 0.07829138221090078 index: 12 n: 25
guess: 0.07829138221090078 index: 13 n: 27
guess: 0.07829138221090078 index: 14 n: 29
guess: 0.07829138221090078 index: 15 n: 31
guess: 0.07829138221090078 index: 16 n: 33
guess: 0.07829138221090078 index: 17 n: 35
guess: 0.07829138221090078 index: 18 n: 37
guess: 0.07829138221090078 index: 19 n: 39
guess: 0.07829138221090078 index: 20 n: 41
guess: 0.07829138221090078 index: 21 n: 43
guess: 0.07829138221090078 index: 22 n: 45
guess: 0.07829138221090078 index: 23 n: 47
guess: 0.07829138221090078 index: 24 n: 49
guess: 0.07829138221090078 index: 25 n: 51
guess: 0.07829138221090078 index: 26 n: 53
guess: 0.07829138221090078 index: 27 n: 55
guess: 0.07829138221090078 index: 28 n: 57
guess: 0.07829138221090078 index: 29 n: 59
guess: 0.07829138221090078 index: 30 n: 61
guess: 0.07829138221090078 index: 31 n: 63
guess: 0.07829138221090078 index: 32 n: 65
guess: 0.07829138221090078 index: 33 n: 67
guess: 0.07829138221090078 index: 34 n: 69
guess: 0.07829138221090078 index: 35 n: 71
guess: 0.07829138221090078 index: 36 n: 73
guess: 0.07829138221090078 index: 37 n: 75
guess: 0.07829138221090078 index: 38 n: 77
guess: 0.07829138221090078 index: 39 n: 79
guess: 0.07829138221090078 index: 40 n: 81
guess: 0.07829138221090078 index: 41 n: 83
guess: 0.07829138221090078 index: 42 n: 85
guess: 0.07829138221090078 index: 43 n: 87
guess: 0.07829138221090078 index: 44 n: 89
guess: 0.07829138221090078 index: 45 n: 91
guess: 0.07829138221090078 index: 46 n: 93
guess: 0.07829138221090078 index: 47 n: 95
guess: 0.07829138221090078 index: 48 n: 97
guess: 0.07829138221090078 index: 49 n: 99
0.7071067811865475 is the sine of 45.0 evaluated with a Taylor polynomial, to compare: 0.7071067811865476 is the computer's inbuilt sine for 45.0
All my own work. Charles Thomas Wallace Truscott Watters

"""
