plain_text = input("Enter plain text: ")
odd = []
even = []

for i in range(len(plain_text)):
    if i % 2 == 0:
        even.append(plain_text[i])
    else:
        odd.append(plain_text[i])

print("The output is:")
print("Even indexed characters:", ''.join(even))
print("Odd indexed characters:", ''.join(odd))