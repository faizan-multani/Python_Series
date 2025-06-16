# Practice Problems (With Solutions) :
## Q 1️⃣ Create a list of first 10 natural numbers ?
```
numbers = list(range(1, 11))
print(numbers)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

##  Q 2️⃣ Add an element to the list ?
```
numbers.append(11)
print(numbers)
# Output: [1, 2, ..., 10, 11]
```
##  Q 3️⃣ Insert 100 at index 3 ?
```
numbers.insert(3, 100)
print(numbers)
# Output: [1, 2, 3, 100, 4, 5, ..., 11]
```

##  Q 4️⃣ Remove element 5 from list ?
```
numbers.remove(5)
print(numbers)
# Output: 5 removed
```

##  Q 5️⃣ Reverse the list ?
```
numbers.reverse()
print(numbers)
# Output: reversed list
```

## Q 6️⃣ Sort a list in ascending and descending order ?
```
lst = [5, 2, 9, 1, 8]
lst.sort()
print(lst)  # Ascending

lst.sort(reverse=True)
print(lst)  # Descending
```

## Q 7️⃣ Count even numbers using list comprehension ?
```
nums = list(range(1, 21))
evens = [x for x in nums if x % 2 == 0]
print(evens)
# Output: [2, 4, ..., 20]
```

## Q 8️⃣ Find the sum of all elements ?
```
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)
# Output: 15
```

# Top Interview Questions :
## Q1: Difference between list and tuple ?
### List  
-  Mutable	 
- Slower	 
- [1, 2, 3]	
### Tuple 
- Immutable 
- Faster   
- (1, 2, 3)

## Q2: What is list comprehension ?
- ✅ Shortcut to create list using for loop inside list.
```
squares = [x*x for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]
```

## Q3: Can list store different data types ?
- ✅ Yes, Python lists are heterogeneous.
```
lst = [10, "Hello", 3.5, True]
```

## Q4: How is list stored internally ?
- ✅ Python lists are dynamic arrays — resizing occurs automatically.