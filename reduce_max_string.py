"""
Program to reduce the adjacent small case common letters in a string 
"""

s = input("Enter the string to be reduced \n")

maxr_str = ''
count = 1

for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        count = count+1
        if i+2 == len(s):
            if count % 2!=0:
                maxr_str = maxr_str + s[i]
    else:
        if count % 2 != 0:
            maxr_str = maxr_str + s[i]
        count = 1
        if i+2 == len(s):
            if count % 2!=0:
                maxr_str = maxr_str + s[i+1]
                
print("Maximun reduced string is",  maxr_str if maxr_str else " empty")