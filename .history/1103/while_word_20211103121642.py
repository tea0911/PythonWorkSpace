import os
if(os.path.exists('./1103/word.txt')):
    with open("./1103/word.txt", "r") as f:
         lines = f.readlines()
         print(lines)    # 改行文字が含まれる





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
        lis.append(f"{word}")
print(f"これまでに覚えた単語：{lis}")