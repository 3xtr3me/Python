#This Program prints out the longest word in the sentence which is given by the user
sentence = input("Enter a sentence ").split()
longest_word = []
stored_word = 0
for current_word in sentence:
    if len(current_word) > stored_word:
        longest_word = [current_word]
        stored_word = len(current_word)
    elif len(current_word) == stored_word:
        longest_word.append(current_word)
print(longest_word)
