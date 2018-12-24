import sys
import re


def output_dictionary(filename):
    """ str -> dict of {int: int}
    Read from the file, and output a dictionary where
    the keys are word lengths, and the values are the
    number of words that correspond to that length.
    """
    dictionary = {}
    file = open(filename)
    for line in file:
        line = line.rstrip()
        word_array = re.split("\W+", line)
        for word in word_array:
            if not word.isalpha():
                continue
            if len(word) not in dictionary:
                dictionary[len(word)] = 0
            dictionary[len(word)] = dictionary[len(word)] + 1

    return dictionary


def main():
    if len(sys.argv) < 2:
        print("Please input the filename as a command-line argument.")
        return

    filename = sys.argv[1]
    dictionary = output_dictionary(filename)
    for length, frequency in dictionary.items():
        print("Words of length " + str(length) + ": " + str(frequency))


if __name__ == "__main__":
    main()
