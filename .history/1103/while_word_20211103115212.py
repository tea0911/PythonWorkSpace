


while True:
    word =input("単語を入力してください：")

    if(word == "LIST"):
        print(f"単語リスト：{list}")
    elif(word in list):
        print("既に登録済みです")
    elif(word == ""):
        print("終了します")
        break
    else:
        list.append(word)
print(f"これまでに覚えた単語：{list}")