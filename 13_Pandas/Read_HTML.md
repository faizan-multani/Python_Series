# 
```
import pandas as pd

html=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")

type(html)
# Output : list

print(html[0])

# Output : Table(first table which is present in the link/url)

```

## Get Specific table : match=" "
- we'll use match parameter.
```
import pandas as pd

html=pd.read_html("https://en.wikipedia.org/wiki/Economy_of_the_United_States",match="Government debt")

print(html[0])
```