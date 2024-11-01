def checkOddEven(x):
    if x % 2 == 0:  # Check if the number is even
        print("Even")  # Print "Even" if true
        return 
    else:
        print("Odd")  # Print "Odd" if false
        return 

# Get user input, convert it to an integer, and check if it is odd or even
checkOddEven(int(input("Enter a number: ")))  # Prompt the user for input
