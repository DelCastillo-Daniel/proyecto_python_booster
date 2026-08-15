def fibonacci(n1 = 0, n2 = 1):
    n3 = 0
    while n3 < 100:
        print(n3)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3

fibonacci()