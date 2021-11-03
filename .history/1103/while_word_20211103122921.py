import os






while True:
    if(os.path.exists('./1103/word.txt')):
     with open("./1103/word.txt", "r") as f:
         lis = f.readlines()
         lis = [i.strip() for i in lis]
         print(lis)    # 改行文字が取り除かれる
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
          lis.writelines(lis)
print(f"これまでに覚えた単語：{lis}")