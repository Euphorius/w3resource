import time
def lcm(x, y):

   if x > y:

       z = x

   else:

       z = y


   while(True):

       if((z % x == 0) and (z % y == 0)):

           lcm = z
           break
       z += 1

   return lcm
t0 = time.perf_counter()
for i in range(5000):
    lcm(40,83)
t1 = time.perf_counter()
total_time = t1 - t0
print (total_time)