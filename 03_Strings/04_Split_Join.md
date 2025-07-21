# 🔥 Practice Questions (with Solutions)
## Q1: Split a sentence into words ?
```
sentence = "Python is very powerful"
words = sentence.split()
print(words)
# Output: ['Python', 'is', 'very', 'powerful']
```

## Q2: Join words into a sentence ?
```
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)
# Output: Python is awesome
```
## Q3: Split email into username & domain ?
```
email = "faizan@gmail.com"
username, domain = email.split('@')
print(username)
print(domain)
# Output: faizan / gmail.com
```
## Q4: Join list of numbers with comma ?
```
numbers = ['1', '2', '3', '4', '5']
result = ','.join(numbers)
print(result)
# Output: 1,2,3,4,5
```

## Q5: Remove extra spaces in string ?
```
s = "Python    is    awesome"
clean = ' '.join(s.split())
print(clean)
# Output: Python is awesome
# Extra spaces are ignored in list/split()
```
## Q6: Split only first 2 words ?
```
sentence = "Python is very easy and powerful"
result = sentence.split(' ', 2)
print(result)
# Output: ['Python', 'is', 'very easy and powerful']
```

# 🔥 2️⃣ Common Interview Questions
## Q1:What is the difference between split() and join() ?
✅ Answer:
split() converts string → list

join() converts list → string

## Q2:Can you split using multiple separators ?
✅ Answer:

Not directly. Use re.split() from regex module.
```
import re
text = "apple,banana;orange|grape"
result = re.split(r'[;,|]', text)
print(result)
# Output: ['apple', 'banana', 'orange', 'grape']
```
## Q3:What happens if you use split() without any arguments ?
✅ Answer:

Default separator is any whitespace.

Extra spaces are automatically handled.
```
"  a  b c  ".split()
# Output: ['a', 'b', 'c']
```

## Q4:Can you join() non-string items ?
✅ Answer:

No, join() works only on iterables of strings.

Use list comprehension or map:
```
nums = [1, 2, 3]
result = ','.join(map(str, nums))
print(result)
# Output: 1,2,3
```