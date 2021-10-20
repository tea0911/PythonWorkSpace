n=input("整数を入力してください")

n = int(n)
while n == 0:
    n =input("整数を入力してください")
    if n % 2  == 0:
        print("偶数です")
    else:
        print("奇数です")

