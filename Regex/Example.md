## 🔹 Examples :
```
import re

text = "My number is 9876543210"

# Find all digits

digits = re.findall(r'\d+', text)
print(digits)  # ['9876543210']

# Check if string starts with "My"

match = re.match(r'My', text)
print(match.group())  # 'My'

# Replace digits with XXXXX

masked = re.sub(r'\d+', 'XXXXX', text)
print(masked)  # 'My number is XXXXX'

```

## 🔹 Compiled Pattern (Optional) :
```
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
match = pattern.search("Call me at 123-456-7890")
print(match.group())  # 123-456-7890

```

# ✅ Practice Exercises :
## 🔸 1. Extract all email addresses ?
```
import re

text = "Please contact us at support@example.com or sales@shop.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)  # ['support@example.com', 'sales@shop.org']

```

## 🔸 2. Validate a phone number (e.g., 9876543210) ?
```
phone = "9876543210"
is_valid = re.fullmatch(r'[6-9]\d{9}', phone)
print("Valid" if is_valid else "Invalid")  # Valid

```

## 🔸 3. Find all words starting with capital letters ?
```
text = "Faizan and Ahmad are working at OpenAI in Mumbai."
words = re.findall(r'\b[A-Z][a-z]*\b', text)
print(words)  # ['Faizan', 'Ahmad', 'OpenAI', 'Mumbai']

```

## 🔸 4. Mask all digits in a string ?
```
text = "My OTP is 859630."
masked = re.sub(r'\d', '*', text)
print(masked)  # 'My OTP is ******.'

```

## 🔸 5. Extract all hashtags from a tweet ?
```
tweet = "Loving #Python and #MachineLearning! #AI #coding"
hashtags = re.findall(r'#\w+', tweet)
print(hashtags)  # ['#Python', '#MachineLearning', '#AI', '#coding']

```

## ✅ 1. Scraping and Parsing HTML/XML ?
- Extract all links:
```
html = '<a href="https://example.com">Click</a>'
links = re.findall(r'href="(.*?)"', html)

```

## ✅ 2. Log File Analysis ?
```
log = "ERROR 2025-06-23 11:34:56 - Disk Full"
match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log)
print(match.group())  # O/P 2025-06-23 11:34:56

```
## ✅ 3. Form Validation (like email/password) ?
```
def is_valid_password(pwd):
    return bool(re.fullmatch(r'[A-Za-z0-9@#$%^&+=.-]{8,}', pwd))

print(is_valid_password("Faizan@123.com"))  # True

```
## ✅ 4. Extract Numbers from Mixed Strings ?
```
s = "Order number: 298, Price: ₹550"
numbers = re.findall(r'\d+', s)
print(numbers)  # O/P ['298', '550']

```

## ✅ 5. Find repeated(duplicate) words ?
```
import re

text = "This is is a test test string."

matches = re.findall(r'\b(\w+)\b\s+\1\b', text)
print(matches)  # ['is', 'test']

# (\b\w+\b) - captures a word
# \s+ - space(s)
# \1 - backreference to the first group (i.e., same word again)

```

## ✅ 6. Neglate/Ignore a word ?
```
words = '''
cat
bat
pat
'''
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(words)

for match in matches:
    print(match)
    
    # O/P cat pat
```

