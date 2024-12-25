#Challenge: Count Words Ending with Vowels
sentence = input("Enter a sentence: ").split()
Vowels_set = {"a","e","i","o","u"}
Vowels_Counter = 0
for words in sentence:
    if(words.lower()[-1] in Vowels_set):
        Vowels_Counter += 1
print("Words Ending with Vowels: ", +Vowels_Counter)
#Input:This is an example input
#Output:Words Ending with Vowels 1

#Optimized slightly for readability and performance.
sentence = input("Enter a sentence: ").split()
vowels = "aeiou"
vowel_count = sum(1 for word in sentence if word.lower()[-1] in vowels) 
#if the generator is true then it increments the value to 1
# inside sum() is the generator expression -> like list comprehension
print("Words Ending with Vowels:", vowel_count)
#New things Learned: Sum() function {Syntax: Sum(iterable,start)

#Iterable can be List,Set,Tuple Not Dicionaries

#start (Optional):An initial value to start the sum with. The default value is 0
