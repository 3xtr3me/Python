# Challenge:Words with Consecutive Repeated Characters
sentence = input("Enter a sentence: ").split()
word_set =set()
for words in sentence:
    if words.isalpha():
        for i in range(len(words.lower())-1):
            if words.isalpha() and words[i] == words[i+1]:
                word_set.add(words)
                break
print("The consecutive words are :", len(word_set))
#Input:Hello apple book keeper yellow Woohoo.
#Output:The consecutive words are : 5
