"""Write a Python program to sum of three given integers.
 However, if two values are equal sum will be zero."""

def sum_3(a,b,c):

    if a != b and a != c and b != c:
        return a + b + c

    else:
        return 0

print (sum_3(3,4,6))
print (sum_3(3,3,9))