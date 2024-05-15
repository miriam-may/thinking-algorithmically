# Helper function to reduce duplicated code
def helper(power, num, characters, divisor, char):
    # create string to return
    string = ""
    # make sure the digit has all its zeros
    digit = num * power
    # divisor for the modulo operation
    divisor = divisor // power
    # create the repeated characters (like the 2 Is for 7)
    if(num < 4):
        default = str(num * characters[power])
    elif(num < 10):
        default = str((num % divisor) * characters[power])

    # if the number is in the dictionary, no additional characters need to be added
    if characters.get(digit):
        string += (characters[digit])
    # if the digit is greater than (5, 50, 500), a V or L or D need to be added first
    elif num > divisor:
        string += (char + default)
    # if not, just the repeated characters are needed, e.g. 3 = III
    else:
        string += default
    return string


def roman_numerals_converter(num):
    #create a list to hold the solution
    rn = []

    # Create map/dictionary with string values mapped to number keys
    characters = {1 : 'I',
                  4: 'IV',
                  5 : 'V',
                  9 : 'IX',
                  10 : 'X',
                  40: 'XL',
                  50: 'L',
                  90: 'XC',
                  100: 'C',
                  400: 'CD',
                  500: 'D',
                  900: 'CM',
                  1000: 'M'}
    # How to decompose a number by 10? You can do integer/floor division by powers of 10 to lop off decimal places and
    # find how long the number is, for the first step. But first, reverse the number
    num_string = str(num)
    temp_string = ""
    for i in range(len(num_string)):
        temp_string += num_string[(len(num_string)-1) - i]
    
    length_count = 0
    power = 1
    divisor = 5
    # create a counter
    temp = int(temp_string)
    # while there are still numbers...
    while temp > 0:
        # the current digit in the reversed number
        current = temp_string[length_count]
        # make sure you can do numerical operarations on it
        digit = int(current)
        # call the helper function with the desired arguments
        st = helper(power, digit, characters, divisor, characters[divisor])
        # add to the list of strings at the beginning
        rn.insert(0, st)
        # increment the arguments by powers of ten
        power = power * 10
        divisor = divisor * 10
        # lop off another digit
        temp = temp//10
        # next digit, please
        length_count += 1
      

    # although Roman Numerals don't have spaces, it makes it easier to differentiate the powers of 10
    return " ".join(rn)

# grab an integer
num = input("Please enter an integer number up to 999\n")

# convert the string input to an integer
num = int(num)

# print the returned answer
print(roman_numerals_converter(num))