# Write a fun sum of given numbers pass 1,2,3 n return result is 6
# def java(a,b,c):
#     return a+b+c
# d=java(1,2,3)
# print(d)


# write a fun to print even and odd num in list -> pass list to fun x=list(range(1,11))->(1,10)
# x=list(range(1,11))
# even_list=[]
# odd_list=[]
# def Deva(x):
#     for i in range(len(x)):
#         if(x[i]%2==0):
#             even_list.append((x[i]))
#         else:
#             odd_list.append((x[i]))
#     return even_list,odd_list
# print(Deva(x))


#write a program for default args and return result
#
# def add(b,c,a=200):
#     print("a val",a)
#     print("b val",b)
#     print("c val",c)
#     return (a + b, c)
# A=add(20,30)
# print(A)



# write a  fun to print multiplication table  # pass n from keyboard

# def table(n):
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i)
# table(9)


# write a function pass n of args and return list using varible len args

# def Deva(*k):
#     return(list(k))
# print(Deva("Deva","Hima","Giri"))



# write a function pass keyword args nd return dict (a=10,b,20,c=30)  -> {a:100,b:400,c:900}

# def Deva(a,b,c):
#     a=a*a
#     b=b*b
#     c=c*c
#     return a,b,c
# x,y,z=Deva(a=10,b=20,c=30)
# print(x,y,z)

# def java(a,b,c):
#     a=a*a
#     b=b*b
#     c=c*c
#     return a,b,c
# x,y,z=java(10,20,30)
# print(x,y,z)

# def java(a,b,c):
#     print(a*a)
#     print(b*b)
#     print(c*c)
# java(10,20,30)
# def python(**Deva):
#     print(Deva)
# python(a=100,b=400,c=900)






# write a function to fetch frst word from list elements x=["PYTHION IS GOOd","JAVA IS GOOD"]  # ["PYTHON","JAVA"]

# x=["PYTHON IS GOOD","JAVA IS GOOD"]
# out=[]
# for i in range(len(x)):
#     temp=x[i].split()
#     out.append(temp[0])
# print(out)

# write a fun to chnage string lower to uppeer and upper to lower  and return the string

# a="Be Positive iN Always"
# def python(x):
#     return x.swapcase()
# i=python(a)
# print(i)


# write fun to get only vowels from the list
# x=["PYTHION IS GOOd","JAVA IS GOOD"]   ->[I,O,I,O,O,A,A,I,O O]  -> remove the duplicates -> ['I','O','A']
# x=["PYTHION IS GOOd","JAVA IS GOOD"]
# Vowels=['A','E','I','O','U']
# out=[]
# def b(vowels,x):
#     out=[]
#     y=''.join(x)
#     print(y)
# for i in range(len(x)):
#     if i in Vowels and i not in out:
#             out.append(i)
# print(out)


# x=['PYTHON IS GOOD','JAVA IS GOOD']
# vowels=['A','E','I','O','U']
#
# def b(vowels,x):
#     out=[]
#     y=''.join(x)
#     print(y)
#     for i in y:
#         if i in vowels and i not in out:
#             out.append(i)
#     return out
# duplicates=b(vowels,x)
# print(duplicates)

# write a function get the max num from list without using predefined fun max   x=[101,200,3000,400]  #max : 3000


# def max(x):
#     max=x[0]
#     for i in x:
#         if i>max:
#             max=i
#     return max
# x=[101,200,3000,400]
# print(max(x))


# write a function to sort the list without using sort fun     hint: we can use sorted fun
# x=[1,4,5,2,37,79,7869,86,357]
# print(sorted(x))

print("sekhar")
