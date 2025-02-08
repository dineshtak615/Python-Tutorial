# pass the argument in function
# def average(a=4,b=9):

#     print("the avg :",(a+b)/2)
# # average(2,6)
# # average(1)
# # average(b=4)
# average(b=8,a=3)

# def name(fname,mnmae="jhon",lnmae ="whatson"):
    # print("hello ",fname,mnmae,lnmae)
# name("manish","kalu","hero")
def average(number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
        print("average is ",sum/len(number))
        return 4
        return sum/len(number)

r=4
average(r)
c = average(3) #give not argument default case none
print(c)
