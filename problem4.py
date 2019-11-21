import math

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome():
    max_palindrome = 0
    num_one = 999
    while(num_one > 99):
        num_two = 999
        while(num_two > 99):
            num_prod = num_one * num_two
            if(is_palindrome(num_prod) and
            num_prod > max_palindrome):
                max_palindrome = num_prod
            num_two -= 1
        num_one -= 1
    return max_palindrome

def is_palindrome(num):
    num_digits = int(math.log10(num))+1
    digits = []
    while(num_digits > 0):
        digit_pow = pow(10, num_digits-1)
        remainder = num % digit_pow
        num = num // digit_pow
        digits.append(num)
        num = remainder
        num_digits -= 1
    if len(digits) == 1:
        return True
    for i in range(0, len(digits) // 2):
        if digits[i] != digits[-i-1]:
            return False
    return True

print(largest_palindrome())