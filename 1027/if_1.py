while True:
    i = input("好きな文字を入力してください:")
    if i == '':
        break
    elif i.isalpha():
        print("文字")
    elif i.isdigit():
        print("数字")
    elif i.isalnum():
        print("アルファベットと数字")
    else:
        print("その他")