#Create a set using curly baskets
from enum import unique

#my_set = {1,2,3}

#print(my_set)

#Creating a set from a list using the set() function
#my_set = ([4,5,6])
#print(my_set)

#Create an empty set using the set() function
#my_set = set()
#print(my_set)

#my_set = {1,1,2,3,3,4,5,3,2,3}
#print(my_set) #Set will automaticlly remove duplicates


#############


set1 = {1,2,3}
set2 = {3,4,5}

#Union between set1 and set2 using union() method

union_method = set1.union(set2)

#Compute an union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method:" , union_method)
print("Union of seet1 and set2 using operator", union_operator)

#Compute intersection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#Computing intersection between seet1 and set2 using & operator

intersection_operator= set1 & set2

print("Intersection of set1 and set2 using the intersection method", intersection_method)
print("Intersection of set1 and set2 using the intersection operator", intersection_operator)

#Computing the elements that are unique to set1 using the difference method
difference_method = set1.difference(set2)

#computing elements that are uniqu to set1 using the - operator
difference_operator = set1 - set2

print("Difference of set1 and set2 using the difference method", difference_method)
print("Difference of set1 and set2 using the difference operator", difference_operator)

#Computing the elements that are in set1 and in set2 but not in their intersection
symmetric_difference_method = set1.symmetric_difference(set2)

#Computing the elements that are in set1 and in set2 but not in their intersection using the ^ operator
symmetric_difference_operator = set1 ^ set2

print('Symmetric difference of set1 and set2 using the symmetric difference method:', symmetric_difference_method)
print('Symmetric difference of set1 and set2 using the symmetric difference operator:', symmetric_difference_operator)


#SET METHODS

#Create a set

my_set = {1,2,3}

#Add number 6 at the end of the set

my_set.add(7) #add method

#remove number 3 from my set

my_set.remove(3) #remove method

#Removing 8 from the set without throwing and error if 8 in snow on the set

my_set.discard(8)
print(my_set)

#Removing all the numbers from the set
my_set.clear()

print(my_set)


#Remove duplications from a list

#Create a list that contains duplications
my_list = [1,2,2,2,3,4,4,4,5,6]

#Convert this list to a set to remove duplications
unique_set =set(my_list)

print(unique_set)

#Convert this set to a list
unique_list = list(unique_set)
print(unique_list)


#Checking for common elements

blertas_interest = {"music", "movies", "travler"}
drilonis_interests = {"movies", "games", "skiing"}

common_intrests = blertas_interest.intersection(drilonis_intrests)
print(common_intrests)

#IN operator

colors = {"red", "purple", "yellow", "blue"}
color = "green"
print(color in colors)


