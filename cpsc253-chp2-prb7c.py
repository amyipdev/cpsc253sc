import cpsc253_chp2_prb7b_functionized as c
chars = [0 for _ in range(48)]
while True:
    s = "".join([chr(n+65) for n in chars])
    res = c.hashme(s)
    if res == "BFQG":
        print("Found result: ")
        print(s)
        break
    chars[47] += 1
    cf = 0
    for n in range(47, -1, -1):
        if cf:
            chars[n] += 1
            cf = 0
        if chars[n] >= 26:
            cf = 1
            chars[n] %= 26