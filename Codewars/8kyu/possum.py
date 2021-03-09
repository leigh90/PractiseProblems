def positive_sum(arr):
    pos_nums = []
    neg_nums = []
    for num in arr:
        if num > 0:
            pos_nums.append(num)

    print(sum(pos_nums))
    if pos_nums == []:
        print(0)

    


    

            


    
    # return 0
positive_sum([1,-4,7,12])