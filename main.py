def roman_to_int(roman_numerals):
    roman_values = {'T': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for i in reversed(roman_numerals):
        current_value = roman_values[i]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

    return total

roman_numerals = input("Enter the roman numerals: ")
result = roman_to_int(roman_numerals)
print(roman_numerals, "is", result)

