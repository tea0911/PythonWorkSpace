fruits = ['バナナ','リンゴ','オレンジ']
n = input("果物をカタカナで入力してください：")
judge = n in fruits

while judge is True:
    print ("{n}は,知っています！")
    n = input("果物をカタカナで入力してください：")
    judge = n in fruits
    
print('知っている果物')
print(fruits)
