def preLetter(str,letter):
    index=str.lower().find(letter.lower())
    if index==-1:
        return str.lower()
    return str[:index].lower()+str[index:].upper()
str1=input()
l=input()
print(preLetter(str1,l))