# Mini-Project Using List :
## 📝 Count frequency of each word
```
text = "Python is easy and Python is powerful"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# Output: {'Python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

```