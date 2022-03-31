def descending_order(num):
    num_list = list(str(num))
    pre_sort = [int(ele) for ele in num_list]
    print(pre_sort)
    sorta =sorted(pre_sort, reverse=True)
    print(sorta)
    full = [str(ele) for ele in sorta]
    big = int(''.join(full))
    print(big)


descending_order(42145)


# One liner I liked
def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))