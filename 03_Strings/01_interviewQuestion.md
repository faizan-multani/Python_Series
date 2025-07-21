# 🧠 INTERVIEW LEVEL STRING QUESTIONS :
## 1️⃣ Reverse a string ?
```
s = "Python"
print(s[::-1])  # nohtyP
```
## 2️⃣ Check if string is palindrome ?
```
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
```

## 3️⃣ Count vowels in a string ?
```
s = "hello world"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count)  # Output: 3
```

## 4️⃣ Remove duplicates from string ?
```
s = "banana"
result = "".join(dict.fromkeys(s))
print(result)  # ban
```

## 5️⃣ Find first non-repeating character ?
```
from collections import Counter
s = "aabbccde"
count = Counter(s)
for char in s:
    if count[char] == 1:
        print(char)
        break
```   

## 🎯 Quick Summary:
String = Immutable Sequence of Characters

Powerful built-in methods

Slicing and indexing are your best friends

f-strings for formatting