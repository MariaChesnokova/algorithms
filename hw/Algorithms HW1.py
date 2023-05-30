# Task#1 Compute the sum of digits in all numbers from 1 to n.
def sum_of_digits(n):
    total = 0
    for i in range(1, n + 1):
        total += sum(int(d) for d in str(i))
    return total


print(sum_of_digits(5))


# Task#2 Find the max number from 3 values.
def max_number(a, b, c):
    max_value = max(a, b, c)
    return max_value


print(max_number(124, 21, 32))


# Task#3 Count odd and even numbers
def count_num(n):
    even = [int(i) for i in str(n) if int(i) % 2 == 0]
    odd = [int(i) for i in str(n) if int(i) % 2 != 0]
    even_count = str(len(even))
    odd_count = str(len(odd))
    print("The", str(n), " number contains ", even_count, " even digits:", even, " and ", odd_count, "odd digits:", odd)


count_num(34560)
