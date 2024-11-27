Plain = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
plain_text = input("Enter plain text in capslock: ")
cypher_text = []

for x in plain_text:
    index = Plain.index(x)
    ans = (index + 3) % 26
    cypher_text.append(Plain[ans])

print("Cipher text is:", ''.join(cypher_text))