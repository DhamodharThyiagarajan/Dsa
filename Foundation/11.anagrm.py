def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    return sorted_str1 == sorted_str2

str1 = "listen"
str2 = "silent"

print(are_anagrams(str1, str2))  # Output: True
