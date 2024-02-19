import cpsc253_chp2_prb7b_functionized as c
import random
while True:
    s = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for n in range(48))
    x = c.hashme(s)
    if x == "BFQG":
        print("Found!")
        print(s)
        break