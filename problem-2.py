a, b, fib, even = 1, 1, [], []
while a + b < 4000000:
    fib.append(a + b)
    a, b = b, a + b
for x in fib:
    if x % 2 == 0:
        even.append(x)
print(sum(even))

# I improved it a bit...

a, b, c = 1, 1, 0
while (a + b) < 4000000:
    a, b = b, (a + b)
    if b % 2 == 0:
        c += b
print(c)
