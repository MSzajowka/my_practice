def check_palindrome(palindrome):
    string = palindrome.replace(" ", "")
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

palindrome = "Kobyła ma mały bok"
print(check_palindrome(palindrome))
