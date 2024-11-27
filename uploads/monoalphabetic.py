a = {
    "a": "C", "b": "E", "c": "A", "d": "T", "e": "R", "f": "B", "g": "D",
    "h": "N", "i": "F", "j": "U", "k": "X", "l": "D", "m": "Q", "n": "G",
    "o": "Y", "p": "L", "q": "K", "r": "H", "s": "V", "t": "I", "u": "J",
    "v": "M", "w": "P", "x": "Z", "y": "S", "z": "W"
}

q = input("Enter plain text in lowercase: ")
r = []
res = ""

for i in q:
    c = a.get(i)
    if c:  # Check if the character exists in the dictionary
        r.append(c)

# Join the list into a string and print the result
print("Plain text:", q)
print("Cipher text:", ''.join(r))