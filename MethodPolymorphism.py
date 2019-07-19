# Method Polymorphism
# Method Overloading
# Creating methods that behave differently depending on parameters passed to them

# print('Print can take 1 parameter')
# print('Or it can take many', 'and it will still work,', 'it', 'can', 'take', 'a', 'lot', 'of', 'arguments')
#
# # Same with + it can either take ints and combine them
# print(2 + 2)
# # Or strings and concatenate them
# print('Concat ' + 'enation')


class Calculator:
    def addition(self, num1, num2, num3=0, num4=0):
        return num1 + num2 + num3 + num4

    def subtraction(self, num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        if num1.isnumeric() is True and num2.isnumeric() is True:
            return (int(num1) - int(num2))
        else:
            return 'Please Give Numbers!!!!'


my_calc = Calculator()


print(my_calc.addition(1, 2))
print(my_calc.addition(1, 2, 3, 4))

#
# print(my_calc.subtraction(10, 5))
# print(my_calc.subtraction('10', '5'))
# print(my_calc.subtraction('Wasp', 'Football'))