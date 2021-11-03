import time
while True:
    n = int(input("何匹数えますか？："))
    if n > 100:
        print("多すぎます")
        continue
    else:
        break

a = 1
while a <= n:
    print(f"羊が{a}匹")
    time.sleep(a/10)
    a+=1
    