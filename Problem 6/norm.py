"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
"""

def norm():
    # Write your code here
    num_values = int(input())
    values = []

    for _ in range(num_values):
        value = float(input())
        values.append(value)

    max_value = max(values)

    for value in values:
        normalized_value = value / max_value
        print(f'{normalized_value:.2f}')

if __name__ == "__main__":
    norm()