kata = "abc2dja"
for char in kata:
    if kata in "0123456789":
        print(True)
    else:
        print(False)
    if "0123456789" in kata:
        print(True)
    else:
        print(False)