import time
import sys
print("WELCOME TO BEHYDRATED")
time.sleep(2)
print("Enter the no of glass of water you want to drink each day")
a=int(input("ENTER YOUR TARGET FOR TODAY DAY: "))
b=0
while b<a:
    c=input("TYPE IF YOU DRANK WATER'w' OR BEER'b' :  ").strip().lower()
    if "w" in c:
        b=b+1
        print("Good job be hydrated")
        print(f"Total hydration score :{b}")
        if b==a:
            print("you reached your goal, keep going")
            break
    elif "b" in c:
        b=b-1
        print("You hurted your body")
        print(f"Total hydration score :{b}")
        if b<0:
            print("your are under negative dehydration")
    else:
        print("please choose a valid action")    



