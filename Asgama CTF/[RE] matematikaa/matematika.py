from z3 import *

s = Solver()
key = [Int(str(x)) for x in range(25)]
print key
s.add( 107 * (key[0] + 40) == 16692 )
s.add( 101 * (key[1] + 103) == 15655 )
s.add( 116 * (key[2] + 97) == 23896 )
s.add( 101 * (key[3] + 107) == 15756 )
s.add( 109 * (key[4] + 32) == 9047 )
s.add( 117 * (key[5] + 110) == 24219 )
s.add( 32 *  (key[6] + 97) == 5408 )
s.add( 112 * (key[7] + 109) == 22848 )
s.add( 101 * (key[8] + 98) == 17473 )
s.add( 115 * (key[9] + 97) == 17135 )
s.add( 97 *  (key[10] + 104) == 17460 )
s.add( 110 * (key[11] + 32) == 8910 )
s.add( 32 *  (key[12] + 112) == 6624 )
s.add( 114 * (key[13] + 111) == 23484 )
s.add( 97 *  (key[14] + 105) == 17460 )
s.add( 104 * (key[15] + 110) == 23608 )
s.add( 97 *  (key[16] + 116) == 22310 )
s.add( 115 * (key[17] + 32) == 9660 )
s.add( 105 * (key[18] + 121) == 24255 )
s.add( 97 *  (key[19] + 97) == 14647 )
s.add( 32 *  (key[20] + 97) == 6144 )
s.add( 110 * (key[21] + 32) == 10780 )
s.add( 105 * (key[22] + 58) == 16275 )
s.add( 104 * (key[23] + 118) == 19656 )
s.add(32 * (key[24] + 41) == 2880)

print s.check()
print s.model()
m = [49,71,97,66,95,54,110,52,114,117,75,95,95,49,76,52,75,95,72,97,51,49,109,52,116]
lol = [chr(x) for x in m]
final = [x for x in lol]
final = ''.join(final)[::-1]
print final
