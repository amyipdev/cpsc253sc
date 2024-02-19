k = input("Key: ")
m = input("Ciphertext: ")
r = []
pos = 0
for c in m:
    if c == ' ':
        r.append(' ')
        pos += 1
        continue
    cl = k[pos % len(k)]
    if cl == ' ':
        r.append(c)
        pos += 1
        continue
    bv = ord(c) - 65
    if bv < 0 or bv > 57:
        r.append(c)
        pos += 1
        continue
    while True:
        tv = bv - pos - ord(cl)
        if tv < 0:
            bv += 58
            continue
        r.append(chr(tv + 65))
        break
    pos += 1
print("".join(r))