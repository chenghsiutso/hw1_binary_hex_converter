# 設計一個輸入為10進位，輸出為二進位與16進位數字的程式。
while True:
    input_value = input("Please input a decimal number (range is 0-255) : ('q' to quit) ")
    if input_value == 'q':
        break

    # Check whether the input value is digit and in the range between 0 and 255.
    invalid_input_flag = 0
    if not input_value.isdigit():
        invalid_input_flag = 1
    else:
        decimal_number = int(input_value)
        if decimal_number > 255:
            invalid_input_flag = 1

    if invalid_input_flag:
        print("Invalid input! Your input value is out of range.")
        continue

    carry_digit = 8
    binary_string = ""
    hex_result = 0
    hex_string = ""
    
    # Compare decimal number to n power of base 2 to get each bit number where n is from 7 to 0 decrementally.
    # For example, if decimal number is 255 which is greater than 7 power of base 2, 2^7(=128), we can get the
    # 7th bit number is 1. Then, decimal number 255 is subtracted from 2^7(=128) which is 255 - 128 = 127 and
    # continue to process the next bit n(=6) until n=0.
    while carry_digit:
        carry_digit -= 1
        carry_number = pow(2, carry_digit)
        if decimal_number >= carry_number:
            binary_number = 1
    
            # Add up each four bit number to get the hex number
            hex_result += pow(2, carry_digit % 4)
    
            decimal_number -= carry_number
        else:
            binary_number = 0
    
        binary_string += str(binary_number)
    
        # Calculate the hex number by each four bit number
        if carry_digit % 4 == 0:
            if hex_result >= 10:
                # Convert to alphabet when hex number is greater than 9 using ascii number.
                # For example, 10 => A(ascii 65), 11 => B(66), 12 => C(67), 13 => D(68), 14 => E(69), 15 => F(70)
                hex_string += chr(55 + hex_result)
            else:
                hex_string += str(hex_result)
            hex_result = 0
    
    print("binary number is %s" % binary_string)
    print("hex number is %s" % hex_string)
