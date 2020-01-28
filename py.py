## Sieve of Eratosthenes
 

prime = []

for i in range(2,30):
  
   if i%2 != 0:
     prime.append(i)
     
     
for i in prime:
   for y in range(3,30):
      if i != y and i%y == 0 and i in prime:
         prime.remove(i)
       
print(prime)
