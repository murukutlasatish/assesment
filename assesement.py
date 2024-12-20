##assesment for finding biggest of three numbers

a=int(input("enter the a value : "))
b=int(input("enter the b value : "))
c=int(input("enter the b value : "))


def biggest_of_three_numbers(a,b,c):
    if a > b  and a > c:
        return a
    elif a == b and a == c:
        return("equal")
    
    elif b > c:
        return b

    elif b ==a and b == c:

        return ("equal")
    else :
        return c
        
    
biggest=biggest_of_three_numbers(a,b,c)

print("the biggest number is ",biggest)