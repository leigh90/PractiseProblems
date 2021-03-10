def hex_hash(code):
    word_dec = []
    num_list = []
    # convert string to ascii then to hexcode
    for i in code:
        decimal = hex(ord(i))
        # remove address location
        word_dec.append(decimal[2:])
    print(word_dec)
    # create a full string
    word_dec = ''.join(word_dec)
    print(word_dec)
    # loop through the string to separate digits and return the sum
    for char in word_dec:
        if char.isdigit():
            num_list.append(int(char))
    print(sum(num_list))

hex_hash('Hello World')


