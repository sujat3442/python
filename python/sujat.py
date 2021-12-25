A=int(input("Enter the number: "))
for x in range(1500,2700):
    if A%7==0 and A%5==0:
        print("the number is divisible by 7 and multiple of 5.")
        break
    else:
        print("Error")
        break



#2. Write a Python program to get the smallest number from a list.

A=[1,2,3,0,4,5]
print(min(A))







# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

A=["Abas","Abd","Aba","Asa"]
B=0

for word in A:
    if len(word)>1 and word[0]==word[-1]:
        B+=1
print(B)






#4. Write a Python program to check a list is empty or not.

A=[1,2]
if len(A)!=0:
    print("Not Empty.")
else: 
    print("Empty.")






#5. Write a Python program to print a specified list after removing the 4th elements.
A=[1,2,3,4,5,6,7,8,9]
print(A)
del A[3]
print(A)

#Alternative
A=[1,2,3,4,5,6,7,8,9]
print(A)
A.pop(3)
print(A)




#6. Write a Python program to select an item randomly from a list.


import random

A=range(20)
print(random.choice(A))




#7. Write a Python program to add an item in a tuple.
tuple_A=(1,2,3,4)
print(tuple_A)
List_A=list(tuple_A)
print(List_A)
#Append  Add number from last
List_A.append(5)
#insert add item to  list in required index
List_A.insert(5,"suju")
print(List_A)
update_tuple=tuple(List_A)
print(update_tuple)





#8. Write a Python program to convert a tuple to a string. 
S=("S","U","J")
st = ''.join(S)
print(st)






#9. Write a Python program to create the colon of a tuple.
from copy import deepcopy

Sujat = ("HELLO", 5, [], True) 
print(Sujat)

Sujat_colon = deepcopy(Sujat)
print(Sujat_colon)





#10. Write a Python program to iteration over sets.
A={1,2,3,4,5,6}
for i in A:
    print(i)






#11. Write a Python program to remove an item from a set if it is present in the set.
A={1,2,3,4,5,6,"Sujat","Poudel"}
A.remove("Sujat")
print(A)
A.remove("Poudel")
print(A)





#12. Write a Python program to update list element in a set.


A={1,2,3,4,5,6}
print(A)
B={7,8,9,10}
print(B)

# .update is used to update set
A.update(B)
print(A)





#13. Write a Python script to concatenate following dictionaries to create a new one.

dic1= {1:"Sujat", 2:"Poudel"}
dic2= {3:"Chhetri", 4:"Gopal"} 
dic3= {5:"Softwarica",6:"Acadamic"}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)

print(dic4)






#14. Write a Python script to check if a given key already exists in a dictionary.
A={1: 'Sujat', 2: 'Poudel', 3: 'Chhetri', 4: 'Gopal', 5: 'Softwarica', 6: 'Acadamic',7:"Requirement"}
B=int(input("enter the number: "))
if B in A:
    print("present")
else:
    print("Not Present")






