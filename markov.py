"""Generate Markov text from text files."""

from os.path import isfile
from sys import argv
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


# def make_chains(text_string, n_gram=2):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']

#         >>> chains[('there','juanita')]
#         [None]
#     """

#     chains = {}
#     words = text_string.split()
#     for i in range(len(words) - n_gram + 1):
#         key_list = []
#         for j in range(n_gram):
#             key_list.append(words[i+j])
#         key_tuple = tuple(key_list)

#         try:
#             if key_tuple in chains:
#                 chains[key_tuple].append(words[i+n_gram])
#             else:
#                 chains[key_tuple] = [words[i+n_gram]]
#         except IndexError:
#             chains[key_tuple] = [None]

#     return chains


# def make_text(chains):
#     """Return text from chains."""

#     words = []
#     link = choice([key for key in chains.keys() if key[0][0].isupper()])
#     words.extend(link)

#     next_word = choice(chains[link])
#     while next_word is not None:
#         words.append(next_word)

#         link_list = []
#         for i in range(1, len(link)):
#             link_list.append(link[i])
#         link_list.append(next_word)
#         link = tuple(link_list)

#         next_word = choice(chains[link])

#     return " ".join(words)


def make_chains(text_string, n_gram=2):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    for i in range(len(words) - n_gram):
        key_list = []
        for j in range(n_gram):
            key_list.append(words[i+j])
        key_tuple = tuple(key_list)

        if key_tuple in chains:
            chains[key_tuple].append(words[i+n_gram])
        else:
            chains[key_tuple] = [words[i+n_gram]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    link = choice([key for key in chains.keys() if key[0][0].isupper()])
    words.extend(link)

    while True:
        if chains.get(link) is not None:
            next_word = choice(chains[link])
            words.append(next_word)

            link_list = []
            for i in range(1, len(link)):
                link_list.append(link[i])
            link_list.append(next_word)
            link = tuple(link_list)
        else:
            break

    return " ".join(words)


def get_file_path():
    """Check path arguments for filename, else use green-eggs.txt"""

    if len(argv) > 1:
        if isfile(argv[1]):
            return argv[1]
        else:
            print "{} is not a file.".format(argv[1])
            print "Using green-eggs.txt as default."

    return "green-eggs.txt"
    # return "gettysburg.txt"


input_path = get_file_path()

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
