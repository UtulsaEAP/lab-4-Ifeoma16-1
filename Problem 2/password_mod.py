"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    word = word.replace('i', '1')
    word = word.replace('a', '@')
    word = word.replace('m', 'M')
    word = word.replace('B', '8')
    word = word.replace('s', '$')

    password = word + '!'
    print(password)

if __name__ == "__main__":
    password_mod()