def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sort the strings to ensure the common prefix is at the beginning
    strs.sort()
    
    # Take the first and last strings in the sorted list
    first_str = strs[0]
    last_str = strs[-1]
    
    # Find the common prefix character by character
    common_prefix = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break
    
    return ''.join(common_prefix)

# Ask the user for a list of strings
input_strings = input("Enter a list of strings separated by spaces: ").split()

# Find the longest common prefix
result = longest_common_prefix(input_strings)

# Display the result
print("Longest Common Prefix:", result)
