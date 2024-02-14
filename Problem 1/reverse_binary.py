"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binary_str = ""

    while user_num > 0:
        binary_str += str(user_num % 2)
        user_num //= 2

    print(binary_str)

if __name__ == "__main__":
    reverse_binary()