listx=[1,2,3,4,5]

for i in listx:
    print(i)

for letter in "satish":
    print (letter)   ## satish


for letter in "satish":
    print (letter[0])   ## satish

# for letter in "satish":
#     print (letter[1])   ## error in flor loop here index will have temporary memory and alway 0 index

print ("================")

cars = ["audi",'benz',"merce","rr"]

for car in cars:
    print(car)   
## this will give below output
# benz
# merce
# rr
print("###########")
## want to print inly audi and benz from cars list

for car in cars:
    print(car)
    if car == "merce":
        break

### using continue  -- this will skip the iteration of the loop and continue to the new index

fruits=["bananan","apple","orange"]
for i in fruits:
    if i == "apple":
        continue
    print(i)  ## this will print only banana and orange

## dictionary

family={
    "name":"satish",
    "age":"30",
    "eductation":"pgdm"
}

for (k,v)in family.items():
    print(k,v)

#This will print as below
# name satish
# age 30
# eductation pgdm

