def square_digits(num):
    string_num= str(num)
    string_list = []
    squared_list = []
    string_list = list(string_num)
    for num in string_list:
        num = int(num)** 2
        squared_list.append(str(num))
    print(squared_list)

    squared_list = "".join(squared_list)
    

    print(int(squared_list))

# one i like
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)
        




square_digits(9119)



