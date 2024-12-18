#Writing the word count frequency function
#Taking the sentence from the user
sentence = input('Enter a Sentence: ').split()
word_count = {}
for word in sentence: #checking the word in split sentence
    word_count[word] = word_count.get(word, 0) + 1
#If it’s not in the dictionary, it's added with a value of 1.
#If it’s already in the dictionary, its value is incremented by 1.
print(word_count)
#Output:
#Enter a Sentence: Hello World Hello
#{'Hello': 2, 'World': 1}
