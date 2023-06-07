# Task#1Split in Half
def split_in_half(n):
    center = len(n) // 2
    first_half = n[:center]
    second_half = n[center:]
    if len(n)%2 != 0:
        first_half = n[:center + 1]
        second_half = n[center + 1:]
    result = second_half + first_half
    return result


string = 'bbbbbcaaaaa'
print(split_in_half(string))


# Task#2Unique Characters in String
def unique_characters(n):
    return len(n) == len(set(n))

string1 = 'aabcde'
string2 = 'abc'
string3 = 'abcde'
print(unique_characters(string1))
print(unique_characters(string2))
print(unique_characters(string3))
