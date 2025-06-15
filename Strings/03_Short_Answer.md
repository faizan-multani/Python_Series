# Python String Interview Questions (With Short Answers)

## 1. Are strings mutable in Python ?
- No, strings are immutable.

## 2. How do you reverse a string ?
- s[::-1]

## 3. Difference between is and == for strings ?
- is: checks identity (same memory object).
- ==: checks value equality.

## 4. How to count occurrences of a substring ?
- s.count('substring')

## 5. How to check if a string starts or ends with a substring ?
- s.startswith('sub')
- s.endswith('sub')

## 6. How to remove whitespace from a string ?
- s.strip()      # both sides
- s.lstrip()     # left
- s.rstrip()     # right

## 7. How to join a list into a string ?
- " ".join(['a', 'b', 'c'])  # Output: 'a b c'

## 8. How to split a string ?
- s.split('delimiter')

## 9. How to replace part of a string ?
- s.replace('old', 'new')

## 10. How to check if string contains only digits, letters, or both ?
- s.isdigit()
- s.isalpha()
- s.isalnum()

## 11. How to capitalize first character of each word ?
- s.title()

## 12. How to format strings ?
- name = "Faizan"
- f"Hello, {name}!"

## 13. How to remove punctuation from string ?
- import string
- s.translate(str.maketrans('', '', string.punctuation))

## 14. How to count vowels in a string ?
- sum(1 for c in s if c in 'aeiouAEIOU')

## 15. Write code to check palindrome ?
- def is_palindrome(s):
    return s == s[::-1]

