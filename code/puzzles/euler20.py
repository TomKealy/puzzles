def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n = n -1
    return fact

def digit_sum(n):
    sum = 0 
    while n:
        sum += n % 10
        n /= 10
    return sum
