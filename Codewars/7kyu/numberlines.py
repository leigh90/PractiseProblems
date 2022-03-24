def number(lines):
    num_list = list(range(1,len(lines)+1))
    numbered_dict = dict(zip(num_list, lines))
    new_list = [(str(key) +": " + val).strip() for key,val in numbered_dict.items()]
    print(new_list)

   
number(["a", "b", "c"])
# ["1: a", "2: b", "3: c"]