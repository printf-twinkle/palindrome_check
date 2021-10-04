word = input("Enter the word to check palindrome: ") //no integers or special characters are allowed.

if word == word[::-1]:
   print("word is palindrome!")
else:  
   print("word is not palindrome")
