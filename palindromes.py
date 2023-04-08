def palindromes(s: str):
    return s == s[::-1]


while True:
    usr_str = input("Please type in a palindrome: ")
    if palindromes(usr_str):
        break
    print("that wasn't a palindrome")
print(f"{usr_str} is a palindrome!")
