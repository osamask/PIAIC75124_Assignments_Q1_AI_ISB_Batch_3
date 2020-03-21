"""Mimic pyquick exercise -- optional extra exercise.
Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  with open(filename) as f:
    str = f.read()
    words = str
    word_list = words.split()
    mim_dict = {}
    for word in word_list:
      each_list = []
      word_index = word_list.index(word)
      if word_index == 0:
        mim_dict[""] = [word]
      if word_index == len(word_list) - 1:
        break
      if word in mim_dict:
        continue
      for next in word_list:
        if next == word:
          count = len(each_list)
          #next_index = word_list.index(next)
          if count == 0:
            each_list.append(word_list[word_index + 1])
          if count > 0:
            each_list.append(word_list[right_index(word_index, count, next, word_list)])
      mim_dict[word] = each_list
    print(mim_dict)
  return mim_dict


def right_index(ind, count, w, list):
  for i in range(count):
    ind += 1
    next_occ = list.index(w, ind)
    ind = next_occ
  next_occ += 1
  return next_occ


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  for i in range(200):
    print (word),
    next = mimic_dict.get(word)
    if next == None:
      next = mimic_dict['']
    word = random.choice(next)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)
  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
