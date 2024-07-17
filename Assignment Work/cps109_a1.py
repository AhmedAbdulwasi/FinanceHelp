"""
1) Come up with a problem you wish to solve and describe it in a paragraph or two. Your
description should be technical and precise – no vague handwaving. The clearer the
problem description, the easier it will be to solve in Python. (Those of you in the computer science program will take a software engineering course in
2nd year and learn all about the art of defining requirements and specifications)


Intro: One big change that I noticed ever since I became a university student is finance.
With the addition of tuitions and loans as an expense, it became more and more frighenting not only to
fund your education but also your everyday needs such as transportation, food, self-care and much more.
It becomes a bit difficult to track how much you are spending or how much you are earning or if you can
afford a specific item etc. 

Problem: FINANCE CALCULATOR! What if there was a program that tells you your monthly finance. This consist of
the total income and expense that you have, what you are able to afford, how much should you save up
based on your unique financial situation. It also generates you a text file that contains 
all outputs that you received in this program. This program must answer all the features that 
were mentioned in this problem as well as an additional function of your choice (e.g. resources, etc.).

"""

'''
2) Write a Python program called cps109_a1.py that solves the problem you defined in part
1. At minimum, your program must meet the following requirements. Feel free to exceed
these requirements – this is only a lower bound:
a. In a comment at the top of your source file you should paste the problem description
you wrote in part 1. DONE

b. At least 20 lines of meaningful comments (not including the problem description) and
60 lines of code (not including whitespace). 
Note: The 60-line requirement is to prevent your program from being too
simple/trivial. Do not write inefficient code or needlessly expand your syntax for the
sake of hitting 60 lines. You’re all well versed in padding high school essays I’m sure,
but do not extend this habit to programming. Writing succinct, readable, efficient
code is your prime directive. If you’re having trouble hitting 60 lines, you should
expand the scope of your problem. DONE


c. Your program must demonstrate each of the following Python elements at least once:
• Variable declarations and assignments DONE
• Arithmetic expressions (can include function calls) DONE
• Use of if/elif/else statement DONE
• Use of sequence types and their operations (strings, lists, tuples) DONE
• Use of a for loop for sequence iteration (a list comprehension works here also) DONE
• Use of a while loop for general iteration (driven by a condition) DONE
• A user-defined function for solving some meaningful subproblem. DONE
• Print statements for displaying output (user input is allowed, but not required) DONE
• Read input from a file, write output to a file. DONE
d. Finally, your program must of course solve the problem you defined in part 1 DONE
'''
import os,sys # I use os to stop the program and sys to clear the screen.


fl = 0.00 # Initialize because it will be used to get the float of income and expense.
def get_budget(filename):
    with open(filename,'r') as file: 
        line = file.readlines()
        values = [lines.strip() for lines in line] # we open the file and put it in a list without spaces.
    file.close() # Close the file. Pretty important as to not have future problems.
    return values

def get_income(values): # First sub-problem: Get the income ONLY.
    
    income = []
    # Using for loop for general iteration
    for inc in range(1,len(values)):
        if values[inc] == 'expense':
            break # Break the function so that we don't include expense as well.
        else:
            fl = float(values[inc]) # We make sure it's converted to FLOAT as the whole project is float.
            income.append(fl) # We add it to our new list called income.
    
    return income
def get_expense(values): # Second sub-problem: Get the expense ONLY.
    
    expense = []
    values.reverse() # I added the reverse function to add more python built-in functions to my project.
    # Using for loop for general iteration
    for exp in range(len(values)):
        if values[exp] == 'expense': # Since its reversed, we stop at expense. We don't want to count income.
            break
        else:
            fl = float(values[exp])
            expense.append(fl) # We add it to our new list called expense.
    return expense
def how_much_money(income,expense):
    file = open("cps109_a1_output.txt",'a') # Tip: TA said that its faster to append then to create an entire new txt.
    income_sum = sum(income) # I could've used For loop but it would just not be efficent compared to sum().
    expense_sum = sum(expense)
    summ = income_sum - expense_sum # Using the sum function, we can calculate the total amount of money we have.
    
    file.write("\n How Much Money?") # Here we write whatever we outputted.
    file.write("\n")
    file.write(f"\n Your revenue/income is: ${income_sum}. ")
    file.write(f"\n And your expense will be: ${expense_sum}")
    print(f"Your revenue/income is: ${income_sum}. ")
    print(f"And your expense will be: ${expense_sum}")
    print(f"This means you have: ${summ}")
    if (expense_sum/income_sum) >= 0.50: # It's been said (https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp#:~:text=Key%20Takeaways,else%20that%20you%20might%20want.)
        # 50-30-20 is the recommended budget. 50% should be used for expense, 30% for want, 20% for save up.
        print(f"You should slow down with your spending as its close to your income, ${summ}.")
        file.write(f"\n You should slow down with your spending as its close to your income, ${summ}.")
        file.write("\n ---------------")
        file.close()
        input("Type to continue ") # We give them sometime for the user to see the output.
        os.system('cls') # This will clear the console screen.
        main_page() # We go back to our main_page by calling the function.
    else:
        print(f"Great job, not that much expenses. The total is ${summ}!")
        file.write(f"\n Great job, not that much expenses. The total is ${summ}!")
        file.write("\n ---------------")
        file.close()
        input("Type to continue ")
        os.system('cls') 
        main_page()
    
    
def should_i_buy(income,expense):
    count = int(input("How many items do you want to buy? ")) # How many items does the user want to buy. We then use it for general while loop.
    file = open("cps109_a1_output.txt","a")
    file.write("\n Should I buy?")
    file.write("\n")
    prices = []
    # Using while loop for general iteration.
    while count > 0: # You can use For loop but I used while to diversify my code.
        x1 = float(input(f"Enter the price for item {count} in two decimals: "))
        count -= 1 # Important to decrement to stop the while loop once at 0.
        prices.append(x1)
    file.write(f"\n The prices for the {len(prices)} item(s) are/is: {prices}")
    if ((sum(prices)+sum(expense))/sum(income)) >= 0.50:
        
        file.write("\n Oh oh. I suggest that drop some/all of the item(s) you are buying.")
        file.write("\n ---------------")
        file.close()
        print("Oh oh. I suggest that drop some/all of the item(s) you are buying.")
        input("Type to continue ")
        os.system('cls')
        main_page()
    else:
        file.write("\n It's within the budget!")
        file.write("\n ---------------")
        file.close()
        print("It's within the budget!")
        input("Type to continue ")
        os.system('cls')
        main_page()
        
def save_up(income,expense):
    file = open("cps109_a1_output.txt",'a')
    user_save,user_want,user_need = 0.2,0.3,0.5 # Using the 50-30-20 rule to plan how your budget should be.
    total = sum(income) - sum(expense)
    total_save = user_save * total
    total_want = user_want * total
    total_need = user_need * total
    file.write("\n Save Up!")
    file.write("\n")
    file.write(f"\n With the amount of money you have being ${total},")
    file.write(f"\n You should save ${round(total_save,2)} (20% of your money).")
    file.write(f"\n You should use ${round(total_want,2)} for your wants (30% of your money).")
    file.write(f"\n You should use ${round(total_need,2)} for your needs (50% of your money).")
    print(f"With the amount of money you have being ${total},")
    print(f"You should save ${round(total_save,2)} (20% of your money).")
    print(f"You should use ${round(total_want,2)} for your wants (30% of your money).")
    print(f"You should use ${round(total_need,2)} for your needs (50% of your money).")
    print('\n')
    file.write("\n ---------------")
    file.close()
    input("Type to continue ")
    os.system('cls')
    main_page()
        
def resources(income,expense): # Useful resources for financial literacy resources.
    file = open("cps109_a1_output.txt",'a')
    file.write("\n Helpful resources!")
    file.write("\n")
    file.write("\n 1) https://www.torontomu.ca/student-financial-assistance/about/")
    file.write("\n 2) https://www.lib.sfu.ca/help/research-assistance/subject/business/personal-finance")
    file.write("\n 3) https://uwaterloo.ca/school-of-accounting-and-finance/financial-literacy-resources")
    file.write("\n 4) https://www.otffeo.on.ca/en/resources/useful-links/financial-literacy/")
    
    print("Helpful resources!")
    print("1) https://www.torontomu.ca/student-financial-assistance/about/")
    print("2) https://www.lib.sfu.ca/help/research-assistance/subject/business/personal-finance")
    print("3) https://uwaterloo.ca/school-of-accounting-and-finance/financial-literacy-resources")
    print("4) https://www.otffeo.on.ca/en/resources/useful-links/financial-literacy/")
    file.close()
    input("Type to continue ")
    os.system('cls')
    main_page()
    
def exiting(income,expense):
    sys.exit() # sys will be used to close/stop the program
    
def main_page(): # We defined it as a function as we would like to return to this screen to pick other options.
    os.system('cls')
    print("Welcome to your Monthly Finance Calculator/Planner!")
    print("To start, pick one of the options below that you would like to use.")
    print("\n")
    print("1) How much money I have? ")
    print("2) Should I buy this? ")
    print("3) How much should I save up? ")
    print("4) Resources.")
    print("5) Exit.")
    options = { # Defined it as dictionary as it will be helpful to use to call functions through values.
        1: how_much_money,
        2: should_i_buy,
        3: save_up,
        4: resources,
        5: exiting
        
        }
    user_input = int(input("Enter the number: "))
    if user_input in options:
        os.system('cls')
        print(options[user_input](incomee,expensee))
    else:
        # while loop for general iteration.
        while user_input not in options: # The user must choose between the options or it will "while" loop forever.
            print("Invalid Input.")
            user_input = int(input("Enter the number: "))
        if user_input in options:
            os.system('cls')
            print(options[user_input](incomee,expensee)) #since all of the functions use income and expense, we can just include them there.
    

if __name__ == "__main__":
    incomee = get_income(get_budget("cps109_a1_input.txt")) # Calculate income
    expensee = get_expense(get_budget("cps109_a1_input.txt")) # Calculate expense
    main_page()  # Calling the main function to start the program
                
    
        

