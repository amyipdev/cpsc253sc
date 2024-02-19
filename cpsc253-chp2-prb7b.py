import math
rt = [0,0,0,0]
dat = input("String to hash: ")
dat = [n.upper() for n in dat if n.isalpha()]
dat.extend(["A" for n in range(len(dat)%16)])
for n in range(len(dat)//16):
    cs = [ord(n)-65 for n in dat[(n*16):(n+1)*16]]
    rt[0] += cs[0] + cs[4] + cs[8] + cs[12] + cs[1] + cs[6] + cs[11] + cs[15]
    rt[1] += cs[1] + cs[5] + cs[9] + cs[13] + cs[2] + cs[7] + cs[8] + cs[14]
    rt[2] += cs[2] + cs[6] + cs[10] + cs[14] + cs[3] + cs[4] + cs[9] + cs[13]
    rt[3] += cs[3] + cs[7] + cs[11] + cs[15] + cs[0] + cs[5] + cs[10] + cs[12]
print("".join([chr(n % 26 + 65) for n in rt]))    