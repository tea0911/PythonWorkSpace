import time
n = int(input("何匹数えますか？："))
a = 0
while a < n:
    print(f"羊が{n}匹")
    if(a > n/4):
        time.sleep(1)
    elif(a > n/2):
        time.sleep(2)
