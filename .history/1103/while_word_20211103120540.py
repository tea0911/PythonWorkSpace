import os
if(os.path.exists('word.txt')):
    with open("word.txt", "r") as f:
      lines = f.read().split(',')



while True:
    word =input("単語を入力してください：")

    if(word == "LIST"):
        print(f"単語リスト：{lis}")
    elif(word in lis):
        print("既に登録済みです")
    elif(word == ""):
        print("終了します")
        break
    else:
        lis.append(f"{word}\n")
print(f"これまでに覚えた単語：{lis}")