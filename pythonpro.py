# defined function to create acronym
def fxn(string):
    # add first letter
    output = string[0]

    # iterate over string
    for i in range(1, len(string)):
        if string[i - 1] == ' ':
            # add letter next to space
            output += string[i]

    # uppercase output
    output = output.upper()
    return output

# input string
input = input("Enter a String sepreated by space: ")

# output acronym
print(fxn(input))
