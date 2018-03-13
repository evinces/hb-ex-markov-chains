"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(file_path).read()

    return file_string


def make_chains(text_string):
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
    lst = text_string.split()
    for i in range(len(lst)-1):
        key_tuple = (lst[i], lst[i+1])
        try:
            if key_tuple in chains:
                chains[key_tuple].append(lst[i+2])
            else:
                chains[key_tuple] = [lst[i+2]]
        except IndexError:
            chains[key_tuple] = [None]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    keys = chains.keys()
    link = choice(keys)
    words.extend(link)
    next_word = choice(chains[link])
    while next_word is not None:
        words.append(next_word)
        link = (link[1], next_word)
        next_word = choice(chains[link])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
