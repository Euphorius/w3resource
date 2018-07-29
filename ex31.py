
""" Find the GCD (Great common divisor) of two positive integers"""

def GCD(a,b):
    list_1 = set()
    list_2 = set()
    c = b

    if a > b:
        c = a

    for i in range(1,c):

        if a % i == 0:
            list_1.add(i)

        if b % i == 0:
            list_2.add(i)
            
    gcd = max(set.intersection(list_1, list_2))
    
    if gcd == 1:
        return 'There is no common divisor of {} and {} different than 1'.format(a,b)

    else:
        return ("The GCD of {} and {} is {}.".format(a,b, gcd))

print (GCD(34, 86))
print (GCD(21, 74))
print (GCD(14, 44))
print (GCD(12, 30))
print (GCD(336, 360))
