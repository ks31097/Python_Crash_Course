def count_words(filename):
    """Counting words in a document"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # with open('missing_file.txt', 'a') as f:
        #     f.write(f"{filename}\n")
        pass
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['moby_dick.txt', 'alice.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)