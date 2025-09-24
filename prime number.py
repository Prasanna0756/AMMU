def prime(num):
   if num < 2:
      return False
   for i in range(2, num):
      if num % i == 0:
            return False
   return True

def primer(limit):
   prime_numbers = []
   count = 0
   sum = 0
   for i in range(1, limit + 1):
      if prime(i):
            prime_numbers.append(i)
            count += 1
            sum += i
   return prime_numbers, count, sum
def twinprime(twin):
    r = []
    for i in range(1, twin + 1):
        if prime(i) and prime(i + 2):  
            r.append((i, i + 2))      
    return r
limit = int(input("Enter the limit: "))
prime_numbers, count, sum = primer(limit)
print(prime_numbers)
print(count)
print(sum)
print(twinprime(100))