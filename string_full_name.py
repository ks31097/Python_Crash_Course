first_name ="ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("=" * 60)
another_full_name = "{} {}".format(first_name, last_name)
print(another_full_name.upper())