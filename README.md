Python Program to Find Longest Common Prefix
This README describes a Python program that retrieves a string array from the user and finds the longest common prefix shared by all strings in the array.

Functionality:

Prompts the user to enter a list of strings, separated by spaces.
Calculates the longest prefix shared by all strings in the list.
Displays the resulting prefix to the user.
Code Breakdown:

The program leverages the following functions:

input: Obtains user input as a string.
split: Splits the input string into individual strings based on spaces.
min: Identifies the shortest string within the user-provided list.
enumerate: Iterates through characters in a string while keeping track of their index.
if statements: Control the program flow based on specific conditions.

Example:
Input:
flower rose violet

Output:
The longest common prefix is: flo
