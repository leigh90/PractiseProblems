from collections import Counter
def find_deleted_number(arr, mixed_arr):
    if len(arr) == len(mixed_arr):
        return 0
    else:
        set_a, set_b = set(arr),set(mixed_arr)
        print(list(set_a - set_b)[0])

        # YOU CAN USE COLLECTION MODULE FOR THE .counter() method
        # res = list((Counter(arr) - Counter(mixed_arr)))
        # print(res[0])






find_deleted_number([1,2,3,4,5,6,7,8,9],[3,2,4,6,7,8,1,9])