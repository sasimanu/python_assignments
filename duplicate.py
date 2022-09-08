#Remove duplicate characters from given string and print it
s="resources"
s1=""
for ch in s:
    if ch not in s1:
        s1=s1+ch
print(s1)
