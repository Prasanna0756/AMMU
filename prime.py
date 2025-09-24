def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
                        
def print_primes(n):
    print(f"Prime numbers from 1 to {n}:")
    for num in range(1, n + 1):
        if is_prime(num):
            print(num, end=" ")
n = int(input("Enter a number: "))
print_primes(n)
