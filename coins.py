print("Welcome to coin collector")
a=0
while a<1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    c=input("Type 'C' to collect coins and 'S' to spend coins: ").strip().lower()
    if "c" in c:
        a=a+10
        print("COINS COLLECTED")
        print(f"Available balance:{a}")
        if a==100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            print("MAX COINS")
            break
    elif "s" in c:
        a=a-10
        print("COINS SPENT")
        print(f"Available balance:{a}")
        if a<0:
            print("YOU TOOK A LOAN")
        if a==0:
            print("NO COINS")
    else:
        print("PLEASE INPUT A VALID VALUE")    

           
    