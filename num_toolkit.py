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