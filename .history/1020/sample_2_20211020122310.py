fruits = ['バナナ','リンゴ','オレンジ']
n = input("果物をカタカナで入力してください：")
judge = n in fruits

while n is not True:
    if judge is True:
     print (f"{n}は、知っています！")
    if judge is False:
        print(f"{n}は、知りませんでした。覚えておきます。")
        # fruits[fruits.length+1]=n
    n = input("果物をカタカナで入力してください：")
    judge = n in fruits

    
print('知っている果物')
print(fruits)
