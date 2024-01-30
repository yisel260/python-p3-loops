#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0 :
       print(i)
       i -= 1
    if i == 0:
        print("Happy New Year!")
 
def square_integers(int_list):
    squared_numbers = [num * num for num in int_list]
    return squared_numbers 
    

def fizzbuzz():
    i = 1
    while i <=100 :
         if i%3 == 0 and i%5==0:
            print ("FizzBuzz")
            i += 1
         elif i%5 == 0 :
            print ("Buzz")
            i += 1
         elif i%3==0:
            print ("Fizz")
            i += 1
         else:
            print( i)     
            i += 1
    
