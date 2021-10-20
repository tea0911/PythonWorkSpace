n = 2
while n != 0:
    n =input("整数を入力してください")
    n = int(n)
    if n == 0:
        break
    else if n % 2  == 0:
        print("偶数です")
    else:
        print("奇数です")

