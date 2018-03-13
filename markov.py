"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


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
    for i in range(len(lst) - n_gram + 1):
        key_list = []
        for j in range(n_gram):
            key_list.append(lst[i+j])
        key_tuple = tuple(key_list)

        try:
            if key_tuple in chains:
                chains[key_tuple].append(lst[i+n_gram])
            else:
                chains[key_tuple] = [lst[i+n_gram]]
        except IndexError:
            chains[key_tuple] = [None]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    keys = chains.keys()
    keys = [key for key in keys if key[0][0].isupper()]
    link = choice(keys)
    words.extend(link)

    next_word = choice(chains[link])
    while next_word is not None:
        words.append(next_word)

        link_list = []
        for i in range(1, len(link)):
            link_list.append(link[i])
        link_list.append(next_word)
        link = tuple(link_list)

        next_word = choice(chains[link])

    return " ".join(words)


if len(argv) > 1:
    input_path = argv[2]
else:
    # input_path = "green-eggs.txt"
    input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

input_path = "green-eggs.txt"
input_text = open_and_read_file(input_path)
add_to_chains = make_chains(input_text)

chains.update(add_to_chains)

# Produce random text
random_text = make_text(chains)

print random_text
