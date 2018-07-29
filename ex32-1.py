import time
def lcm(a,b):
    list_1 = []
    list_2 = []

    for i in range(2,100):
        list_1.append(i * a)
        list_2.append(i * b)
    #print(list_1, "\n", list_2)

    for i in list_1:
        if i in list_2:
            return "The LCM of {} and {} is {}".format(a,b,i)
t0 = time.perf_counter()
for i in range(5000):
    lcm(40,83)
t1 = time.perf_counter()
total_time = t1 - t0
print (total_time)
#print (lcm(int(input("Enter first integer: ")), int(input("Enter second integer: "))))