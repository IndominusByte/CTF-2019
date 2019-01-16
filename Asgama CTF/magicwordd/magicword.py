cigam = "mbO`^Ifco^DfifPqf@buMf^iFal@flRqQr`"
flag = "SupeRcaLifraGiliStiCexPialIdoCioUs"
j = ""
for i in range(len(cigam)):
    if i == 0 or i == len(cigam)-1:
        j += chr(ord(cigam[i]) + 2)
    else:
        j+= chr(ord(cigam[i]) + 3 )

print j
