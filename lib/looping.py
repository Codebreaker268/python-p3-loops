#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x=11
    while x > 0:
        x-=1
        print(x)
    print("Happy New Year!")    

    
        
    

def square_integers(int_list):
    squares=[]
    for ints in int_list:
        squares.append(ints*ints)
        # print(squares)
    return squares    

        
    
    

def fizzbuzz():
    x=0
    while x<= 99:
        x+=1
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0:
            print("Fizz")   
        elif x%5==0:
            print("Buzz") 
        else:print(x)        
        

    
