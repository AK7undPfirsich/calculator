import calcs
from all_commands import list_of_commands

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

def control(i):
    for command in list_of_commands:
        if i == command.name:
            return True
    return False

def control_for_numbers(x):
    n = 0
    dot_count = 0
    while n < len(x):
        if x[n] in numbers:
            if x[n] == ".":
                dot_count += 1
            n += 1
        else:
            return False
    if dot_count != 0 and dot_count != 1:
        return False
    return True

def get_op(x):
    for command in list_of_commands:
        if x == command.name:
            return command.operator
    return print("Error")

def calculate():
    instruction = input("Welcome to this little calculator! How can i help you today? (Input 'help' for further instructions) ")
    if instruction == "help":
        for command in list_of_commands:
            print(command.__dict__)
        calculate()
    elif control(instruction) == False:
        print("False Input. Try again or input 'help' for an overview over all possible Inputs.")
    elif instruction == "off":
        return
    else:
        first_number = input("Perfect! Now please input the first number to calculate with: ")
        second_number = input("...And the second number: ")
        if control_for_numbers(first_number) == False or control_for_numbers(second_number) == False:
            print("One of the given numbers is not a number.")
            return
        print("And the result is: ")
        print(eval(f"{float(first_number)} {get_op(instruction)} {float(second_number)}"))

calculate()