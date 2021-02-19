# parst csv data to python list
import csv

# with open('numbers.csv',newline='') as f:
#     csv_data = csv.reader(f)
#     data = list(csv_data)

# print(data)

# #flatten the list and convert the elements to integers.
# result = []
# for sublist in data:
#     for item in sublist:
#         result.append(int(item))

# print(result)

# new_list = []
# for i in result:
#     new_int = int(i)
#     new_list.append(new_int)


# print(new_list)
def flatten(data):
    result = []
    for sublist in data:
        for item in sublist:
            result.append(int(item))
    print(result)
    return result

def create_plist():
    """
    Open CSV file and convert data to python list
    """
    with open('numbers.csv',newline='') as f:
        csv_data = csv.reader(f)
        data = list(csv_data)
        flatten(data)
        return data
        
create_plist()







 