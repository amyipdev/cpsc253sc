k = input("Key: ")
m = input("Message: ")
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
    cv = ord(c) - 65
    if cv < 0 or cv > 57:
        r.append(c)
        pos += 1
        continue
    rv = (cv + ord(cl) + pos) % 58 + 65
    r.append(chr(rv))
    pos += 1
print("".join(r))