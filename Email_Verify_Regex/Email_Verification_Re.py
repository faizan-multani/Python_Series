import re

# faizan.multani33@gmail.com
# a-z start with alphabate
# 0-9 contains number
# . _ time 1   ,should be only 1 time
# . 2,3pos     , . should be there at the last 2,3 place

emails = input('enter email : ')

pattern = re.compile(r'^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            
if re.search(pattern,emails):
    print("correct email")
else:
    print("incorrect email")


# ^     starting condition , starts with character(a-z)
# [a-z] start with a-z
# [\._]?   its optional condition after writiung ' ? '
# ?     to make condition optional
# [a-z0-9]  before ' @ ' we can provide alphabate or number
# [@]    it should hv only one ' @ ' 
# [@]\w     after getting ' @ ' it will check for ' \w '  means [a-zA-Z0-9_]    
# [.]      checks for ' . ' and after that \w
# \w{2,3}   the ' . ' it should be on 2,3 place at the last