f = open("enc", 'r')
flag = f.read()

for i in range(len(flag)):
    #print(ord(flag[i])>>8, chr(ord(flag[i])>>8))
    #print(ord(flag[i]) & 0b11111111, chr(ord(flag[i]) & 0b11111111))
    print(chr(ord(flag[i])>>8), end='')
    print(chr(ord(flag[i]) & 0b11111111), end='')