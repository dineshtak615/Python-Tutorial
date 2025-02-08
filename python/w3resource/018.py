def substrng_copy(text,n):
    flen=2
    if flen > len(text):
        flen=len(text)
    substr=text[:flen]    
    result="  "
    for i in range(n):
        result=result + substr
    return result

print(substrng_copy("ababf ",2))
print(substrng_copy(" a ",3))