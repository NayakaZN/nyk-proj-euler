a, b, fib, even = 1, 1, [], []
while a + b < 4000000:
    fib.append(a + b)
    a, b = b, a + b

for x in fib:
    if x % 2 == 0:
        even.append(x)
print(sum(even))
