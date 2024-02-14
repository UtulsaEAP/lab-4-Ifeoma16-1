"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
"""

def inc_5():
    # Write your code here
    first_integer = int(input("Enter first integer: "))
    second_integer = int(input("Enter second integer: "))
    if first_integer <= second_integer:
        current_value = first_integer

        while current_value <= second_integer:
            print(current_value, end=" ")
            current_value += 5
        print() 
    else:
        print("Second integer can't be less than the first.")


if __name__ == '__main__':
    inc_5()