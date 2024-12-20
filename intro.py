# print("hello world")
# a='satish murukutla'
# print(a[2])
# print(a.count('s'))
# print(a.endswith('h'))
# print(a.join('ss'))

#slicing string
text='satish'  ## print ati from satish

## formula 

# text[start:stop(-1):1(default)]

print(text[-3:-6:-1])

print(text[1:5:2])   # it will give ai 

print(text[-4:-1:1]) 

print(text[::-1])  ## reverse the string 
print(text[::1])   ## to print the same

## list_intro

my_family_members=['dad','mom','wife','brother']
print(my_family_members)  ## sol: ['dad', 'mom', 'wife', 'brother']
print(type(my_family_members))  ##<class 'list'>
print(my_family_members[2])  ##wife
software_employee=['satish',23,True,['dad','mom','wife','brother']]
print(software_employee[3][1])  ##mom
## i want to print only t from brother
print(software_employee[3][3][3]) ## t  using +ve indexing
print(software_employee[-1][3][3]) ## t  using -ve indexing

## list 
listx=[1,2,3,4,5]
print(listx)
listx.append(6)
print(listx)
## pop will basically will delete the values ,it gove with LIFO order 
listx=[1,2,3,4,5]
listx.pop()
print(listx)

for i in listx :
    print(i)