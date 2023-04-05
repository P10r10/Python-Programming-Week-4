lst = []
while True:
    word = input("Word: ")
    if word in lst:
        break
    lst.append(word)
print(f"You typed in {len(lst)} different words")
