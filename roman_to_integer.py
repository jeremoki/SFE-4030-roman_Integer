def roman_to_integer(s):

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in s[::-1]:
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Test cases
test_cases = [
#Single letters
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
#Multiple letters
    ("XI", 11),
    ("IV", 4),
    ("XIV", 14),
    ("III", 3),
#Repetition
    ("II", 2),

    ("III", 3),

# invalid
    ("Z", "Error"),
# Invalid and Valid Letters

("XIZ", "Error"),

# Not valid

    ("VV", "Error"),
# Null input
    ("", "Error"),


]


for roman_numeral, expected_result in test_cases:
    result = roman_to_integer(roman_numeral)
    print(f"The integer equivalent of {roman_numeral} is {result}. Expected: {expected_result}")
    assert result == expected_result, f"Test failed for {roman_numeral}"
