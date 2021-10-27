# 初期化
marks = ('S','H','C','D')	# 4種類のマーク
cards = []                  # デッキ用リスト
number =[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in marks:

    for num in number:
        cards.append((i, num))





print('-'*10)
print(cards)
print('-'*10)

# 1枚選択
import random				# 乱数用モジュール
r = random.randrange(52)	# 0〜51の乱数生成
print(f'選んだカードは{cards[r]}です')
