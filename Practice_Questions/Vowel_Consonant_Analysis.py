#Challenge: To count how many words in a sentence contain both vowels and consonants
#import the string module for punctuation
import string
sentence = input("Enter a sentence: ").split()
Vowel_Set = {"a","e","i","o","u"}
Vowel_consonant_counter = 0
for words in sentence:
    #Remove punctuation from the word using translate once
    cleaned_words = words.translate(str.maketrans('','',string.punctuation)).lower()
    # Use set membership and isalpha to check for both vowels and consonants
    if (any(char in Vowel_Set for char in cleaned_words) and any(char not in Vowel_Set and char.isalpha() for char in cleaned_words)):
            Vowel_consonant_counter += 1
print("Words with both vowels and consonants:",Vowel_consonant_counter)
#Input:It's a bright day for coding
#Output:Words with both vowels and consonants: 5

#Learned new things translate(),isalppha()

#translate() ->replace characters in a string based on a translation table (which you provide) or using a map of characters to their replacements.

#translate() applies a translation table to replace characters in a string.
#str.maketrans() is used to create that table -> str.maketrans('', '', string.punctuation)
