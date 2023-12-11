def de_vowel(str):

    str_list = list(str)
    result_list = []

    for letter in str_list:
        match letter.lower():
            case "a"|"e"|"i"|"o"|"u":
                pass 
            case other:
                result_list.append(letter)

    result = "".join(result_list)
    return result


# What if the string is all vowels?
print(de_vowel("aeiou")) ## -> result = "" 
# What if there are no vowels?
print(de_vowel("bbcclllqq")) ## -> result = "bbcclllqq"
# What if there is a mix of vowels and non-vowels and spaces?
print(de_vowel("hello world")) ## -> result = "hll wrld"
# What if some vowels are capitalized, e.g., the first letter in a sentence?
print(de_vowel("Hello world")) ## -> result = "Hll wrld"