
# kbc 
questions=[
    
    ["which language was used to create fb ?",
           "python","french ","javascrift","php"
           ,"none",4
           ], 
            
            
             [
    
    "which language was used to create fb ?",
           "python","french ","javascrift","php"
           ,"none",4] ,   
            
            
             [
    
    "which language was used to create fb ?",
           "python","french ","javascrift","php"
           ,"none",4],



           ["which language was used to create fb ?",
           "python","french ","javascrift","php"
           ,"none",4]

]
 
levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i-1]
    print(f"question for Rs. {levels[i]}")
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]} ")
    reply=int(input("enter your answer (1-4)"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"\n\n\ncorrect answer you have won Rs {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9): 
            money=320000
        elif(i==14):   
            money=10000000
    else:
        print("wrong answer  ")
        break
print(f"your take money is{money} ")