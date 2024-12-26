str1=[]
while True:
    str=input()
    if str.strip()=="stop":
        break
    str1.append(str.upper())
for i in str1:
    print(i)