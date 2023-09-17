# regex.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: my brother


import re


#Commented out the code that was in the sample file

# def find_date(line):
#     pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
#     result = re.findall(pattern,line)

#     pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
#     result = result + re.findall(pattern,line)
#     return result


# f = open("datefile.dat")
# for line in f.readlines():
#     print(line)
#     result = find_date(line)
#     if (len(result)>0):
#       print(result)


textfile = open("datefile.dat", 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("((?:Mr\.|Dr\.|Ms\.|Mrs\.)(?:\s+[A-Z]\w+){1,2})", filetext)
print(matches)
print(len(matches))