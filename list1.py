#List Comprehension
student=["vishal", "manav", "kishan", "hardik", "pooja"]
newlist = []
for x in student:
  if "k" in x:
    newlist.append(x)
print(newlist) 

#Creating a list of capital letters from a list
student=["vishal", "manav", "kishan", "hardik", "pooja"]
newlist = [x.upper() for x in student]
print(newlist)

##Filter even numbers in a list:
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumber=[x for x in numbers if x % 2 == 0]
#print(x)
print(evennumber)

##Generating a list of unique numbers
numbers = [1, 2, 3, 2, 4, 3, 5, 4, 6]
uniquenumbers = list(set(numbers))
print(uniquenumbers)