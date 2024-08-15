# Write a Python program that inputs a list of words, separated by white- space,
# and outputs how many times each word appears in the list.
# You need not worry about efficiency at this point, however,
# as this topic is something that will be addressed later in this book.

# Example 1
from collections import Counter

words = input('Enter the words: ').split(' ')
lst_words = list(words)

word_counter = Counter(lst_words)
for key, value in word_counter.items():
    print(f'{key}: {value}')


# Example 2
words = input('Enter words:\n')
words=words.split(' ')

word_list = set(words)
word_count={}
for word in word_list:
    if word != '':
        word_count[word]=words.count(word)

print(word_count)