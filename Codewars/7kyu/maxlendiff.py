import random
def mxdiflg(a1, a2):
    pick_x, pick_y = random.randint(0,(len(a1)-1)), random.randint(0,(len(a2)-1))
    print(pick_x, pick_y)
    print(a1[pick_x], a2[pick_y])
    x = a1[pick_x]
    y= a1[pick_y]
    print(len(x),len(y))

    # found = max(abs(len(x) -len(y)))
    print(len(x) - len(y))
    print(abs(len(x) - len(y)))
    print(max(abs(len(x) - len(y))))



    # print(found)



    



mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"])