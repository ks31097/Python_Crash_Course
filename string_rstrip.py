def empty_line():
    print(" " * 60)

favorite_language = ' python '
print(favorite_language)
empty_line()

print(favorite_language.rstrip())
empty_line()

print(favorite_language.lstrip())
empty_line()

print(f"{favorite_language.strip()}")
empty_line()

favorite_language = favorite_language.strip()
print(favorite_language)