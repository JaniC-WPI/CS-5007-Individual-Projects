# This function contains code that the program executes when it is first started

def main():
    print("Hello World")

"""
this code calls the main function to get everything started. The condition in this 
"if statement" evalutes to True when the module is executed by the Interpreter, but
not when it is imported into another module.
"""

if __name__ == "__main__":
    main()

# Print the value __main__ referenced by __name__ which is a built-in variable in Python

print(__name__)
