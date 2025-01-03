#Challenge:Counting Words Ending with Specific Letters
import string
sentence = input("Enter a sentence: ").split()
set_of_letters = input("Enter set of letters seperated by commas: ")
letters_set = set(item.strip() for item in set_of_letters.split(','))

Letter_counter = sum(1 for words in sentence 
                     if letters_set.issubset(set(words.translate(str.maketrans('', '', string.punctuation)).lower())))
print("Count of words ending with the specified letters: ",Letter_counter)
#Input:Enter a sentence: Count of words ending with the specified letters
#Input:Enter set of letters seperated by commas: n,g
#Output:Count of words ending with the specified letters:  1
