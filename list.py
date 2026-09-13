numbers=list(map(int,input("Enter numbers separated by space:").split()))
print("Original list:", numbers)
search=int(input("Enter number to search:"))
if search in numbers:
    print(search, "is present in the list")
else:
    print(search, "is not present in the list")
old=int(input("Enter number to update:"))
new=int(input("Enter new number:"))
if old in numbers:
    index=numbers.index(old)
    numbers[index]=new
    print("Updated list:", numbers)
else:
    print(old, "is not present in the list")
even_numbers=[x for x in numbers if x%2==0]
print("Even numbers in the list:", even_numbers)
element=int(input("Enter number to add to the list:"))
numbers.append(element)
print("List after adding",numbers)
element=int(input("Enter number to remove from the list:"))
if element in numbers:
    numbers.remove(element)
    print("List after removing", numbers)
else:
    print(element, "is not present in the list")
numbers.sort()
print("Sorted list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)