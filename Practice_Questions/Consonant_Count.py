#Challenge: Count The Words that begin with the consonants
sentence = input("Enter a sentence: ").split()
Not_Consonant_Words = "aeiou"
Consonant_Counter = sum(1 for words in sentence if words.isalpha() and words.lower()[0] not in Not_Consonant_Words)
print("The Number of Consonant Words are:",+Consonant_Counter)
#Input:The 42rules! jump over the lazy dogs
#Output:The Number of Consonant Words are: 5
