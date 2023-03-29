while True:
    s = input("Editor: ").upper()
    if s == "VISUAL STUDIO CODE":
        print("an excellent choice!")
        break
    if s == "EMACS" or s == "VIM" or s == "ATOM":
        print("not good")
    if s == "WORD" or s == "NOTEPAD":
        print("awful")
