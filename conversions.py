def numConversion(decNum, base):
    result = []
    count = 0
    while decNum > 0:
        remainder = decNum % base
        if remainder > 9:
            # Map values greater than 9 to corresponding letters
            result.insert(count, chr(remainder + 55))  # 55 is ASCII offset for A
        else:
            result.insert(count, remainder)
        decNum = decNum // base
        count += 1
    result.reverse()
    for i in range(0, len(result)):
        print(result[i], end=" ")
    return result

exit_flag = False
while not exit_flag:
    inputOne_str = input("Please enter a value you would like to convert; Decimal value (type 'exit' to quit): ")
    if inputOne_str.lower() == 'exit':
        exit_flag = True
    else:
        while not inputOne_str.isdigit():
            inputOne_str = input("Please try again.\nSelect a valid value (value>0):")
        inputOne = int(inputOne_str)

        inputTwo_str = input("Please enter what base you would like the decimal number to be in; Base value: ")
        while not inputTwo_str.isdigit() or int(inputTwo_str) < 2 or int(inputTwo_str) > 16:
            inputTwo_str = input("Please try again.\nSelect a valid value, (2-16):")
        inputTwo = int(inputTwo_str)

        numConversion(inputOne, inputTwo)
        print()
