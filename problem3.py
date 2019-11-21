# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def get_largest_prime_factors(n):
    prime_factor = 2
    prime_factors = []
    while(n > 1):
        if(n % prime_factor == 0):
            n /= prime_factor 
            prime_factors.append(prime_factor)
        else:
            prime_factor += 1
    if (prime_factors != []):
        return prime_factors[-1]
    else:
        return 1

print(get_largest_prime_factors(600851475143))