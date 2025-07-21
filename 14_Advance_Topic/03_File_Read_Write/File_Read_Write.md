
## File reading :
### First create file called 'about.txt' and provide a correct path (folder/file_name.txt).
```
# f = open('File_Read_Write/about.txt' , 'r')

# print(f.read())
# f.close()

                # (OR)

with open('File_Read_Write/about.txt', 'r') as f:
    print(f.read())
    
    # this is modern way to reading a file called 'context   manager'.

```

## Large size of file :
```
# Iterating through small chunks:

size_to_read = 100 # 100 = character

f_contents = f.read(size_to_read)
while len(f_contents) > 0:
	print(f_contents)
	f_contents = f.read(size_to_read) # again check the size of a file
```

## File writing :
```
with open('File_Read_Write/demo.txt', 'w') as w:
    w.write("hello there!")

    # o/p demo.text -> hello there!
    # it creates the file itself
```

## Make a copy of 'about.txt' fileby writing it :
```
with open('File_Read_Write/about.txt', 'w') as rf:
    with open('File_Read_Write/about_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
```

## Make a copy of a 'image.png/image :
```
with open('File_Read_Write/image.png', 'rb') as rf:
    with open('File_Read_Write/image_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)

```

## Copying the image with size :
```
# Copying the image with chunks:

with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            
```
