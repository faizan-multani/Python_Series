# 
```
import pandas as pd

html=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")

type(html)
# Output : list

print(html[0])

# Output : Table(first table which is present in the link/url)

```

## Get Specific Data/Table : match=" "
- we'll use match parameter.
```
import pandas as pd

html=pd.read_html("https://en.wikipedia.org/wiki/Economy_of_the_United_States",match="Government debt")

print(html[0])

# for datatype
print(type(html[0]))
```

## Convert Dataframe to HTML :
```
html[0].to_html('demo.html')
```