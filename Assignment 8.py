# x={'A':'Deva','B':2011}
# print(x.get('A'))
# print(x.get('B'))


# x={'A':'Deva','B':2011}
# del x['B']
# print(x)


# x={'A':'Deva','B':'2011','C':'Hima','D':'1010'}
# x.pop('C')
# print(x)
# print(x.pop('A'))


# x={'A':'Deva','B':'2011','C':'Hima','D':'1010'}
# x.clear()
# print(x)

# x={'A':'Deva','B':'2000'}
# x['B']='2011'
# print(x)
# x.update({'C':'Hima'})
# print(x)
#
# x={'A':'Deva','B':'2000'}
# z=x.copy()
# print(z)
#

# x=['Deva','2011','Hima','1010']
# y=[1,2,3,4]
# z={}
# z=dict(zip(y,x))
# print(z)



#x={'A':1,'B':'5'}
# keys=list(x.keys())
# val=list(x.values())
# out={}
# for i in range(len(val)):
#     out[val[i]]=keys[i]
# print(out)

# x= {'1':['a','b'], '2':['c','d']}
# l1=x['1']
# l2=x['2']
# out=[]
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         temp=l1[i]+l2[j]
#         out.append(temp)
# print(out)



# x='EMBEDDED'
# y=list(x)
# print(type(y))
# final=[]
# for i in range(len(y)):
#     final.append(x.count(y[i]))
# print(final)
# z=dict(zip(y,final))
# print(z)


# x={'A':3,'C':4,'E':1,'B':5,'D':2}
# print(type(x))
# out=(dict(sorted(x.items())))
# print(out)
# a=list(x.keys())
# b=list(x.values())
# z=dict(zip(b,a))
# print(z)
# p=dict(sorted(z.items()))
# print(p)
# a=list(p.keys())
# b=list(p.values())
# z=dict(zip(b,a))
# print(z)


#
# x={'A': 'Red','D':None, 'B': 'Green', 'C': None}
# for key, value in dict(x).items():
#         if value is None:
#             del x[key]
# print(x)

# x={'A':123,'B':100}
# for key, value in dict(x).items():
#         if key=='A':
#             print(" Key is exist in the dict")
#         else:
#             print("for loop executed successfully")
#
#
# x='Hello PYTHON who ARE YOU'
# x=(x.upper())
# print(x)
# keys=[]
# values=[]
# x=x.split()
# print(x)
# for i in range(len(x)):
#     keys.append(x[i][0])
#     values.append(x[i])
# out=dict(zip(keys,values))
# print(out)



# x={'C1':[10,20,30],'C2':[20,30,40],'C3':[12,34]}
# keys=list(x.keys())
# val=list(x.values())
# for i in range(len(val)):
#     val[i].reverse()
# print(val)
# out=dict(zip(keys,val))
# print(out)

#
# x={1:'red',2:'green',3:'black',4:'white',5:'black'}
# out = {}
# for key, value in dict(x).items():
#     out[value]=len(value)
# print(out)

# def python(dic):
#     out = {}
#     for i in dic.values():
#         out[i]=len(i)
#     return out
# x={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print(x)
# print(python(x))










# x={'A':3,'B':5,'C':4,'D':2,'E':1}
# keys=list(x.keys())
# val=list(x.values())
# out={}
# for i in range(len(val)):
#     out[val[i]]=keys[i]
# print(out)