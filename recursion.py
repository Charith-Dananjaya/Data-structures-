def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n

print(sum(2))

def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n

print(factorial(1000))