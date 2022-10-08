#Byte()
x=[1,2,3,255]  # 0 to 255
y=bytes(x)
#Y[0]=100
print("type of a :",type(y))
for i in y:
    print(i,end=' ')

#Bytearray

x=[1,2,3,255]  # 0 to 255
y=bytearray(x)
for i in y:
    print(i,end=' ')
print()
print(y[0])
y[0]=255
for i in y:
    print(i,end=' ')


