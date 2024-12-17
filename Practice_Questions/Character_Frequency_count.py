#Challenge:
#Write a program that counts how many times each character appears in a string provided by the user.

Text = input("Enter a text ")
dictionary = dict() #Can also use dict = {}
for char in text:
    if char not in dictionary:
        dictionary[char] = 1 #adds the character to the dictionary
    else:
        dictionary[char] = dictionary[char] + 1 #if the character exsists in the dictionary increment the character by 1
print(dictionary) 
#input: Hello World -> Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
