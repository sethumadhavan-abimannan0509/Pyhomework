def even_numbers(number):
    even = []

    for i in number:
        if i % 2 == 0:
            even.append(i)
    return even

list1 = [1, 2, 3, 4, 5]

print(f"This is unmodified list: {list1}")
print(f"This is only even numbers list: {even_numbers(list1)}")