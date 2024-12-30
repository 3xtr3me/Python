#Challenge: To count and display the words that contain all the vowels at least once, we need to ensure that each word contains every vowel
sentence = input("Enter a sentence: ").split()
Vowels = {'a','e','i','o','u'}
Vowel_Words = []
for words in sentence:
    Word_set=set(words.lower())
    if Vowels.issubset(Word_set):
        Vowel_Words.append(words)
print("Words Containing all the vowels",Vowel_Words)
print("Total Count:",len(Vowel_Words))
#Input:Education is a powerful medium of communication
#Output:Words Containing all the vowels ['Education']
#Total Count:1
