# Task#1 Reverse a Statement
def reverse_statement(n):
    split_string = n.split()
    reverse_string = split_string[::-1]
    final_statement = ' '.join(reverse_string)
    return final_statement


print(reverse_statement("Everything is hard before it is easy"))


# Task#2 Write a solution that will print all permutations of a string.
def permutations(n):
    if n == "":
        return []
    if len(n) == 1 or len(n) == 0:
        return [n]
    p_list = []
    used_chars = set()
    for i in range(len(n)):
        if n[i] in used_chars:
            continue
        used_chars.add(n[i])
        for j in permutations(n[:i] + n[i + 1:]):
            p_list.append(n[i] + j)

    return p_list


print(permutations("ABC"))
print(permutations("AB"))
print(permutations("EFF"))


# Task#3 Create a program that will count vowels and consonants in a string.
def count_char(n):
    n = n.lower()
    vowels = 0
    consonants = 0
    vowel_set = set("aeiou")
    for i in n:
        if i.isalpha():
            if i in vowel_set:
                vowels += 1
            else:
                consonants += 1
    return f"Vowels:{vowels}, Consonants:{consonants}"


print(count_char("Hello world"))
