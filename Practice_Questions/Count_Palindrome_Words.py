#Challenge:Count how many Palindrome users are there
#Take sentence from the user
sentence = input("Enter a sentence: ").split()
Palindrome_words  = []
Palindrome_counter = 0
for words in sentence: 
    if(words.lower()[::-1] == words.lower()):
        Palindrome_words.append(words)
        Palindrome_counter += 1
print(Palindrome_words)
print("Total Count: ",Palindrome_counter)
#Input:Madam Anna went to Kayak racecar.
#Output:['Madam', 'Anna', 'Kayak', 'racecar'] Total Count:  4
