#Python program to add all the array elements using the built-in function
lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)
print("Sum:", sum(lst))
