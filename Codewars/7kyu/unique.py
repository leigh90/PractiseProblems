# Take 2 strings s1 and s2 including only letters from ato z.
#  Return a new sorted string, the longest possible, 
# containing distinct letters - each taken only once - coming from s1 or s2.

# Pseudocode
# join the two string 
# remove the duplicates
# sort the string


a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

def longest(a1, a2):
    new_string = a1+a2
    test_c = list(set(new_string))
    lister= ""
    test_c.sort()
    new_testb = lister.join(test_c)
    return new_testb

longest(a1,a2)