# PROJECT 8: NUMBER UTILITY TOOLKIT
# Group 8: Rajesh Chaurasiya, Manas Dubey, Sweta Gupta, Pavan Kumar

# Session data
primes = []
history = []


# Check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Check palindrome
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# Check Armstrong
def is_armstrong(n):
    s = str(n)
    total = 0
    for d in s:
        total = total + int(d) ** len(s)
    return total == n

# Check perfect number
def is_perfect(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total == n

# Sum, count and reverse of digits
def digit_ops(n):
    total = 0
    count = 0
    rev = 0
    while n > 0:
        d = n % 10
        total = total + d
        count = count + 1
        rev = rev * 10 + d
        n = n // 10
    return total, count, rev

# Factorial (recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci number (recursion)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# GCD (recursion)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Fibonacci series
def fib_series(terms):
    series = []
    for i in range(terms):
        series.append(fib(i))
    return series

# Prime numbers up to N
def primes_upto(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
            if i not in primes:
                primes.append(i)
    return result
