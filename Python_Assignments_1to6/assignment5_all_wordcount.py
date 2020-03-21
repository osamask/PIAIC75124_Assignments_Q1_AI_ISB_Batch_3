"""Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def utility(filename):
  with open(filename) as f:
    str = f.read()
    words = str.lower()
    word_list = words.split()
    dict = {}
    for word in word_list:
      count = 0
      for occurrence in word_list:
        if occurrence == word:
          count += 1
      dict[word] = count  
    return dict  

def print_words(filename):
  dict = utility(filename)
  list = []
  for key in dict.keys():
    list.append(key)
  list = sorted(list)
  for word in list:
    for key in dict.keys():
      if key == word:
        print(key + " " + str(dict[key]))   

def print_top(filename):
  dict = utility(filename)
  list = []
  for value in dict.values():
    list.append(value)
  list = sorted(list, reverse = True)
  common = []
  for num in list:
    if len(common) == 0 or num != common[-1]:
      common.append(num)
  print(common)
  if len(common) > 20:
    common = common[0:20]  
  for wcount in common:
    for key in dict.keys():
      if dict[key] == wcount:
        print(key + " " + str(dict[key]))

def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
