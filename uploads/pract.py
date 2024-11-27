#ceaser cipher
Plain = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
plain_text = input("Enter plain text in capslock: ")
cypher_text = []

for x in plain_text:
    index = Plain.index(x)
    ans = (index + 3) % 26
    cypher_text.append(Plain[ans])

print("Cipher text is:", ''.join(cypher_text))
"""------------------------------------------------------------------------------"""
# monoalphabetic cipher
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
"""------------------------------------------------------------------------------"""
#polyalphabetic substitution cipher
def poly_cipher(text, key, encrypt=True):
    key = key.upper()
    text = text.upper()
    key_length = len(key)
    result = []

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if not encrypt:
                shift = -shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

# User inputs
plain_text = input("Enter Text: ")
key = input("Key: ")

# Encryption and Decryption
encrypted = poly_cipher(plain_text, key, encrypt=True)
decrypted = poly_cipher(encrypted, key, encrypt=False)

# Output results
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
"""------------------------------------------------------------------------------"""
#Vernam Cipher
import string

# Function to encrypt using Vigenère cipher
def vigenere_encrypt(plain_text, key):
    alphabets = list(string.ascii_letters)
    cypher_text = []
    i = 0

    for x in plain_text:
        if x in alphabets:
            index = alphabets.index(x)
            key_index = alphabets.index(key[i % len(key)])
            ans = (index + key_index) % len(alphabets)
            cypher_text.append(alphabets[ans])
            i += 1
        else:
            cypher_text.append(x)

    return "".join(cypher_text)

# Function to decrypt using Vigenère cipher
def vigenere_decrypt(cypher_text, key):
    alphabets = list(string.ascii_letters)
    plain_text = []
    i = 0

    for x in cypher_text:
        if x in alphabets:
            index = alphabets.index(x)
            key_index = alphabets.index(key[i % len(key)])
            ans = (index - key_index) % len(alphabets)
            plain_text.append(alphabets[ans])
            i += 1
        else:
            plain_text.append(x)

    return "".join(plain_text)

# User inputs
plain_text = input("Enter Plain Text: ")
key = input("Enter Key: ")

# Encryption
encrypted_text = vigenere_encrypt(plain_text, key)
print("The Cypher text is:", encrypted_text)

# Decryption
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("The Decrypted text is:", decrypted_text)
"""------------------------------------------------------------------------------"""
#PlayFair
import string

def create_playfair_matrix(key):
    # Filter and prepare the key
    key = ''.join(filter(str.isalpha, key)).upper().replace('J', 'I')
    key = ''.join(sorted(set(key), key=key.index))

    matrix = list(key)
    for char in range(ord('A'), ord('Z') + 1):
        char = chr(char)
        if char not in key and char != 'J':
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = ''.join(filter(str.isalpha, text.upper().replace('J', 'I')))
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            pairs.append(text[i] + text[i + 1])
            i += 2
        else:
            pairs.append(text[i] + 'X')
            i += 1
    return pairs

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def playfair_encrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    if c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_decrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    if c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_cipher(text, key, encrypt=True):
    matrix = create_playfair_matrix(key)
    pairs = preprocess_text(text)
    process_pair = playfair_encrypt_pair if encrypt else playfair_decrypt_pair
    return ''.join(process_pair(pair, matrix) for pair in pairs)

def main():
    key = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")

    encrypted = playfair_cipher(plaintext, key, encrypt=True)
    decrypted = playfair_cipher(encrypted, key, encrypt=False)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
"""------------------------------------------------------------------------------"""
#Rail Fence
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
"""------------------------------------------------------------------------------"""
#columnar transposition
def columnar_transposition_encrypt(text, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = -(-len(text) // num_cols)  # Ceiling division
    padded_text = text.ljust(num_cols * num_rows)
    grid = [padded_text[i:i + num_cols] for i in range(0, len(padded_text), num_cols)]

    key_order = sorted(range(len(key)), key=lambda x: key[x])
    ciphertext = ''.join(''.join(grid[row][col] for row in range(num_rows)) for col in key_order)

    return ciphertext

def columnar_transposition_decrypt(ciphertext, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)  # Ceiling division
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    key_order = sorted(range(len(key)), key=lambda x: key[x])
    index = 0

    for col in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                grid[row][col] = ciphertext[index]
                index += 1

    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext.rstrip()

def main():
    text = input("Enter the plaintext: ").replace(" ", "").strip()
    key = input("Enter the key: ").strip()

    encrypted_text = columnar_transposition_encrypt(text, key)
    decrypted_text = columnar_transposition_decrypt(encrypted_text, key)

    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
"""------------------------------------------------------------------------------"""
#RSA
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi

# Example values for p, q, and e
p = 13
q = 17
e = 35

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    raise ValueError("Public key e is not coprime with φ(n)")

d = mod_inverse(e, phi)

print("Public Key (n, e):", (n, e))
print("Private Key (d):", d)
"""------------------------------------------------------------------------------"""
#Practical 8 windows firewall to block a port.
'''
Steps to Block a Port in Windows Firewall:
1.	Open Advanced Settings:
o	Press Win + R, type wf.msc, and press Enter.
2.	Choose Rule Type:
o	Go to Inbound Rules (or Outbound Rules) on the left panel.
o	Click New Rule in the right panel.
3.	Set Port Rule:
o	Select Port > Click Next.
4.	Specify Port:
o	Choose TCP or UDP and enter the port number to block.
o	Click Next.
5.	Block the Connection:
o	Select Block the connection > Click Next.
6.	Apply to Profiles:
o	Choose the profiles where this rule applies (Domain, Private, Public).
o	Click Next.
7.	Name the Rule:
o	Give the rule a name (e.g., "Block Port 80") > Click Finish.
The port is now blocked!
'''
"""------------------------------------------------------------------------------"""
#Practical 8 windows firewall to block a port.
'''
1. Open Windows Firewall
Press  Win + R  to open the Run dialog box.
Type  wf.msc  and press Enter to open the Windows Defender Firewall
with Advanced Security window.
2. Navigate to Outbound or Inbound Rules
Decide if you want to block incoming or outgoing connections:
Inbound Rules: To block incoming traffic on the port.
Outbound Rules: To block outgoing traffic on the port.
Click on Outbound Rules (or Inbound Rules) from the left pane.
3. Create a New Rule
In the Actions pane on the right, click New Rule... to launch the New
Outbound Rule Wizard.
4. Select Rule Type
In the wizard:
Choose Port as the rule type.
Click Next.
5. Specify Protocol and Port
Select the protocol (TCP or UDP) for the port you want to block.
Choose Specific remote ports and type the port number(s) you wish to
block (e.g.,  443  for HTTPS).
Click Next.
6. Set Action
Select Block the connection to deny traffic for the specified port.
Click Next.
Firewall - Steps 2
7. Apply to Network Profiles
Choose the network profiles where this rule will apply:
Domain: For devices in a corporate network.
Private: For trusted networks like home or work.
Public: For public networks.
Click Next.
8. Name the Rule
Provide a name for the rule (e.g., "Block Port 443").
Optionally, add a description.
Click Finish.

"""------------------------------------------------------------------------------"""


Configure Router with password
Step 1: Configure password for vty lines
Execute Command on all routers
R(config) # line vty 0 4
R(config-line) #password vtypa55
R(config-line) #login
Step 2: Configure secret on router
Execute Command on all routers
R(config) # enable secret enpa55
Step 3: Configure OSPF on routers
R1(config) #router ospf 1
R1(config-router) #network 192.168.1.0 0.0.0.255 area 0
R1(config-router) #network 10.1.1.0 0.0.0.3 area 0
R2(config) #router ospf 1
R2(config-router) #network 10.1.1.0 0.0.0.3 area 0
R2(config-router) #network 10.2.2.0 0.0.0.3 area 0
R3(config) #router ospf 1
R3(config-router) #network 192.168.3.0 0.0.0.255 area 0
R3(config-router) #network 10.2.2.0 0.0.0.3 area 0
Step 4: Test Connectivity
PC-A > ping 192.168.3.5
Successful
PC-B > ping 192.168.3.5
Successful


Practical 9: OSPF MD5 Authentication and NTP Configuration

Steps to Perform Practical 1
1. OSPF MD5 Authentication
   - Ensure basic OSPF configurations are already applied on the routers as described in the initial steps.
   - Enable OSPF MD5 authentication in Area 0 for R1, R2, and R3:
     bash
     R1(config)# router ospf 1
     R1(config-router)# area 0 authentication message-digest

     R2(config)# router ospf 1
     R2(config-router)# area 0 authentication message-digest

     R3(config)# router ospf 1
     R3(config-router)# area 0 authentication message-digest

   - Configure MD5 keys on the required interfaces:
     bash
     R1(config)# interface s0/1/0
     R1(config-if)# ip ospf message-digest-key 1 md5 MD5pa55

     R2(config)# interface s0/1/0
     R2(config-if)# ip ospf message-digest-key 1 md5 MD5pa55
     R2(config)# interface s0/1/1
     R2(config-if)# ip ospf message-digest-key 1 md5 MD5pa55

     R3(config)# interface s0/1/0
     R3(config-if)# ip ospf message-digest-key 1 md5 MD5pa55


   - Verification
     - Use the command `show ip ospf interface` to confirm:
       ```bash
       R1# show ip ospf interface

       Output should show: Message-digest Authentication Enabled, and Key ID 1.

   - Verify end-to-end connectivity with the `ping` command.

---

2. NTP Configuration
   - Enable NTP service and authentication on PC-A:
     - Go to PC-A, open the Services tab > NTP.
     - Enable NTP authentication using key 1 and password NTPpa55.

   - Configure R1, R2, and R3 as NTP clients:
     bash
     R1(config)# ntp server 192.168.1.5
     R2(config)# ntp server 192.168.1.5
     R3(config)# ntp server 192.168.1.5


   - Configure routers to update the hardware clock:
     bash
     R1(config)# ntp update-calendar
     R2(config)# ntp update-calendar
     R3(config)# ntp update-calendar


   - Enable NTP authentication on the routers:
     bash
     R1(config)# ntp authenticate
     R1(config)# ntp trusted-key 1
     R1(config)# ntp authentication-key 1 md5 NTPpa55


   - Repeat the above for R2 and R3

   - Verification
     - Check the NTP status:
       bash
       R1# show ntp status

     - Check the hardware clock update:
       bash
       R1# show clock


---

## Practical 10: Logging to Syslog Server and SSH Configuration

### Steps to Perform Practical 2
1. **Syslog Server Logging**
   - Configure routers to send logs to the Syslog server:
     bash
     R1(config)# logging host 192.168.1.6
     R2(config)# logging host 192.168.1.6
     R3(config)# logging host 192.168.1.6


   -Verification
     - Check the logging status on each router:
       bash
       R1# show logging

     - Open the Syslog server and check logs under the **Syslog service tab**.

---

2. SSH Configuration for R3
   - Configure a domain name on R3:
     bash
     R3(config)# ip domain-name ccnasecurity.com


   - Create a user with privilege level 15:
     bash
     R3(config)# username SSHadmin privilege 15 secret sshpa55


   - Configure vty lines to accept only SSH:
     bash
     R3(config)# line vty 0 4
     R3(config-line)# login local
     R3(config-line)# transport input ssh


   - Generate an RSA key pair:
     bash
     R3(config)# crypto key generate rsa

     - Use a modulus of 1024.

   - Adjust SSH settings:
     bash
     R3(config)# ip ssh time-out 90
     R3(config)# ip ssh authentication-retries 2
     R3(config)# ip ssh version 2


   - **Verification**
     - Check SSH settings:
       bash
       R3# show ip ssh


   - Attempt SSH connection from PC-C or R2:
     bash
     PC> ssh -l SSHadmin 192.168.3.1


'''

"""------------------------------------------------------------------------------"""
#Practical 9
"""
Steps:
Part 1 configure OSPF MD5 Authentication
Step 1: Test connectivity. All devices should be able to ping all other IP addresses.
Step 2: Configure OSPF MD5 authentication for all the routers in area 0. Configure OSPF MD5 authentication for all the routers in area 0.
Step 3: Configure the MD5 key for all the routers in area 0. Configure an MD5 key on the serial interfaces on R1, R2 and R3. Use the password MD5pa55 for key 1.
Step 4: Verify configurations.

Part 2: Configure NTP
Step 1: Enable NTP authentication on PC-A.
Step 2: Configure R1, R2, and R3 as NTP clients.
Step 3: Configure routers to update hardware clock.
Step 4: Configure NTP authentication on the routers.
Step 5: Configure routers to timestamp log messages"""

"""------------------------------------------------------------------------------"""
#Practical 10
"""
steps:
Part 3: Configure Routers to Log Messages to the Syslog Server
Step 1: Configure the routers to identify the remote host (Syslog Server) that will receive logging messages.
Step 2: Verify logging configuration.
Step 3: Examine logs of the Syslog Server.

Part 4: Configure R3 to Support SSH Connections
Step 1: Configure a domain name. Configure a domain name of ccnasecurity.com on R3.
Step 2: Configure users for login to the SSH server on R3.
Step 3: Configure the incoming vty lines on R3.
Step 4: Erase existing key pairs on R3.
Step 5: Generate the RSA encryption key pair for R3.
Step 6: Verify the SSH configuration.
Step 7: Configure SSH timeouts and authentication parameters.
Step 8: Attempt to connect to R3 via Telnet from PC-C.
Step 9: Connect to R3 using SSH on PC-C.
Step 10: Connect to R3 using SSH on R2.
Step 11: Check results."""

'''
-----------------------------------------------------------------------
RIP
Router 1
Continue with configuration dialog? [yes/no]: no


Press RETURN to get started!



Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#host R1
R1(config)#int g0/1
R1(config-if)#ip add 192.168.1.1 255.255.255.0
R1(config-if)#no shut

R1(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

R1(config-if)#exit
R1(config)#int s0/0/0
R1(config-if)#ip add 10.1.1.1 255.255.255.252
R1(config-if)#no shut
--------------------------------------------------------------
R1>en
R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router rip
R1(config-router)#network 192.168.1.0
R1(config-router)#network 10.1.1.0
############################################################################################
Router 2
Continue with configuration dialog? [yes/no]: no


Press RETURN to get started!



Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#host R2
R2(config)#int s0/0/0 
R2(config-if)#ip add 10.1.1.2 255.255.255.252
R2(config-if)#no shut

R2(config-if)#
%LINK-5-CHANGED: Interface Serial0/0/0, changed state to up

R2(config-if)#exi
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial0/0/0, changed state to up
t
R2(config)#int s0/0/1
R2(config-if)#ip add 10.2.2.2 255.255.255.252
R2(config-if)#no shut

%LINK-5-CHANGED: Interface Serial0/0/1, changed state to down
-----------------------------------------------------------------

R2(config-if)#exit
R2(config)#router rip
R2(config-router)#network 10.1.1.0
R2(config-router)#network 10.2.2.0
R2(config-router)#^Z
#################################################################################
Router3
Continue with configuration dialog? [yes/no]: no


Press RETURN to get started!



Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#host R3
R3(config)#int g0/1
R3(config-if)#ip add 192.168.3.1 255.255.255.0
R3(config-if)#no shut

R3(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

R3(config-if)#exit
R3(config)#int s0/0/1
R3(config-if)#ip add 10.2.2.1 255.255.255.252
R3(config-if)#no shut
--------------------------------------------

R3(config-if)#exit
R3(config)#router rip
R3(config-router)#network 192.168.3.0
R3(config-router)#network 10.2.2.0
R3(config-router)#^Z
----------------------------------------
show ip route
-------------------------------------
show ip route
'''
