# Reading Different Data sources with the help of pandas :
## StringIO:
- in memeory file format object.
```
from io import StringIO
import pandas as pd

data=('col1,col2,col3\n'
    'x,a,1\n'
    'y,b,2\n'
    'z,c,3')

df=pd.read_csv(StringIO(data))    
print(df)

```

## Datatype in csv file :
```
##datatypes in csv
data = ('a,b,c,d\n'
            '1,2,3,4\n'
            '5,6,7,8\n'
            '9,10,11')

df=pd.read_csv(StringIO(data),dtype={'a':int,'b':float,'c':int})
print(df)            
```

## Seperated by tab:
```
import pandas as pd
url='https://download.bls.gov/pub/time.series/cu/cu.item'

df=pd.read_csv(url,sep='\t')   
print(df)

```