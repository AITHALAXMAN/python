# Q)write a program to check whether the given string is anagram or not ?
str1= "silent"
str2="listen"
if len(str1)==len(str2):
    a= sorted(str1)
    b=sorted(str2)
    if a==b:
        print("anagram")
    else:
        print("not")
