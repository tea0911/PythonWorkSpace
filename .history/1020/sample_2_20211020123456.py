fruits = ['バナナ','リンゴ','オレンジ']
n = input("果物をカタカナで入力してください：")
judge = n in fruits

while True:
    if n =='':
        break
    if judge is True:
     print (f"{n}は、知っています！")
    else:
        print(f"{n}は、知りませんでした。覚えておきます。")
        #
    n = input("果物をカタカナで入力してください：")
    judge = n in fruits

print('知っている果物')
print(fruits)
