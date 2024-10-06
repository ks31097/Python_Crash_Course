names = ['elon', 'jen', 'alex', 'sarah', 'sem', 'edward', 'amanda', 'phil', 'marti',]

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

print(f"{favorite_languages}")
if favorite_languages:
    for name in sorted(names, reverse=False):
        if name.lower() in favorite_languages.keys():
            print(f"Thank you, {name} for your answer!")
        else:
            print(f"Can you {name} spare some time for our survey on the topic \"Favorite programing language\"")

# print(names)

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# items()
    for name, languages in favorite_languages.items():
        if len(languages) == 1:
            print(f"\n{name.title()}'s favorite language is:")
            print(f"\t {(' '.join(languages)).title()}")
        else:
            print(f"\n{name.title()}'s favorite languages are:")
            for language in languages:
                print("\t" + language.title())
# # keys()
# names = []
# for name in favorite_languages:
# # for name in favorite_languages.keys():
#     print(name.title())
#     names.append(name.lower())

# print(names)
# print(favorite_languages.keys())
# print(list(favorite_languages.keys()))


# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")

# if 'erib' not in favorite_languages.keys():
#     print("\nErin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     # print(name)
#     print(f"{name.title()}, thank you for taking the poll.")

# print("\nThe following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# print("\nThe following language have been mentioned:")
# for language in sorted(set(favorite_languages.values())):
#    print(language.title())