s = range(1, 101)
sqsm = 0
smsq = 0
for a in s:
    smsq += a ** 2
for b in s:
    sqsm += b
print(sqsm**2 - smsq)

# Or...
# (a + b + c + ... + z)^2 = a^2 + b^2 + ... + z^2 + 2ab + 2ac + ... + 2az + 2bc + ... + 2xz
# Hence (a + b + c + ... + z)^2 - (a^2 + b^2 + c^2 + ... + z^2) = 2ab + 2ac + ...

diff = 0
for a in range(1, 101):
    for b in range(a + 1, 101):
        diff += 2*a*b
print(diff)
