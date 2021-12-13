name=input("What is your good name ?")
q=input("Do you wanna play this game ?")
if q=="yes":
    print("lets start the game")
    print("question 1. After how many year's FIFA World cup is held ?")
    a=print("a) 2 years")
    b=print("b) 3 years")
    c=print("c) 4 years")
    d=print("d) every year")
    choose=input()
    if(choose=="c"):
        print("your answer is correct")
        t=(0+10)
        print(t)
        print("your score is =",t)
    elif(choose=="a","b","d"):
        t=(-10)
        print(t)
        print("bad luck")

    print("question 2. Which country won the first FIFA World cup ?")
    a=print("a) Argentina")
    b=print("b) uruguay")
    c=print("c) Italy")
    d=print("d) Brazil")
    choose=input()
    if(choose=="b"):
        print("your answer is correct")
        t=(t+t)
        print(t)
        print("your score is =",t)
    elif(choose=="a","c","d"):
        t=(t-10)
        print(t)
        print("bad luck")

    print("question 3. Who won the first ICC World cup ?")
    a=print("a) India")
    b=print("b) West Indies")
    c=print("c) England")
    d=print("d) Australia")
    choose=input()
    if(choose=="b"):
        print("your answer is correct")
        t=(t+10)
        print(t)
        print("your score is =",t)
    elif(choose=="a","c","d"):
        t=(t-10)
        print(t)
        print("bad luck")

    print("question 4. Who won the first T20 World cup ?")
    a=print("a) Pakistan")
    b=print("b) Sri Lanka")
    c=print("c) India")
    d=print("d) West Indies")
    choose=input()
    if(choose=="c"):
        print("your answer is correct")
        t=(t+10)
        print(t)
        print("your score is =",t)
    elif(choose=="a","b","d"):
        t=(t-10)
        print(t)
        print("bad luck")

    print("question 5. Who is known as the Flying Sikh ?")
    a=print("a) Micheal Jackson")
    b=print("b) Usain Bolt")
    c=print("c) Carl Lewis")
    d=print("d) Milkha Singh")
    choose=input()
    if(choose=="d"):
        print("your answer is correct")
        t=(t+10)
        print(t)
        print("your score is =",t)
    elif(choose=="a","b","c"):
        t=(t-10)
        print(t)
        print("bad luck")
    print("Total score is =",t)
    print("congratulation for your score")
elif q=="no" :
    print("Bye Bye")
            
