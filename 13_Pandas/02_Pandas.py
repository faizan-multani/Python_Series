import pandas as pd
# Read a file
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(url)
print(df)

# how many columns should display -> usecols=[]
df = pd.read_csv(url,usecols=['petal_width','species'])
print(df)

# to Write a file
test_file=df.to_csv('test.csv')
print(test_file)