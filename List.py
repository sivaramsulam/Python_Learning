# list : list is a collection of hertroginious ele
#we can store multible values in list
# duplicates r allowed in list
# to access the list ele index is required [+,-]
#list having growable nature  -> we cn store num of ele
# list index starts from zero
# -ve index starts from -1 in reverse order
#syntax : list_name=[]

# x=[]   # this is called empty list
# print(type(x)) # list
# x=list()   # -> this is recommanded to use
# print(type(x))   #list
# x=[5,6,5,10]
# print(type(x))  # list
# print(x[0])     # 5
# print(x[2])     # 5
# print(x[3])     #10
# print(x[-2])    # 5
# print(x[-4])    # 5


# x=[1,10,2,20]
# print(type(x))  # List
# print(x)        # [1, 10, 2, 20]
# x.append(3)
# print(x)        # [1, 10, 2, 20, 3]
# x.append(1000)
# x.append(2000)  # [1, 10, 2, 20, 3, 1000, 2000]
# print(x)


# y=[]
# for i in range(1,6):
#     x=int(input(" enter x val :"))
#     y.append(x) # it will print the 5 numbers.
#     print(y)


# range(statrindx,end_indx,step)
# # # slicing
#x=[10,20,30,40,50]   # [20, 30, 40, 50]
# print(x[-2])
# print(x[3])
# print(x[1])
# print(x[-4])
#syntax x[start:end:step]
x=[10,20,30,40,50]
print(x[:])     # [10,20,30,40,50]
print(x[2:])    # [30,40,50]
print(x[1:4])   # [20, 30, 40]
# x=[10,20,30,10,50,10,30,20,10]
#
# print(x[3:8:2])
# print(x[:7])
# print(x[-4:])
# print(x[-5:-3])
# print(x[:-3])
# print(x[-4:])
# print(x[::2])
#x=[10,20,30,40,50]        # [20,30,40,50]
#print(x[1::2])
# print(x[:4])    # [10,20,30,40]
#print(x[:4:3])   # [10,20,30,40,50]
# #ending index can be anything
# x=[10,20,30,40,50]
# print(x[1:100:2])  # [10,20,30,40,50]

# x=[] # x=list()
# x.append(20) # append used for to add the ele in list
# x.append(10)
# x.append(20)
# x.append(30)
# x.append({'a':10,'b':30}) # we can add set,tuple,list,dict as a single ele
# print(x)
# print(len(x))  # len,min.max


# x=[10,100,30]
# x.append(40)  # append ele i added at lst
# print(x)
# x.append(100)
# print(x)
# print(len(x))
