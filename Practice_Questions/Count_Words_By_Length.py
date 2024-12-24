#Challenge:Python Program that counts words by length
#Learned new things in this program(Countinue,Break,and the Dictionary Get function)
sentence = input("Enter a sentence: ").split()
dictionary = {}

# Iterate through each word in the sentence
for word in sentence:
    # Skip punctuation or empty inputs
    if word in ".?!":
        continue
    # Dynamically update the dictionary based on word length
    word_length = len(word)
    dictionary[word_length] = dictionary.get(word_length, 0) + 1

# If no valid words were entered, handle empty input
if not dictionary:
    print("Please enter a valid sentence with words.")
else:
    print("Word length counts:", dictionary)
#Input:I love coding in Python because it's fun
#Output:Word length counts: {1: 1, 4: 2, 6: 2, 2: 1, 7: 1, 3: 1}
