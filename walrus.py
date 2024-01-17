fruits = ["apple", "kiwi", "banana", "fig", "orange"]

# Option 1
lengths_sup3 = []
for fruit in fruits:
    fruit_length = len(fruit)
    if fruit_length > 3:
        lengths_sup3.append(fruit_length)

print(lengths_sup3)

# Option 2
lengths_sup3 = []
for fruit in fruits:
    if (fruit_length := len(fruit)) > 3:
        lengths_sup3.append(fruit_length)

print(lengths_sup3)

# Option 3
lengths = [fruit_length for s in fruits if (fruit_length := len(s)) > 3]
print(lengths)


# (walrus := True)
# print(walrus)
