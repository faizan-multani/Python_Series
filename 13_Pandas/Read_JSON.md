# Read JSON file using Pandas :
```
import pandas as pd

data = [
  {"id": 1, "name": "Faizan", "age": 22},
  {"id": 2, "name": "Ali", "age": 21}
]

df = pd.read_json(data)
print(df)

# Output :
   id    name  age
0   1  Faizan   22
1   2    Ali   21

```

## Read Json String :
```
json_data = '''
[
  {"city": "Delhi", "temp": 30},
  {"city": "Mumbai", "temp": 32}
]
'''

df = pd.read_json(json_data)
print(df)

```

# Read JSON from API :
```
import requests
import pandas as pd

url = "https://api.example.com/users"
response = requests.get(url)

df = pd.DataFrame(response.json())
print(df.head())

```

## Nested JSON : (important)
```
from pandas import json_normalize

data = [
  {
    "id": 1,
    "name": "Faizan",
    "address": {
      "city": "Delhi",
      "pin": 110001
    }
  }
]

df = json_normalize(data)
print(df)

# Output :
   id    name       address.city    address.pin
0   1    Faizan        Delhi          110001

```

## Modify JSON data :
```
df["status"] = "Active"
```

## Convert DataFrame → JSON :
```
df.to_json("output.json", orient="records", indent=2)
```

##
```
import pandas as pd
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])
print(df)

output:
col 1	col 2
row 1	a	b
row 2	c	d


df.to_json()
output:
'{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'

df.to_json(orient='index')

output:
'{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'

df.to_json(orient='columns')

output:
'{"col 1":{"row 1":"a","row 2":"c"},"col 2":{"row 1":"b","row 2":"d"}}'

df.to_json(orient='records')

output:
'[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'

df.to_json(orient='split')

output:
'{"columns":["col 1","col 2"],"index":["row 1","row 2"],"data":[["a","b"],["c","d"]]}'

df.to_json(orient='table')

Output:
'{"schema":{"fields":[{"name":"index","type":"string"},{"name":"col 1","type":"string"},{"name":"col 2","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":"row 1","col 1":"a","col 2":"b"},{"index":"row 2","col 1":"c","col 2":"d"}]}'
schema='{"schema":{"fields":[{"name":"index","type":"string"},{"name":"col 1","type":"string"},{"name":"col 2","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":"row 1","col 1":"a","col 2":"b"},{"index":"row 2","col 1":"c","col 2":"d"}]}'

pd.read_json(schema,orient='table')

output :
col 1	col 2
row 1	a	b
row 2	c	d

```