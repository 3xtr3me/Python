#Challenge:
#Write a Python program to check whether a given number is a Palindrome or not.
Number = int(input('Enter a number: '))
if(Number == int(str(Number)[::-1])): #[::-1] is a slicing method used in list also can be used in for loops (start_number,end_number,step)
  print('The Number ' +str(Number) +' is Palindrome')
  print(Number)
else:
  print('The Number ' +str(Number) +' is not a Palindrome')
