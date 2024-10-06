programming_languages = ["JavaScript", "Python2", "Java", "Python3", "C++"]
# programming_languages.insert(programming_languages.index('JavaScript'), 'React')

try:
    print(programming_languages.index("React"))
except ValueError:
    print("That item does not exist")