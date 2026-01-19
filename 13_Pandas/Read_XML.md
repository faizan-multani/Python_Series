# What is XML ?
- XML stands for eXtensible Markup Language.
- XML is a markup language much like HTML.
- XML was designed to store and transport data.
- XML was designed to be self-descriptive.
- XML is a W3C Recommendation.

```
import pandas as pd

pd.read_xml('test.xml')

# output :
	shape	degrees	sides
0	square	360	4.0
1	circle	360	NaN
2	triangle	180	3.0

```

## Write xml data :
```
import pandas as pd

xml = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
   <firstname>Krish</firstname>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
   <firstname/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
   <firstname/>
 </row>
</data>'''

print(ps.read_xml(xml))

# Output :
	shape	  degrees	sides	firstname
0	square	    360	    4.0 	Krish
1	circle	    360	    NaN	    None
2	triangle    180	    3.0	    None

```

## Another way to write the xml data :
```
xml = '''<?xml version='1.0' encoding='utf-8'?>
<data>
  <row shape="square" degrees="360" sides="4.0" firstname="Krish"/>
  <row shape="circle" degrees="360"/>
  <row shape="triangle" degrees="180" sides="3.0" lastname="Naik"/>
</data>'''

print(pd.read_xml(xml,xpath=".//row"))

# Output :

    shape	    degrees	   sides  firstname	  lastname
0	square	    360	       4.0	    Krish	    None
1	circle	    360	       NaN	    None	    None
2	triangle	180	       3.0	    None	    Naik

```

##
```
xml = '''<?xml version='1.0' encoding='utf-8'?>
<doc:data xmlns:doc="https://example.com">
  <doc:row>
    <doc:shape>square</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides>4.0</doc:sides>
  </doc:row>
  <doc:row>
    <doc:shape>circle</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides/>
  </doc:row>
  <doc:row>
    <doc:shape>triangle</doc:shape>
    <doc:degrees>180</doc:degrees>
    <doc:sides>3.0</doc:sides>
  </doc:row>
</doc:data>''' 

df=pd.read_xml(xml,xpath=".//doc:row",namespaces={"doc": "https://example.com"})

# converting Dataframe to xml
df.to_xml('test1.xml')
```