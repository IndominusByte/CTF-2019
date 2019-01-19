# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Nov 12 2018, 14:36:49) 
# [GCC 5.4.0 20160609]
# Embedded file name: sanca.py
# Compiled at: 2019-01-12 02:35:09
'''
data = raw_input('Flag:')
data = data[14:] + data[:14]
if len(data) != 28:
    print 'Incorrect!'
    exit()
if data[-2] != 'n':
    print 'Incorrect!'
    exit()
if data[10] != '3':
    print 'Incorrect!'
    exit()
if data[::-2] != '_otp5ar}3l3333':
    print 'Incorrect!'
    exit()
if data[::-3] != '_hpvrtls3r':
    print 'Incorrect!'
    exit()
if data[::-5] != '_yat3v':
    print 'Incorrect!'
    exit()
if data[::-7] != '_{}s':
    print 'Incorrect!'
    exit()
if data[::4] != 'rr_tk{h':
    print 'Incorrect!'
    exit()
if data[::7] != 'r3Ap':
    print 'Incorrect!'
    exit()
print 'Correct!'

'''

flag = ['x' for x in range(28)]
flag[-2] = 'n'
flag[10] = '3'
flag[::-2] = '_otp5ar}3l3333'
flag[::-3] = '_hpvrtls3r'
flag[::-5] = '_yat3v'
flag[::-7] = '_{}s'
flag[::4] = 'rr_tk{h'
flag[::7] = 'r3Ap'

print ''.join(flag)
