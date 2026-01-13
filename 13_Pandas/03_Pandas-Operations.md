# More About Pandas : 

## DataFrame:
- combination of multiple rows or columns.

## Series :
- It represent either one row or either one column.

## Basic Example :
```
import pandas as pd
import numpy as np

np.arange(0,20).reshape(5,4) # reshape(5,4) means 5 rows and 4 columns

Output = 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]

```

## Series: Either 1 row or 1 column
```
##columnname
print(df['Col1'])
# no nesting ->(df[['col1','col2']]) like this.

output :
Row1    1
Row2    1
Name: col1, dtype: int64

print(type(df['col1']))
output:
<class 'pandas.core.series.Series'>

```

## Create DataFrame : Combination of multiple rows or columns
```
## Create Dataframe

import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.arange(1,21).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['col1','col2','col3','col4'])

print(df.head())

Output :
      col1  col2  col3  col4
row1     1     2     3     4
row2     5     6     7     8
row3     9    10    11    12
row4    13    14    15    16
row5    17    18    19    20

```
## Indexing : 3 ways to get the data
```
# 1 columnname
# 2 rowindex[loc]
# 3 rowindex columnindex number[.iloc]

# 1 Using Column name
df[['Col1','Col2','Col3']] 

output :
      col1  col2  col3
row1     1     2     3
row2     5     6     7
row3     9    10    11
row4    13    14    15
row5    17    18    19

# it show us 3 column becoz our condition is only to show 3 column(df[['Col1','Col2','Col3']])

# 2 Using rowindex[loc]
df.loc[['row1','row2']]

output:
      col1  col2  col3  col4
row1     1     2     3     4
row2     5     6     7     8

# 3 Using rowindex columnindex number[.iloc]
df.iloc[2:4,0:2] 
## starting point(2) : ending point+1(4), start point: ending point+1

output:
      col1  col2
row3     9    10
row4    13    14

```

## ##convert dataframe into arrays :
```
print(df.iloc[:,:].values)

output:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
```

## insert null value :
```
df=pd.DataFrame(data=[[1,np.nan,2],[1,3,4]],index=["Row1","Row2"],columns=["Col1","Col2","col3"])

print(df)

output:
	   Col1 	Col2	Col3
Row1	1	    NaN	     2
Row2	1	    3.0	     4

df.isnull().sum()# isnull() check null values than sum() counts.

output:
Col1    0
Col2    1
col3    0
dtype: int64

```

## checks how many times values repeating :
```
df=pd.DataFrame(data=[[1,2,3],[1,2,4]],index=["Row1","Row2"],columns=["col1","col2","col3"])

print(df)

print(df['col2'].value_counts())

output:
col2    count
2         2
Name: count, dtype: int64

```

## Unique values :
```
df['Col2'].unique() # not repeated 
```