from pwn import *

r = remote("asgama.web.id",40500)
r.recvline()
i = 1
for i in range(5000):
    data = int(r.recv())
    if data <= 508 and data > 381:
        lol = chr(data - 381) + chr(127) + chr(127) +chr(127)+ chr(1)
    elif data <= 381 and data > 254:
        lol = chr(data - 254) + chr(127) + chr(127) + chr(1)
    elif data <= 254 and data > 127:
        lol = chr(data - 127) + chr(127) + chr(1)
    elif data <= 127:
        lol = chr(data) + chr(1)

    print "{} >>> {} \n>>> {}".format(str(data),lol,str(i))
    i += 1
    r.sendline(lol)

print r.recv()
