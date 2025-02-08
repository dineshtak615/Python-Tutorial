def largerstring(text ,n):
    result=""
    for i in range(n):
        result=result+text
    return result     

print(largerstring(" abc ", 2))