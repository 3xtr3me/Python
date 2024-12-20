sentence = input("Enter a sentence: ").split()
Vowels = {'a','e','i','o','u'}
words_isVowels = []
for words in sentence:
    if(words[0].lower() in Vowels):
        words_isVowels.append(words)
print(words_isVowels)
