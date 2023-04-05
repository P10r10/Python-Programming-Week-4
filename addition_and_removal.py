lst = []
while True:
    print(f"The list is now {lst}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "x":
        break
    if option == "d":
        lst.append(len(lst) + 1)
    elif option == "r":
        lst.pop()
print("Bye!")
