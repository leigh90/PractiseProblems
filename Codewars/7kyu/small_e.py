def small_enough(array, limit):
    above = []
    ok = []
    for i in array:
        if i  > limit:
            above.append(i)
        else:
            ok.append(i)
    print(above)
    print(ok)
    if len(above) == 0:
        print(True)
    else:
        print(False)
    

small_enough([1,2,4,6,9],9)