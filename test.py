# print ("Hello, Python!");
# a=10
# b=20
# c=40
# d=50
# print(a,b,c,d)
# a,b=c,d
#
# print(a,b,c,d)
# del d
# print(a,b,c)
#
#
# a,b,c = 1,2,"john"
#
# print(a,b,c)
#
# a = 10
# # Two objects are passed in print() function
# print("a =", a)
#
# b = a
# # Three objects are passed in print function
# print('a =', a, '= b')

# a = 10
# print("a =", a, sep='dddd', end='\n')
# print("a =", a, sep='0', end='$$$$$')

# name = input("Enter a name of student:")
# print("The student name is: ", name)

#str1 = '''Hi Python'''
#print(str1)


# list = [1,2,3,4,5,6,7]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# # Slicing the elements
# print(list[0:7])
# # By default the index value is 0 so its starts from the 0th element and go for index -1.
# print(list[:])
# print(list[2:5])
# print(list[1:6:2])

# list = [1,2,3,4,5]
# print(list[-1])
# print(list[-3:])
# print(list[:-1])
# print(list[-3:-1])


# list = [1, 2, 3, 4, 5, 6]
# nested_list=[[7,8,9],['python'],[10,11,12]]
# print(list)
# # # It will assign value to the value to the second index
# list[2] = 10
# print(list)
# # Adding multiple-element
# list[1:3] = [89, 78]
# print(list)
# # # It will add value at the end of the list
# list[-1] = 25
# print(list)
# list.append(30)
# list.append(35)
# print(list)
# list.remove(30)
# print(list)
# print(nested_list[0][2])
# print(nested_list[1][0])
# print(nested_list[2][2])
# print(max(list))
# print(min(list))



# list1 = [1,2,2,3,55,98,65,65,13,29]
# # Declare an empty list that will store unique values
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list1)
# print(list2)

# tuple=1,2,3,4
# nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))
# print(tuple)
# print(tuple[3])
# #print(tuple[5])
# #print(tuple[1.0])
# print(nested_tuple[0][2])
# print(nested_tuple[1][1])
# print(nested_tuple[2][3])

#
# Days = set(["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
# print(type(Days))
# Days.add("wenusday" )
# Days.add("Thursday")
# Days.update(["Deva","Hima","Sekahr"])
# print(Days)
# Days.remove("wenusday")
# print(Days)
# #print("looping through the set elements ... ")
# # for i in Days:
#     print(i)

# # Creating a set which have immutable elements
# set1 = {1,2,3, "JavaTpoint", 20.5, 14}
# print(type(set1))
# print(set1)
# #Creating a set which have mutable element
# set2 = {1,2,3,(4,5,6)}
# print(type(set2))
# print(set2)

# Days1 = {'Wednesday', 'Tuesday', 'Sunday', 'Friday', 'Thursday', 'Monday', 'Saturday'}
# Days2 = {"Friday","Saturday","Sunday"}
# print(Days1^Days2)

# x = int(input("Insert any number: "))
#
# if x % 2 == 0:
#     print("This is an EVEN number!")
# else:
#     print("This is an ODD number!")


#    *
#   **
#  ***
# ****
#*****
# x=[' ',' ',' ',' ',' ']
# for i in range(0,len(x)):
#     print(' '*(len(x)-i)+'*')
#     # for j in range(,i+1):
#     #     print('*', end=' ')

# x=[[1,2,3],[4,5,6],100,200]
# for i in range(len(x)):
#     print(x[i],end=' ')

# x=list()
# x.append(1)
# x.append(3)
# #x[2]=5
# print(x)



# def java():
#     print("JAVA is good")
#     print("JAVA is good")
#     print("JAVA is good")
#
# java()

# def python():
#     print('Deav')
#     print('Hima')
# python()


# def add(a,b):
#     a=10
#     b=20
#     return a+b
# c=add()
#print(c)

#def mul(a,b):
#     return a*b
# print(mul(10,20))

# def sub(a,b):
#     print (a-b)
# sub(20,10)

# def add(a,b ):  # formal  (a,b)  (20,30)  a=20,b=30 c=100
#     print("a val", a)
#     print("b val", b)
#     print('C val',c)
# add(20,30,100)
#

# def my_function(*num):
#   print(num)
# my_function(1,2,3,4)


# def my_function(*kids):
#   print(kids)
# my_function("Emil", "Tobias", "Linus")

# def my_function(**num):
#   print(num)
# my_function( a=1, c=2, d=3, b=4)

# def java(**x):
#     print(list(x.keys()))
#     print(list(x.values()))
#
# java(a=10,b=20,c=30)


# def python(**a): # formal args
#     print(a.keys())
#     print(a.items())
#     return a
#
# x=python(a=10,b=30,c=40,d=20)     # keyword args
# print(x)



# def python(*x,**y): # formal args
#     # x=print(x)
#     # y=print(y)
#     return x,y
# x,y=python(1,2,3,4,5,a=10,b=30,c=40,d=20)     # keyword args
# print(x,y)

# def fact(n):
#     fact=1
#     while(n!=0):
#         fact=fact*n
#         n=n-1
#     return fact
#
# x=(eval(input("enter the number:")))
# val=fact(x)
# print("factorial of {} is : {}".format(x,val))

# a=100   # outside of fun
# def java():
#     print(a)
# java()
# a=a+200 # outside of fun
# def python():
#     print(a)
# python()
# a=300 # outside of fun
# def C():
#     print(a)
#C()

# a=200
# def python():
#     global a
#     x=100     # local
#     print(x)
#     a=a+20
#     print(a)
# python()
# def java():
#     global a
#     a=30+a
#     print(a)
# java()

# a=500
# def java():
#     a=100
#     print(a)
#     print(globals()['a'])
# java()


# a=100
# def python():
#     global a
#     a=200
#     a=500
#     print(a)
#     a=a+100
#     print(globals()['a'])
# python()

# def fact(n):
#     if n==0:
#         Result=1
#     else:
#         Result=n*fact(n-1)
#     return Result
#
# x=(eval(input("enter the number:")))
# val=fact(x)
# print("factorial of {} is : {}".format(x,val))


# def python(a):
#     return a*2
# val=python(4)
# print('val is :',val)
#
# b=lambda a:a*2
# print('val is :', b(5))
# y=list(filter(lambda a:a%2==0,range(0,15,4)))
# print(y)

#
# y=list(map(lambda a:a//2,range(1,5 )))
# print(y)

# from functools import reduce
# y=reduce(lambda a,b:a+b,range(1,11,2))
# print(y)

# def Devansh():
#     print("python is good")
# Dev=Devansh
# #Dev()
# def Hima():
#     print("Deva and Hima are brothers")
#     Dev()
# Hima()
#
# def Devansh():
#     def Hima():
#         print("Deva and Hima are brothers")
#     Hima()
#     print("python is good")
# Devansh()

# x=[1,5,6,8,3,2]
# y=[]
# z=[]
# for i in x:
#     if i%2==0:
#         y.append(i)
#         y.sort()
#     else:
#         z.append(i)
#         z.sort()
# out=y+z
# print(out)






# for i in y:
#     y.sort()
# print(y)
# for i in z:
#     z.sort()
#print(z)


class A:
    def __init__(self):
        self.x = 'A1B2c3'
        for i in self.x:
            if i.isdigit():
                print(i,end='')
        print()
        for i in self.x:
            if i.isalpha():
                print(i,end='')
        print()
        for i in self.x:
            if i.isalpha():
                print(ord(i),end='')
obj=A()

print("Hima")