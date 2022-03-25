###Special Note:  
#       All the functions work when run within their OWN
#       file. However, when I imported functions 2-5 INDIVIDUALLY from this
#       module (e.g., from ce_prework_module import first_odds), 
#       the hello_name function always ran first before
#       the (2-5) imported function did.  Could not solve.


#Question 1:  
#   Write a function to print "hello_USERNAME!"
#   Function call:  hello_name("")
#   Only way I could get this to work was to use 
#        an empty string as the argument in the call.
#        Otherwise, got missing argument error message
#            when "q" was input.

def hello_name(user_name):
    
    """Print "hello_USERNAME" based on user input"""
    message = f"hello_{user_name.upper()}!"
    return message

while True:
    print(f'\nPlease enter "q" when you are finished.')
    USERNAME = input("What is your name? ")
    if USERNAME == 'q':
        print("\nThank you for sharing your name!")
        break

    complete_message = hello_name(USERNAME)
    print(f"\n{complete_message}")
        


#Question 2:  
#   Write a function that prints
#       the odd numbers from 1-100
#   Function call:  first_odds()

def first_odds():
    
    """Prints odd numbers from 1 to 100"""
    for n in range(0,101):
        if n % 2 != 0:
            print(n)
            continue


#Question 3:  
#   Write a function that returns max number
#       in any list
#   Function call: max_num_in_list([#list of numbers#])

def max_num_in_list(a_list):
    
    """Prints max number in a list"""
    answer = print(max(a_list))

    return answer


#Question 4:  
#   Function that returns whether year is a leap year
#   Function Call:  print(is_leap_year(##any year##))

def is_leap_year(a_year):

    """Return True if leap year; False if not leap year"""
    if a_year % 100 == 0 and a_year % 400 == 0:
        a_year = True
    elif a_year % 100 != 0 and a_year % 4 == 0:
        a_year = True
    else:
        a_year = False
    return a_year


#Question 5:  
#   Return True if all numbers in a list are consecutive
#   Function Call:  print(is_consecutive([##list of numbers##]))

def is_consecutive(a_list):
    
    """Return True if numbers in list are consecutive; False if not"""
    while len(a_list) >= 2:
        if a_list[0] + 1 == a_list[1]:
            list = True
            a_list.pop(0)
        
        else: 
            list = False
            break 

    return(list)               

#Question 1:  
#   Write a function to print "hello_USERNAME!"
#   Function call:  hello_name("")
#   Only way I could get this to work was to use 
#        an empty string as the argument in the call.
#        Otherwise, got missing argument error message
#            when "q" was input.

def hello_name(user_name):
    
    """Print "hello_USERNAME" based on user input"""
    message = f"hello_{user_name.upper()}!"
    return message

while True:
    print(f'\nPlease enter "q" when you are finished.')
    USERNAME = input("What is your name? ")
    if USERNAME == 'q':
        print("\nThank you for sharing your name!")
        break

    complete_message = hello_name(USERNAME)
    print(f"\n{complete_message}")