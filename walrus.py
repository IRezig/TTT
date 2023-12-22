# Option 1
fruits = ["apple", "kiwi", "banana", "fig", "orange"]
lengths = []
for s in fruits:
    length = len(s)
    if length > 3:
        lengths.append(length)

print(lengths)

# Option 2
lengths = []
for fruit in fruits:
    if (length := len(fruit)) > 3:
        lengths.append(length)

print(lengths)

# Option 3
lengths = [length for s in fruits if (length := len(s)) > 3]
print(lengths)
