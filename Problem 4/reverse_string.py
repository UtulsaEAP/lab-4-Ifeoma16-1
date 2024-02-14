"""
Complete the following python code to reverse the string entered by the user.

Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
"""

def reverse_string():
    # YOUR CODE HERE
    while True:
        user_string = str(input())
        if user_string == 'Done' or user_string == 'done' or user_string == 'd':
            return 1
        else:
            reversed_string = user_string[::-1]
            print(reversed_string)
    

if __name__ == "__main__":
    reverse_string()