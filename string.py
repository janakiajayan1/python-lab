text=input("Enter a string:")
old=input("Enter character to replace:")
new=input("Enter replacement character:")
print("The replaced string is:", text.replace(old,new))
print("Reversed string is:", text[::-1])
if text==text[::-1]:
    print("The string is a palindrome")
else:
    print("Character frequency:")
for char in set(text):
    print(char, ":", text.count(char))
words=text.split()
print("Number of words in the string:", len(words))