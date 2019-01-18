def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # bonus()

# Print -20 to and including 50.
# Use any loop you want.
def problem1():
    for problem1 in range(-20, 51):
        print(problem1)

# Create a loop that prints even numbers from 0 to and including 20.
def problem2():
    for problem2 in range(0, 21, 2):
        print(problem2)

# Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
def problem3():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    num3 = int(input("Enter a number"))
    numaverage = ((num1 + num2 + num3)//3)
    print("The average of ", num1, num2, num3, "is", numaverage)

# Password Checker - Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.
def problem4():
    password1 = input("Enter your password")
    while True:
        password2 = input("Confirm your password")
        if password1 == password2:
            break
        elif password1 == "q":
            break
        elif password2 == "q":
            break

# Prompt the User for the ending value (e.g. 100)
# Your code should start at 1 and then iterate each number up to the ending value entered by the user
# If the current number is evenly divisible by 3 you should print FIZZ and the number
# If the current number is evenly divisible by 5 you should print BUZZ and the number
# If the current number is evenly divisible by both 3 and 5 you should print FIZZBUZZ and the number to the screen
# Otherwise, just print the original number
def bonus():
    num = int(input("Enter an ending number!"))
    for eachElement in range(1, num+1):
        if (eachElement % 3 == 0) and (eachElement % 5 == 0):
            print(eachElement, "FIZZBUZZ")
        elif eachElement%3 == 0:
            print(eachElement, "FIZZ")
        elif eachElement%5 == 0:
            print(eachElement, "BUZZ")
        else:
            print(eachElement)

if __name__ == '__main__':
    main()