n = int(input("Enter n: "))
even = odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

for i in range(1, 101):
    print(i, end=" ")
print()


for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
print()

for i in range(1, 101):
    if i % 3 == 0:
        if i % 9 == 0:
            continue    # skip these
        print(i, end=" ")
print()

for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0:
        print(i, end=" ")
print()

num = input("Enter an integer: ")
total = 0
for ch in num:
    if ch.isdigit():
        total += int(ch)
print("Sum of digits:", total)