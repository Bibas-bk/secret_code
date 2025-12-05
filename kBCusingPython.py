print("***Kon Banaega Crorepati****")
Questions=["Who is a founder of america",
           "what is full form of wrc",
           "who is a prime minister of oman",
           "who is the fast blower of world",
           "Choose the odd one:"]
Options=[["colombus","Hitler","Mandela","Nicolos"],
        ["colombus","Hitler","Harry","Nicolos"],
        ["colombus","ranit","Mandela","Nicolos"],
        ["colombus","Hitler","Mandela","starc"],
        ["colombus","Hitler","Mandela","Nicolos"],
        ]
Answer=[1,2,2,4,3]
prize=[10000,50000,100000,10000000]

Total=0
for i in range(len(Questions)):
    print(i+1,".",Questions[i])
    for j in Options[i]:
       print("*",j)
    choice=int(input("Enter a option from (1 to 4)"))
    if choice==Answer[i]:
      print("**Correct Answer***")
      print("You won the ",prize[i])
      Total += prize[i]
    else:
     print("wrong answer")
     print(f"you won {Total}rupees")
     break
    
print(f"Congratulations!!! you have won{Total}rupees")
print("thanks for playing KBC") 