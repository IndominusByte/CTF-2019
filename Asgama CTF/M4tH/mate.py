from z3 import *

s = Solver()
key = [Int(x) for x in range(197)]
s.add(key[8]  == 102 )
s.add(key[20] == 101 )
s.add(key[48] == 51 )
s.add(key[52] == 104 )
s.add(key[56] == 76 )
s.add(key[68] == 85 )
s.add(key[72] == 105 )
s.add(key[96] == 48 )
s.add(key[108] == 114 )
s.add(key[112] == 49 )
s.add(key[116] == 70 )
s.add(key[124] == 108 )
s.add(key[136] == 112 )
s.add(key[156] == 117 )
s.add(key[164] == 89 )
s.add(key[196] == 78)

print "====== LV 1 ====="
print s.check()
print len(s.model())
print s.model()

s.add(key[160] + key[140] + key[120] + key[100] + key[80] + key[60] + key[40] + key[20] + key[0] + key[180] == 873 )
s.add(key[164] + key[144] + key[124] + key[104] + key[84] + key[64] + key[44] + key[24] + key[4] + key[184] == 806 )
s.add(key[168] + key[148] + key[128] + key[108] + key[88] + key[68] + key[48] + key[28] + key[8] + key[188] == 749 )
s.add(key[172] + key[152] + key[132] + key[112] + key[92] + key[72] + key[52] + key[32] + key[12] + key[192] == 800 )
s.add(key[176] + key[156] + key[136] + key[116] + key[96] + key[76] + key[56] + key[36] + key[16] + key[196] == 795)

print "====== LV 2 ====="
print s.check()
print len(s.model())
print s.model()

s.add(key[0]  == key[24] and key[24]  == key[128] )
s.add(key[40] == key[64] and key[64]  == key[168] )
s.add(key[12] == key[80] and key[80]  == key[104] )
s.add(key[52] == key[120] and key[120] == key[144] )

s.add(key[16] == key[32]
and key[32]  == key[76]
and key[76] == key[84]
and key[84]  == key[88]
and key[88]  == key[92]
and key[92]  == key[140]
and key[140] == key[160]
and key[160] == key[180]
and key[180] == key[184] )

s.add(key[4] == key[112] and key[112] == key[132] )

s.add(key[28] == key[36]
and key[36] == key[44]
and key[44] == key[172] )

s.add(key[48]  == key[148] and key[148] == key[176] )
s.add(key[20]  == key[100] )
s.add(key[60]  == key[188] )
s.add(key[152] == key[192] )

print "====== LV 3 ====="
print s.check()
print len(s.model())
print s.model()

s.add(key[0]  * key[196] == 6006 )
s.add(key[4]  * key[192] == 4067 )
s.add(key[8]  * key[188] == 7038 )
s.add(key[12] * key[184] == 7980 )
s.add(key[16] * key[180] == 9025 )
s.add(key[20] * key[176] == 5151 )
s.add(key[24] * key[172] == 4081 )
s.add(key[28] * key[168] == 2756 )
s.add(key[32] * key[164] == 8455 )
s.add(key[36] * key[160] == 5035 )
s.add(key[40] * key[156] == 6084 )
s.add(key[44] * key[152] == 4399 )
s.add(key[48] * key[148] == 2601 )
s.add(key[52] * key[144] == 10816 )
s.add(key[56] * key[140] == 7220 )
s.add(key[60] * key[136] == 7728 )
s.add(key[64] * key[132] == 2548 )
s.add(key[68] * key[128] == 6545 )
s.add(key[72] * key[124] == 11340 )
s.add(key[76] * key[120] == 9880 )
s.add(key[80] * key[116] == 5880 )
s.add(key[84] * key[112] == 4655 )
s.add(key[88] * key[108] == 10830 )
s.add(key[92] * key[104] == 7980 )
s.add(key[96] * key[100] == 4848)

print "====== LV 4 ====="
print s.check()
#print len(sorted(s.model()))
print len(s.model())
print s.model()
'''
a1 = [
 k!0   = 77,
 k!4 = 49,
 k!8 = 102,
 k!12 = 84,
 k!16 = 95,
 k!20 = 101,
 k!24 = 77,
 k!28 = 53,
 k!32 = 95,
 k!36 = 53,
 k!40 = 52,
 k!44 = 53,
 k!48 = 51,
 k!52 = 104,
 k!56 = 76,
 k!60 = 69,
 k!64 = 52,
 k!68 = 85,
 k!72 = 105,
 k!76 = 95,
 k!80 = 84,
 k!84 = 95,
 k!88 = 95,
 k!92 = 95,
 k!96 = 48,
 k!100 = 101,
 k!104 = 84,
 k!108 = 114,
 k!112 = 49,
 k!116 = 70,
 k!120 = 104,
 k!124 = 108
 k!128 = 77,
 k!132 = 49,
 k!136 = 112,
 k!140 = 95,
 k!144 = 104,
 k!148 = 51,
 k!152 = 83,
 k!156 = 117,
 k!160 = 95,
 k!164 = 89,
 k!168 = 52,
 k!172 = 53,
 k!176 = 51,
 k!180 = 95,
 k!184 = 95,
 k!188 = 69,
 k!192 = 83,
 k!196 = 78,
]

'''
a1 = [  77, 49, 102, 84, 95, 101, 77, 53, 95, 53, 52, 53, 51, 104, 76, 69, 52, 85, 105, 95, 84,
        95, 95, 95, 48, 101, 84, 114, 49, 70, 104, 108, 77, 49, 112, 95, 104, 51, 83, 117, 95,
        89, 52, 53, 51, 95, 95, 69, 83,78]

v = [3071071080, 2075331335, 1110954624, 3042175500, 3456936000, 3317413680, 4746373632, 4893178680, 1188400980, 4031521650]

for i in range(10):
#    s.add(key[4*(5*i+0)] * key[4*(5*i+1)] * key[4*(5*i+2)] * key[4*(5*i+3)] * key[4*(5*i+4)] == v[i])
    v5 = a1[5*i+0] * a1[5*i+1] * a1[5*i+2] * a1[5*i+3] * a1[5*i+4]
    print v5
    if v[i] == v5 :
        print "OK"

stro = ''.join(chr(a1[x]) for x in range(len(a1)))
print stro

v8 = ''
for i in range(10):
    for j in range(5):
        #v8 = stro[10*j+i]
        v8 += stro[10*j+i]

print v8

#1234567890
#16XXXXXXXX27XXXXXXXX38XXXXXXXX49XXXXXXXX50XXXXXXXXXX
