# solution  of ex 4
st = input("enter a massage :")
words = st.split(" ")
coding = input("1 for coding 0r 0 for decoding ")
coding = True if (coding == "1") else False
print(coding)
if (coding):
   nwords = []
   for word in words:
     if (len(word) >= 3):
        r1 = "wrw"
        r2 = "wdu"
        stnew = r1+word[1:]+word[0]+r2
        nwords.append(stnew)
        # print(stnew)
     else:
        nwords.append(word[::-1])
     print(" ".join(nwords))   
         
else:
   nwords=[]
   for word in words:
      if(len(word)>=3):
         stnew= word[3:-3]
         stnew= stnew[-1] + stnew[0:-1]
         nwords.append(stnew)
      else:
        nwords.append(word[::-1])
      print(" ".join(nwords))   