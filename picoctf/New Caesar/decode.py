import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def b16_decode(pwd):
    str = ""
    for i in range(0, len(pwd), 2):
        v1 = ord(pwd[i])-LOWERCASE_OFFSET
        v2 = ord(pwd[i+1])-LOWERCASE_OFFSET
        binary = bin((v1 << 4) + v2)
        int_v = int(binary, 2)
        str += chr(int_v)
    return str

pwd = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

for key in ALPHABET:
    s = ''
    for i in range(len(pwd)):
        s += unshift(pwd[i], key[i % len(key)])
    decoded = b16_decode(s)
    print(decoded)
    print()