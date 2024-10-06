numbers_list = list(range(1, 10))
print(f"Numbers list: {numbers_list}")
numbers = numbers_list[:]
print(f"Numbers: {numbers}")
removed_numb = 4
numbers_list.remove(4)
print(f"\nRemoved numb: {removed_numb}")
print(f"Numbers list: {numbers_list}")

if numbers:
    for number in numbers:
        if number == 1:
            print(f"{number}) {number}st")
        elif number == 2:
            print(f"{number}) {number}nd")
        elif number == 3:
            print(f"{number}) {number}rd")
        else:
            print(f"{number}) {number}th")