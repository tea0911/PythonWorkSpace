import os

while True:
    with open("./1103/word.txt", "r") as f:
        lis = f.readlines()
        lis = [i.strip() for i in lis]
    word =input("単語を入力してください：")

    if(word == "LIST"):
        print(f"単語リスト：{lis}")
    elif(word in lis):
        print("既に登録済みです")
    elif(word == ""):
        print("終了します")
        break
    else:
        with open("./1103/word.txt", "a") as f:
            f.writelines(f"{word}\n")
print(f"これまでに覚えた単語：{lis}")