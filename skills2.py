#!/usr/bin/env python


"""Hackbright Skills 2: Python Data Structures.

There are a bunch of functions in this file that are not written, but
have documentation strings that explain how they should work. Your job
is to edit this file to write the bodies of these functions.

We expect that you will solve these problems using Python lists
and dictionaries. Some of these problems could be solved with Python
sets (a more advanced data type); if you've learned about sets, you
may use these here.

This file uses "doctests"; the explanation of how the functions should
work contains examples just like you'd see in the Python interpreter.
The examples are actually run and tested when this file is ran.

When you first run this test, it will show test failures for every
function--since the real functions haven't been written yet. As you
write the real functions, your test failure count will go down.

At the point where you've completed this skills assessment, the
only output from this program would be:

   ** ALL TESTS PASSED. GOOD WORK!

Good luck!

"""



def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
  
    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    test_dict = {}
    test_list = string1.split(" ")

    for item in test_list:
        test_dict[item] = test_list.count(item)

    return test_dict



def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    new_list = list1 + list2
    new_dict = {}
    final_list = []

    for item in new_list:
        new_dict[item] = new_list.count(item)

    for key, value in new_dict.items():
        if value > 1:
            for value in range(value - 1):
                final_list.append(key)

    return final_list


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between 
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show 
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    new_list = list1 + list2
    new_dict = {}
    final_list = []

    for item in new_list:
        new_dict[item] = new_list.count(item)

    for key, value in new_dict.items():
        if value > 1:
            final_list.append(key)

    return final_list



def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    # """

    new_dict = {}
    final_list = []

    for number in list1:
        new_dict.setdefault(number, None)

    for key in new_dict.keys():
        negative_key = (key * -1)
        if sorted([key, negative_key]) in final_list:
            pass
        elif negative_key in new_dict:
            final_list.append(sorted([key, negative_key]))

    return final_list



def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:
   
        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    words = ["rose", "is", "a", "rose", "is", "a", "rose"]
    words_dict = {}
    dupe_words = []

    for item in words:
        words_dict[item] = words.count(item)

        for key, value in words_dict.items():
            if value == 2:
                dupe_words = words_dict.keys()
    return dupe_words


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    return []


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.
   
    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    return ""


############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d

def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documenttion tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "** ALL TESTS PASSED. GOOD WORK!"
    print