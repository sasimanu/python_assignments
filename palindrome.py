#check if a given string is a palindrome or not
my_str = "madam"
rev_str = my_str[::-1]
if my_str == rev_str:
    print("string is palindrome")
else:
    print("string is not palindrome")
