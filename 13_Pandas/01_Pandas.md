# panda :
- Pandas is a powerful, open-source library used for data manipulation, analysis, and cleaning. It's built on top of NumPy and is especially useful when working with structured data like tables 
- e.g., CSV files, Excel spreadsheets, SQL databases, etc.).

## 🔸 Installation :
```
pip install pandas
```
## 🔹 What is Pandas ?
- Pandas provides two main data structures:

- Series – a one-dimensional labeled array.

- DataFrame – a two-dimensional labeled table (like a spreadsheet or SQL table).

## 🔸 Why Use Pandas ?
- Easy handling of missing data.

- Powerful and flexible tools for data selection, filtering, grouping, and aggregation.

- Seamless data import/export from CSV, Excel, SQL, JSON, etc.

- High-performance data alignment and merging.

- Integrated with NumPy, Matplotlib, and Scikit-learn.

## 🔹 Example Usage :
## 1. Importing Pandas :
```
import pandas as pd
```
## 2. Creating a DataFrame :
```
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
print(df)

# Output:
      Name  Age      City
0    Alice   25  New York
1      Bob   30     Paris
2  Charlie   35    London

```

## 3. Reading a CSV File :
```
df = pd.read_csv('file.csv')
```

## 4. Basic Operations :
```
df.head()       # Show first 5 rows
df.info()       # Show summary of the DataFrame
df.describe()   # Show statistics for numeric columns
df['Age'].mean()  # Average age

```

## 5. Filtering Data :
```
df[df['Age'] > 30]
```

## Pandas Overview :
### As mentioned earlier, Pandas has two main data structures :

- Series : 1D labeled array

- DataFrame : 2D labeled table (more commonly used)

## 📌 Creating a DataFrame :
```
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print(df)

# Output:
      Name  Age      City  Salary
0    Alice   25  New York   50000
1      Bob   30     Paris   60000
2  Charlie   35    London   70000
3    David   40     Tokyo   80000

```

## Common Pandas Methods (with examples) :
## 1 .head(n) :
- Shows the first n rows (default is 5).
```
df.head(2)
```
## 2 .tail(n) :
- Shows the last n rows.
```
df.tail(2)
```

## 3 .info() :
- Gives a summary of the DataFrame, including data types and non-null counts.
```
df.info()
```

## 4 .describe() :
- Summary statistics of numeric columns.
```
df.describe()
```

## 5 .shape :
- Returns the dimensions: (rows, columns)
```
df.shape
```

## 6 Selecting Columns :
```
df['Name']  # single column
df[['Name', 'City']]  # multiple columns
```

## 7. Filtering Rows :
```
df[df['Age'] > 30]
```

## 8. Adding a New Column :
```
df['Tax'] = df['Salary'] * 0.2
```

## 9. Dropping Columns or Rows :
```
df.drop('Tax', axis=1, inplace=True)  # Drop column
df.drop(2, axis=0, inplace=True)      # Drop row by index
```

## 10. Sorting :
```
df.sort_values(by='Age', ascending=False)
```

## 11. Grouping and Aggregation :
```
df.groupby('City')['Salary'].mean()
```

## 12. Handling Missing Values :
```
df.isnull()        # Detect missing values
df.dropna()        # Drop rows with missing values
df.fillna(0)       # Replace missing values with 0
```

## 13. Reading & Writing Files :
```
# Read
pd.read_csv('data.csv')
pd.read_excel('data.xlsx')

# Write
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)

```

## 🧠 Tips for Learning Pandas :
- Always start by checking df.head() to preview data.

- Use .info() and .describe() to understand your dataset.

- Chain commands when you're more comfortable.
```
df[df['Age'] > 30].sort_values('Salary')
```
