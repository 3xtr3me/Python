#Challenge:Counting Words Containing Only Alphabetical Characters
import string
sentence = input("Enter a sentence: ").split()
counter = 0
for words in sentence:
    cleaned_words = words.strip(string.punctuation)
    if cleaned_words.isalpha():
        counter += 1
print("Words Containing Only letter:",counter)
#Input: Hello World! 123 Python3 is fun.
#Output: Words Containing Only letter: 4
#New things: string.punctuation contains all the punctuations.
