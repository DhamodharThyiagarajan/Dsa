def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Example usage
print(reverse_string("hello"))  # Output: "olleh"