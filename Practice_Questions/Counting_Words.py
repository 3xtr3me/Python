#Challenge: Counting Words of Specific Length
#Write a Python program that:
#Takes a sentence as input from the user.
#Counts and prints how many words in the sentence are exactly 'n' characters long.

character_count = int(input("Enter a the number of characters: "))
sentence = input("Enter a sentence: ").split()
words_counter = 0
for words in sentence:
    if len(words) == word_count:
        words_counter += 1
print("There are " +str(words_counter) +" words with exactly " +str(word_count) +" characters")

#Example Input:
#Enter the number of characters: 5  
#Enter a sentence: The quick brown fox jumps over the lazy dog
#Output:There are 3 words with exactly 5 characters
