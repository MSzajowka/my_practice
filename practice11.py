def check_palindrome(str):
    if str[::] == str[::-1]:
        return True
    else:
        return False


print(check_palindrome('kajak'))
