def count_words(filename):
    """Count the approximate number of words in a file.
    :param filename:
    """
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")

filename = "alice.txt"
count_words(filename)

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt",
             "little_women.txt"]
for filename in filenames:
    count_words(filename)
