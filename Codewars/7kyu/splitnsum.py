def sum_digits(number):
    if number < 0:
        number *= -1
    num_list = list(str(number))
    sumof = sum([int(num) for num in num_list ])
    print(sumof)

sum_digits(-32)

# something I learnt

a = 10
b = 5
print(eval('a * b'))