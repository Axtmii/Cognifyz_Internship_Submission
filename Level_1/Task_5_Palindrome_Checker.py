def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")