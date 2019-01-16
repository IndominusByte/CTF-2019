from pwn import *
from z3 import *

'''
r = process("./hasssh")
s = Solver()
key = [Int('s{}'.format(x)) for x in range(197)]
[s.add(And(key[i] > 1, key[i] <= 255)) for i in range(197)]

r.recvline()
for i in range(5):
    data = int(r.recvline())
    s.add(ord(key[i]) == data)
    m = s.model()
    r.sendline("1")

flag = []
for n in m:
  char = m[n].as_long()
  flag.append(char)
'''
r = process("./hasssh")
r.recvline()
for i in range(10000):
    for x in range(255):
        v4 = chr(x) + chr(x+1) + chr(0)
    print r.recvline()
    r.sendline(v4)
