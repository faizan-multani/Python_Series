# reading a file

# f = open('File_Read_Write/about.txt' , 'r')

# print(f.read())
# f.close()

                # (OR)

# with open('File_Read_Write/about.txt', 'r') as f:
#     print(f.read())

                # (OR)

# with open('File_Read_Write/about.txt', 'r') as f:
#       for line in f:
#         print(line, end='')


# writing a file

# with open('File_Read_Write/demo.txt', 'w') as w:
#     w.write("hello there!")


# make a copy of about.txt file
with open('File_Read_Write/about.txt', 'r') as rf:
    with open('File_Read_Write/about_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
        









