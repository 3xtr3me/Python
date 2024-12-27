#Challenge:Program that counts how many words in a given sentence contain atleast one vowel
sentence = input("Enter a sentence: ").split()
Vowels_Dictionary = {"a","e","i","o","u"}
Vowel_Counter = 0
for words in sentence:
    if any(char in Vowels_Dictionary for char in words.lower()): # Check if any character is a vowel
        Vowel_Counter += 1
print("Total Count: ",Vowel_Counter)
#Input:Python is fun
#Output: Total Count:  3
#New function learned -> any() function The any() function returns 'True' if any item in an iterable are true, otherwise it returns False.If the iterable object is empty, the any() function will return False
