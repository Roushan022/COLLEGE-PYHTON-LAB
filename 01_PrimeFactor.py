def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

num = int(input("Enter a number: "))
if num < 2:
    print("Please enter a number greater than 1.")
else:
    result = prime_factors(num)
    print(f"Prime factors of {num} are: {result}")
