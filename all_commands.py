class commands:
    def __init__(self, name, operator, description):
        self.name = name
        self.operator = operator
        self.description = description

off = commands("off", "", "Turns off the calculator!")

add = commands("add", "+", "Add two numbers!")

subtract = commands("sub", "-", "Subtract the second number from the first!")

multiply = commands("mult", "*", "Multiplies two numbers with each other!")

list_of_commands = [off, add, subtract, multiply]