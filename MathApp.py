##Atiksh C


import sys, os
from time import sleep
from termcolor import colored, cprint
import random



Num_list = []


# Function to generate numbers and stores in the master List to help with various matematical Operation
def genNum(Num):
    for n in (range(1,Num)):
        Num_list.append(n)
    print("You have Generated below numbers")
    print(Num_list)
    sleep(3)

# Print function list and sleep for 2 seconds before prompts the menu
def prnlst():
    print("Your Master List contains below numbers")
    print(Num_list)
    sleep(3)

# Iterates the Main List, initiate 2 variables and compare each element and store the element in variable if its minimum till it finds the lowest value and maximum value till it
# finds highest value
#By Atiksh Chandra Mohan
def fndMinMax(lst):
    min=lst[0]
    max=lst[0]

    for minele in lst:
        if minele < min: min=minele
    print("Minimum Number =" , min)
    sleep(3)

    for maxele in lst:
        if maxele > max: max=maxele
    print("Maximum Number =" , max)
    sleep(3)



# Iterates the list and push even number to even list and odd numbers to odd list by determing the reminder using module operator
#By 
def prnEvenOdd(list):
    evnlst = [ n for n in list if n % 2 == 0 ]
    print("Your even numbers list")
    print(evnlst)
    print ("\n")
    oddlst=[x for x in list if x % 2 != 0]
    print("Your odd number list")
    print(oddlst)
    sleep(3)


# Function to iterate the list in the reverse order in the increment of -1 till it reach beginning and prints the element
#By 
def reverselist(lst):
    rvrslst = []
    for num in lst[-1:0:-1]:
        rvrslst.append(num)
    print("Numbers in Reverse Order")
    print(rvrslst)
    sleep(3)



#  Calculates the square root of each number in the list and prints the list using list comprehension
#By Atiksh Chandra Mohan
def sqrt(lst):
    sqlist=[ x * x for x in lst]
    print("squre root of each number")
    print(sqlist)
    sleep(3)

# Prompts user to pick number of random number to generate and use random module to return the sample from master list.  Uses loop to generate till user wants
#By Atiksh Chandra Mohan
def pickrandom(lst,num):
    rndlst = []
    while True:
        print(random.sample(lst, num))
        ch = input("Press 'y' to continue or 'N' to exit:  ")
        if ch == 'Y' or ch == 'y':
            continue
        else:
            return False
            break


# Main Program which prompts user with main options and allows to pick an option and based on the "if" condition to execute respective
# function to perform the right operation and uses While loop till user enter exit option
#By Atiksh Chandra Mohan
while True:
    os.system('export TERM=linux')
    os.system('clear')
    cprint(' Math App : By Atiksh C +   ', 'black', 'on_white')
    text = colored('Product Features', 'white', attrs=['reverse', 'blink'])
    print("\n\n\n\n")
    print(' '*50 , text)
    print("\n")

    print(' '*40, "1. Generate numbers")
    print(' '*40, "2. Print Numbers")
    print(' '*40, "3. Find Max and Min Numbers")
    print(' '*40, "4. Print Even and Odd Numbers")
    print(' '*40, "5. Print Numbers in reverse")
    print(' '*40, "6. Square root of number")
    print(' '*40, "7. generate random numbers")
    print(' '*40, "9. To Exit")
    print("\n\n\n")

    esc = chr(27)
    choice = int(input("Enter Your Choice:  ".rjust(60)))

    if choice == 1:
        dgt = int(input("How many Digits to be generated: "))
        genNum(dgt)
    elif choice == 2:
        prnlst()
    elif choice == 3:
        fndMinMax(Num_list)
    elif choice == 4:
        prnEvenOdd(Num_list)
    elif choice == 5:
        reverselist(Num_list)
    elif choice == 6:
        sqrt(Num_list)
    elif choice == 7:
        num = int(input("How many random numbers to generate:  "))
        pickrandom(Num_list,num)
    elif choice == 9:
        print("\n\n")
        print(' '*40, "Thanks for using our app, bye")
        break