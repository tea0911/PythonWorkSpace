fruits = ['バナナ','リンゴ','オレンジ']
n = input("果物をカタカナで入力してください：")
judge = n in fruits

while True:
    if judge is True:
     print (f"{n}は、知っています！")
    else:
        print(f"{n}は、知りませんでした。覚えておきます。")
        fruits.append= n
    n = input("果物をカタカナで入力してください：")
    judge = n in fruits

    
print('知っている果物')
print(fruits)
