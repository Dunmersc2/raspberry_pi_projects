# This function computes the factor of the number inputted
def print_factors(x):
    print("The factors of",x," are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = int(input("Please enter an interger:"))
print_factors(num)