## Que Count positive num and negitive number ?
```
num = [1,-2,3,5,-1,5,9,-8]
count_pos = 0
count_neg = 0
for n in num:
    if (n < 0):
        # print("negtive",count)
        count_neg = count_neg +1
    elif (n >= 0):
        # print("positive",count)
        count_pos = count_pos + 1
        
print("positive numbers : ",count_pos)
print("negitive numbers : ",count_neg)

# output // positive numbers :  5
# output // negitive numbers :  3

```

## Que reverse string ?
```
str = "priya"
rev_str = "" # ayirp

for s in str:
    rev_str = s + rev_str
    
print(rev_str)    

```

## Que Find the first non-repeated character ?
```
str = "mamaisgood"

for char in str:
    if str.count(char) == 1:
        print("non-repeated character is :",char)
        break
    
```

## Que Factorial number ?
```
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact * i
    i -= 1

print(fact) 

# num = 5  //  fact = 5x4x3x2X1 => 120

```
## que Prime number ?
```
num = 16

if num > 1 :
    for i in range(2,num+1):
        if(num % i == 0):
            print("not a prime number")
            break
        else:
            print("prime number")
            break
            
```

## Que Find Duplicate items ?
```
fruits = ["apple","mango","litchi","banana","cheery","apple","mango"]

duplicate_fruit = set()

for fruit in fruits:
    if fruit in duplicate_fruit:
        print("duplicate fruit",fruit)
        # break
    
    duplicate_fruit.add(fruit)
       
```