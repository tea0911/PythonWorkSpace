n=input("整数を入力してください")

n = int(n)

numbers = range(1,int(n)+1)
total = sum(numbers)
average = total/len(numbers)
print(f"1~{n}までの合計：{total}")
print(f"平均：{average}")