from name_function import get_formatted_name as full_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first.strip().lower() == 'q':
        break
    last = input("Please give me a last name: ")
    if last.strip().lower() == 'q':
        break

    formatted_name = full_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")