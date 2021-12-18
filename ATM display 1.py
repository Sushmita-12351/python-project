print("Welcome to ABC Bank\n")

a=int(input("Please Choose any one option : \n1. withdraw money \n2.Update Password \n3.Exit"))

if a==1:
    print(int(input("\nHow much money you want to withdraw : ")))
    print("\nPlease collect your money")
    u2=input("Do you want to see your total balance : ")
    if u2=="yes":
       u3=(400000-a)
       print("your total balance is : ",u3)
    else:
       print("thankyou")

elif a==2:
    p1=int(input("enter your current password : "))
    if p1=="7683":
        print("succesfully matched\n")

    p2=int(input("enter your new password : "))
    print("password updated")
    u1=input("do you want to see your password : ")
    if u1=="yes":
       print("your password is : ",p2)
    else:
        print("Thankyou")

elif a==3:
    print("Thankyou")
    exit()
          
