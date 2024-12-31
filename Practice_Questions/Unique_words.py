#Challenge:This Challenge requires you to check if the letters are unqiue in the word 
sentence = input("Enter a sentence: ").split()
unique_word_count = sum(
    1 for words in sentence if words.isalpha() and len(words.lower()) == len(set(words.lower())))
print("Words with unique characters: ", unique_word_count)
#Input:Wow! This is amazing
#Output:Words with unique characters:  2
#Set() Funtion removes all the duplicates.
