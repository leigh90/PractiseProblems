# without converting to a string
# convert to list
# loop through list
# append as new number
# wont work because you still have to convert to a string

# def ispalindrome(num):
#     rev_num = 0
#     while num > 0:
#         # divide the mumber and get the remainder
#         a = num % 10
#         print(a)
#         # multiply rev_num by 10 and add the remainder from dividing the number by 10 and set the new rev num to the new addition
#         rev_num = (rev_num * 10 ) + a
#         print(rev_num)
#         # floor divide num by 10 and this becomes your new num
#         num = num // 10
#         print(num)
#     if num <= 0:
#         if rev_num == num:
#             print(True)
#         else:
#             print(False)
#
#     print(rev_num)

def ispalindrome(num):
    rev_num = 0
    new_num = num
    while new_num > 0:
        a = new_num % 10
        rev_num = (rev_num * 10 ) + a
        new_num = new_num // 10

    print(rev_num)
    print(new_num)
    print(num)
    print(rev_num == num)
    # return rev_num
    # print(f'rev_num is {rev_num}')
    # print(f'num is {num}')
    # print(num == rev_num)

ispalindrome(121)