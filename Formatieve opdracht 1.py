hoog = int(input("hoe hoog? "))
for a in range(1, hoog + 1):
    print("*" * a)
for b in reversed(range(1, hoog + 1)):
    print("*" * b)
i = 0
while i <= hoog:
    i += 1
    print("*" * i)

