def feast(beast, dish):
    # check if the first letter of beast == first letter of food
    # print(beast[0])
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        print(True)
    else:
        print(False)
    # check if the last letter of beast == last letter of food
    print(dish[-1])

    

#  the great blue heron is bringing garlic naan 
#  and the chickadee is bringing chocolate cake.

feast('pig','chocolate cake' )