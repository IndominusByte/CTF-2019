import string

p = 6
q = 6

enc = [
0xc7,	0x9a,	0xae,	0xc4,
0x8b,	0xb3,	0xc5,	0xa4,
0xa4,	0xc2,	0xaa,	0x89,
0xc5,	0xba,	0xa3,	0x95,
0xb9,	0xbf,	0xac,	0xb5,
0xbb,	0xac,	0xf7,	0x95,
0xa9,	0xaa,	0x8f,	0xb1,
0x9f,	0xbb,	0x93,	0x93,
0xd7,	0xaa,	0xb1,	0xc6]

k = "JHackHero"
lenk = len(k)

#tmp[i] = 0xff ^ id ^ k[i % lenk] ^ passwd[i];
#tmp 27 + lenk 9 == len enc(36)
#len passwd = 36
#id 1 - 255
tmp = []
passwd = []

for i in range(len(enc)):
    tmp.append(enc[i] - lenk)

for i in range(36):
    passwd.append(0xff ^ ord(k[i % lenk]) ^ tmp[i])

for i in range(255):
    plain = ''.join([chr(x ^ i) for x in passwd])
    if all(y in string.printable for y in plain):
        print plain
