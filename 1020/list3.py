a=[0,1,2,3,4,5]
b=['a','b']
c=['x','y','z']

print(a)

d=[0,1,2,3,4,5]					# aのコピーを作成
d[1:2]=b
print(d)
d[4:5]=c
print(d)
