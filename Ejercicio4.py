def palindromo(palabra):
    palabra = palabra.lower()
    # Base case: if the length is 0 or 1, it's a palindrome

    # Check the first and last characters

    if len(palabra) <= 1:
        return True
        # Recursive case: check the substring

    if palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])
    else:
        return False

# Test cases
print(palindromo("radar"))  # True
print(palindromo("hello"))  # False
print(palindromo("A man a plan a canal Panama"))  # True

