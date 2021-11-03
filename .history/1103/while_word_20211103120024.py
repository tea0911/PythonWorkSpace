import os
if(os.path.exists('word.txt')):
    fileobj = open('word.txt')
    lis= fileobj.read()
    fileobj.close()

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
        lis.append(word)
print(f"これまでに覚えた単語：{lis}")