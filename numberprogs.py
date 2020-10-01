n=int(input("Enter the no of students in class:"))  
dict1={}
for i in range(n):
    key=input("Name of the student")
    value=int(input("Enter the %age"))
    dict1[key]=value
lst=dict1.values()  

print(lst)

