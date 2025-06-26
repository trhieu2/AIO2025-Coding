def count_character(string):
    result = dict()

    for char in string:
        result[char] = result.get(char,0) + 1

    return result

string = "Happiness"
print(count_character(string))