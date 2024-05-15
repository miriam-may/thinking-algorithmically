def n_of_ones(n):
    # return value
    count = 0
    # create a string so I can reverse the numnber
    string_n = str(n)
    # reverse the number
    reversed = ""
    for i in range(len(string_n)):
        reversed += string_n[(len(string_n)-1) - i]

    # this is needed so I can count the number of 10s I need to add up
    string_index = 0
    # this is needed for figuring out where to "stop" when the number starts with 1
    so_far = 0
    # keep a record of the power
    power = 1
    while n > 0:
        # what digit are we working on
        digit_char = reversed[string_index]
        string_index += 1
        digit = int(digit_char)
        # edge case - 10s and digit is a 1
        if (power == 10 and digit == 1):
            count += (string_index - 1) * (power // 10) + (so_far) + 1
        # greater than 1 - no problem, obey the rule for 10s
        elif(power == 10 and digit > 1):  
            count += (power + (digit * power//10))
        # edge case, 100s and digit is a 1
        elif(power == 100 and digit == 1):
            count += (power//10 + (digit * power//10)) + so_far + 1
        # no problem, obey the rule for any power above 10
        elif(power > 10 and digit > 1):
            count += digit * ((string_index - 1) * power//10) + power
        # edge case again!
        elif(power > 100 and digit == 1):
            count += digit * ((string_index - 2) * power//10) + power//10 + so_far + 1
        # this is for just 0-9
        elif (digit >=1):
            count += 1 
        # keep a record of where I'm at
        so_far += digit * power
        n = n // 10
        # up the power
        power *= 10
        
        
    return count


nber = input("please enter an integer number\n")
print(n_of_ones(int(nber)))