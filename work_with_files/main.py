from text_reader import file_reader

text = "work_with_files/text_from_wiki.txt"
word = input("Input the word: ")

information = file_reader(text)
result = information.lower().count(word)

print(f"The word \"{word}\" appears in the text {result}.")

# try:
#     list = file_reader(text)
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print(list)