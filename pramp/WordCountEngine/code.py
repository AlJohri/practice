"""
Word Count Engine

Question:

Implement a document scanning engine that receives a text document doc and
returns a list of all unique words in it and their number of occurrences,
sorted by the number of occurrences in descending order.

Example:
for doc: "practice makes perfect. get perfect by practice. just practice!"
the engine returns the list: { practice: 3, perfect: 2,  makes: 1, get: 1,
by: 1, just: 1 }.

The engine should ignore punctuation and white-spaces.
Find the minimal runtime complexity and analyze it.

Tips:
If your peer is stuck, you can start things up by asking about the data
structures needed for the solution

For each data structure, ask your peer to explain what it is and why is
it optimal in this case

Things your peer should relate to: clearing white-spaces and punctuation,
how to handle lowercase (not specified in the question but should be
	approached), how to recognize words that have already appeared

If your peer can't implement the some of the neccesary operations, frame
these actions as independent functions (such as getNextDocumentWord())
and allow your peer to use it and implement the other, more logical
parts of the solution (In this case, do note it on your peer's feedback)

If you have time, you can ask your peer what would improve the engine
and how these improvements can be implemented

"""

punctuation_to_remove = [".", ",", "!", "?", ";"]
# allow "'", "-"

string = "practice makes perfect. get perfect by practice. just practice!"

string = "practice  |  perfect.  amazing! "

def word_count_engine(string):

   word_list = {}

   word_start_index = 0
   word_end_index = 0
   current_word = ""

   i = 0

   while(i < len(string)):
      if char in punctuation_to_remove: continue

      # first space at the end of a word
      if char is " ":
         word_end_index = i-1
         current_word = substr(string, word_start_index, word_end_index).trim()
         current_word = lower(current_word)
         if current_word in word_list:
            word_list[current_word]++
         else:
            word_list[current_word] = 1
         word_start_index = i+1

      i += 1

   # sort this
   return sorted(word_list.items(), key=operator.itemgetter(1))

###########
### Word count problem
# doc scanning engine
# input: string
# dict: keys -> words, values -> counts
###

import re
from collections import defaultdict

def word_count_engine(my_string):
   dictionary = defaultdict(int)
   match = re.scan(my_string, r"\b[\w'\-\d]+\b")
   for word in match.groups():
      dictionary[word] += 1
   return dictionary

"""

Solution:

Let doc be the number of n words and m unique words (m ≤ n).

Stage 1: we split the words (by spaces in doc).
For each word w, we clean it from all non alpha characters (digits,
punctuation etc) and convert it to lowercase to make the counting
case-insensitive.
We'll use a hash table to count all appearing words (using w as the
key and maintain the number of its occurrences as the value).
A hash table is optimal in this case because it gives us find, store
and update operations on O(1) runtime complexity (amortized and
assuming we have a good hash function).
Therefore, scanning the document and counting the number of unique
words can be done at O(n), which is also the minimal complexity to
process any input of n words

Stage 2: Once we have a list of the words and its number of occurrences
in the document we need to sort the list by number of occurrences, in
descending order. Sorting of m words can be done on O(m⋅log m) runtime complexity

The overall runtime complexity is O(n + m⋅log m).

Possible improvements of the engine: concurrent processing of the
document with multiple engine instances and improvement of search
by words stemming.
"""