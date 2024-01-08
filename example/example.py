# Write a python prog. to check 3 numbers are bigger or not..
#data=[]
#for i in range(3):
#   a=int(input("Enter Number: "))
#  data.append(a)

# print ("The, Biggest Number is: ",max(data))
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))

if a > b and a > c:
    print (a,"is bigger..")
elif b > c:
    print(b,"is bigger..")
else:
    print(c,"is bigger..")
