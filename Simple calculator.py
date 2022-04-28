print(" welcome to mini calculator \n" )
operator=input("\nselect the operator(+,-,*,/,%) : ")
f1=int(input("\nenter the first number : "))
f2=int(input("enter the second number : "))

if operator=="+":
    print("answer is : ", f1+f2)
elif operator=="-":
      print("answer is : ",f1-f2)

elif operator=="*":
      print("answer is : ",f1*f2)

elif operator=="/":
      print("answer is : ",f1/f2)

elif operator=="%":
      print("answer is : ",f1%f2)

else:
    print("invalid  operation")
