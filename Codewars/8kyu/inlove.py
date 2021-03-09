def lovefunc( flower1, flower2):
    # check if all are even
    if flower1 % 2 == 0 and flower2 % 2 == 0:
        print(False)
    # check if all are odd
    elif flower1 % 2 !=0 and flower2 % 2 != 0:
        print(False)
    else:
        print(True)

lovefunc(8,8)