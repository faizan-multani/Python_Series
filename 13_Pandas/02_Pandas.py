# import pandas as pd
# # Read a file
# url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
# df = pd.read_csv(url)
# print(df)

# # how many columns should display -> usecols=[]
# df = pd.read_csv(url,usecols=['petal_width','species'])
# print(df)

# to Write a file
# test_file=df.to_csv('test.csv',index=False) # remove index number like 0,1,2,3,4 use-> index=False
# print(test_file)

# to Insert record and write in csv file
# from io import StringIO
# import pandas as pd

# data=('col1,col2,col3\n'
#     'x,a,1\n'
#     'y,b,2\n'
#     'z,c,3')

# df=pd.read_csv(StringIO(data)).to_csv('string_csv.csv',index=False)    
# print(df)


import pandas as pd

df=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')           
print(df)