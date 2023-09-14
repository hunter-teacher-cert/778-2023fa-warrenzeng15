# Chapter 5 Excercises
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: 
# consulted: 

#5.1
import time

current_time = time.time()

# isolate the seconds for today
seconds_today = current_time % (60 * 60 * 24) #multiply by 60 for minutes, again for hours, 24 for days. we mod the seconds to end up with just the seconds of today
                                              
hour = int(seconds_today // (60*60)) #divide by 60 * 60, hours and minutes
minute = int(seconds_today % (60*60) // 60) #mod (60*60) "removes" the hours from the seconds and we are left with minutes
second = int(seconds_today % 60) #mod 60 gives us the seconds count

days_since_epoch = int(current_time / (60 * 60 * 24)) #just need to divide the seconds into number of days


print(current_time)
print(seconds_today)
print("Time of day:",hour,":", minute,":",second)
print("Days since epoch:", days_since_epoch)


#5.2

def check_fermat(a,b,c,n):
    if (n < 3):
        print("Choose a value for N that is greater than 2")
    else:
        if (((a^n) + (b^n)) == (c^n)):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")

def user_prompt():
    a = int(input("Choose a number for a:"))
    b = int(input("Choose a number for b:"))
    c = int(input("Choose a number for c:"))
    n = int(input("Choose a number for n:"))

    check_fermat(a,b,c,n)

#user_prompt()



#5.3
def is_triangle(a,b,c):
    if (c>(a+b) or b>(a+c) or a>(b+c)):
        print("No")
    else:
        print("Yes")


def ask_triangle():
    a = int(input("Choose the length for a:"))
    b = int(input("Choose the length for b:"))
    c = int(input("Choose the length for c:"))

    is_triangle(a,b,c)

ask_triangle()



#5.4

# it outputs 0, 3, 5 , and then 6, each on individual lines
# since it's recursively called, the print order is the opposite, starting with 6

# stack diagram:

# recurse|   n = 0   s = 6      #base case, where n == 0
# recurse|   n = 1   s = 5
# recurse|   n = 2   s = 3
# recurse|   n = 3   s = 0

# 1. If you called the function as: recurse(-1,0),
# the function would never reach the base case (0) and will continue to 
# recursively run. Eventually you will hit a stack overflow error

# 2.
"""
Recurse is a fucntion that adds the sum of all numbers leading up to 
integer n, printing out each subsequent step. 

n is the "target" integer, and s is the sum -- the sum begins with integer n, then recursively adds
n-1 to the sum until n reaches 0. 

"""




#5.5

#The draw function is called recursively and is repeating many of the same steps.
#The result should be some sort of fractal image drawn by the turtle

