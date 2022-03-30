# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(string, ending):
    length = (len(ending))
    string_end = (string[-length:])
    print(string_end)
    if ending == string_end or ending == '':
        print('True')
    else:
        print('False')
   



solution('abcde', 'cde')

# One I found and liiked ;)
def solution(string, ending):
    return string.endswith(ending)