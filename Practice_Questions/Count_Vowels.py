#Write a Python program that takes a string as input and counts the number of vowels in it.
# Take input from the user
string = input("Enter any message: ")

# Initialize counters
vowel_counter = 0
consonant_counter = 0

# Define a set of vowels for fast lookup
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Loop through each character in the string
for char in string:
    if char in vowels:  # Check if the character is a vowel
        vowel_counter += 1
    elif char.isalpha():  # Check if it's an alphabetic character
        consonant_counter += 1

# Count the number of words in the string
word_count = len(string.split())

# Print the results
print(f"The string has {vowel_counter} vowels, {consonant_counter} consonants, and {word_count} words.")

#string = input("Enter any message: ")
#word_counter = 0
#vowel_counter = 0
#for words in string:
#    if(words == 'a' or words =='e' or words == 'i' or words == 'o' or words =='u' ):
#        vowel_counter += 1
#    else:
#        word_counter += 1
#total_words = vowel_counter + word_counter
#print("The word Has " +str(vowel_counter) +" vowels and has " +str(total_words) +" words ")
#This is  my code but the code has been optimized by ChatGPT
