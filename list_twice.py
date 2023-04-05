values = []
while True:
    value = int(input("New item: "))
    if value == 0:
        break
    values.append(value)
    print(f"The list now: {values}")
    print(f"The list in order: {sorted(values)}")
print("Bye!")
