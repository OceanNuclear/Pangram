"""
Find pangrams of length = 26
"""
import os
import unicodedata
from numpy import array as ary
import logging, random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_set = set(alphabet)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def count_occurance(string):
    lower_string = string.lower()
    return ary([ lower_string.count(i) for i in alphabet ])

look = remove_accents(os.popen("look .").read()).decode().split()
look = [word for word in look if len(word)>1]
norepeats = [word for word in look if (count_occurance(word)<=1).all()] # only use words with no repeated letters
ary_norepeats = ary(norepeats)

def find_next_word_excluding_set(forbidden_letter_set, prepending_indices=[]):
    for i, word in enumerate(norepeats):
        forbidden_letters_in_current_word = forbidden_letter_set.intersection(word.lower())
        if not forbidden_letters_in_current_word: # if no forbidden letters in current word
            # then add in the current word
            new_indices = prepending_indices.copy()
            new_indices.append(i)
            new_letters = alpha_set.intersection(word.lower())
            if random.uniform(0,1)<0.2: # randomized debugging
                print("\t"+" ".join(ary_norepeats[new_indices]))
            # calculate what still remains to be seen
            remaining_letter_set = forbidden_letter_set.union(new_letters)
            if remaining_letter_set:
                # if there are still letters left in the current set, use recursion.
                yield from find_next_word_excluding_set(remaining_letter_set, new_indices)
            else:
                # else it's a complete solution. Return it.
                yield new_indices

if __name__=="__main__":
    found_matches = []

    for index_list in find_next_word_excluding_set(set()):
        if sorted(index_list) not in found_matches:
            found_matches.append(sorted(index_list))
            print(index_list)
            print(" ".join(ary_norepeats[index_list]))
            input()
