import time
n = int(input("何匹数えますか？："))
a = 1
while a <= n:
    print(f"羊が{a}匹")
    a+=1
    if(a > n/5):
        time.sleep(1)
    elif(a > n/4):
        time.sleep(2)
    elif(a > n/3):
        time.sleep(3)
    elif(a > n/2):
        time.sleep(4)
