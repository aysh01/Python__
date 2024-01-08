# Wrie a prog. to accept the marks of 5 subjects & find percentage of marks & class of the student..
subjects=['Sub1','Sub2','Sub3','Sub4','Sub5']
marks=[] #Get values of marks of 5 subjects..

for i in range(5):
    a=float(input("Enter Marks of Subjects: "))
    marks.append(a)

percentage=sum(marks) / 5
print("Your, Percentage is ",percentage) #Percentage

if percentage < 35:
    print("I'm so Sorry.. App Fail Ho Gaye Ho..")
elif percentage < 40:
    print("Pass..Class Congrats! App Pass Ho Gaye..")
elif percentage < 50:
    pring("Second..Class Congrats! App Class Mai Second Ho..")
elif percentage < 65:
    print("First..Class Congrats! App Class Mai First Ho..")
else:
    print("Congrats.. App Distinction Se Pass Ho Gaye..")
