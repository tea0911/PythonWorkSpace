fruits = ['バナナ','リンゴ','オレンジ']

while True:
    n = input("果物をカタカナで入力してください：")
    if n =='':
        break
    judge = n in fruits
    if judge is True:
     print (f"{n}は、知っています！")
    else:
        print(f"{n}は、知りませんでした。覚えておきます。")
        fruits.append(n)

print('知っている果物')
print(fruits)
