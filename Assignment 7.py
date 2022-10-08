# x = [[0.0, 1.0, 2.0],[4.0, 5.0, 6.0]]
# out=[]
# for i in range(len(x)):
#     out.extend(x[i])
# print(out)
# y=''
# for i in range(len(out)):
#     y=y+"".join(str(out[i]))
# print(y)
# print(type(y))
# print(y.count('0'))




# list=[[1,2,3,4],[4,7,5,6]]
# for i in range(len(list)):
#     list[i][0], list[i][-1] = list[i][-1], list[i][0]
# print(list)

# x=list(range(11))
# x=[i for i in range(11) if i%2==0]
# print(x)

# x=[1,2,3,4,5,6,7]
# for i in range(len(x)+1):
#     count = 0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#         if count==2:
#             print(i,end=' ')

# x='ABCADA'
# a=x.count('A')
# b=x.count('B')
# c=x.count('C')
# d=x.count('D')
# print("A-".format({a}),a)
# print("B-".format({b}),b)
# print("C-".format({c}),c)
# print("D-".format({d}),d)



# list = [3, 1, 4, 5, 9, 2, 6, 8]
# print(list)
# list.remove(1)
# del list[-1]
# print(list)


# s1= 'Devansh'
# s2 = 'Himansh'
# if(len(s1) == len(s2)):
#     if(s1==s2):
#         print(" s1 and s2 are equal")
#     else:
#         print("s1 and s2 are not equal")


# x=['hi','madam','java','python','amma']
# max=0
# for i in range(len(x)):
#     temp=x[i]
#     rev=temp[::-1]
#     if rev==temp:
#         if max<len(temp):
#             max=len(temp)
#             long_palindrome_str=temp
# print("longest palindrome string is",long_palindrome_str)



# x='python is good'
# y=x.split()
# print(y)
# y[0]="Java"
# print(y)
# z=" ".join(y)
# print(z)

