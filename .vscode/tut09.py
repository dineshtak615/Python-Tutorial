# string is immutable{not changable }
a="harry!!!! !!!!!!!! 4848 !harry!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #it remove the all last "!" this character don't remove the leading character
print(a.replace("harry","danish"))
print(a.split(" ")) #it is use like list type
b="introduction tO jS "
print(b.capitalize())


str1= "welcome to the console 222 "

print(len(str1))
print(str1.center(50)) #making a space in output in front of the str1 length equal to 
print(str1.endswith(" 222 ")) 
str1= "welcome to the console 222 "
print(str1.endswith("to",4,10))
str1=" he's name is 45 \"Dan he's an honest man."
print(str1.find("Dan")) # this is find the caharacter/intiger in string for every plaace 
print(str1.index(" is")) # don't found substring 

str2="welcomeToconsole455"
print(str2.isalnum())#  this fun contains the character and number also but don't contain float and it is  also recall don't give the space  in middle of string 

str2="welcomethedinesh" #this function don't contain number/float

print(str2.isalpha())

str1="hello world "

print(str1.islower())
print(str1.isupper())

str1="we wish you a marry christmas 3.0" 
print(str1.isprintable()) # it is take all sting int flaot but othertype data don't take
str="          "# using spacebar
print(str.isspace())

str2=" World Wealth Organzation "
print(str2.istitle())
str4="python  is a interpreted language "
print(str4.startswith("python"))
str4= "he's name is dan , dan is an honest man "
print(str4.title())



