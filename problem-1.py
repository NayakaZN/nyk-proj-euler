summa = 0
for i in (1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        summa += i
print(summa)

# I think I understood list comprehension more! Here's my improvement:

print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))
