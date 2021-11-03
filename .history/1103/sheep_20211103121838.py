import time
n = int(input("何匹数えますか？："))
a = 1
while a <= n:
    print(f"羊が{a}匹")
    time.sleep(a/10)
    a+=1
    