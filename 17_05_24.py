# from abc import ABC, abstractmethod
# class A(ABC):
#         def __init__(self,x):
#                 self.x=x
#         @abstractmethod
#         def m1(self):
#                 pass
# class B(A):
#         def __init__(self,x,y):
#                super().__init__(x)
#                self.y=y
#         def m1(self):
#             return self.x + self.y
# print(B(9,2).m1())


# class A:
#     def m(self):
#         return 'A'
# class B:
#     def m(self):
#         return 'B' 
# class C(A):
#     # def m(self):
#     #     return 'C'
#     pass
# class D(B):
#     def m(self):
#         return 'D'
# class E(D,C):
#     # def m(self):
#     #     pass  
#     pass
 
# print(E().m())   # C, D


# class A:
#     def __init__(self):
#         pass
#     def m(self):
#         return 'm'
#     def m2(self):
#         # return 'm2'
#         return self.m()
# print(A().m2())
# def test():
#     return 'test1'
# a=A()
# a.m=test
# # a.m2=test
# print(a.m2())


# abstraction, inheritance, polymorphism, Encapsulation

# Encapsulation

# class SecureData:
#     def __init__(self, data):
#         self.__data = data
#         # self.__data = None

#     def get_data(self):
#         return self.__data

#     def set_data(self, data):
#         if self.validate(data):
#             self.__data = data
#     def validate(self, data):
#         if data > 10:
#             return True
#         # Add validation logic here
        

# s=SecureData(9)
# print(s.get_data())
# s.set_data(11)
# print(s.get_data())



# class A:
#     def m(self,x):
#         return f'data from database {x}'
#     def m2(self,y):
#         return self.m(y)
    
# a=A()
# # a1=a.m(10)
# # print(a1)
# a2=a.m2(10)
# print(a2)


# def decor(g):
#     print('1')
#     def inner(*args, **kwargs):
#         print('3')
#         return g(*args, **kwargs)*10
#     # def inner(c,d):
#     #     print('3')
#     #     return g(c,d)*10
#     print('2')
#     return inner

# @decor
# def f(a,b):
#     return a+b
# print(f(2,4))

# # @decor
# # def f(*args, **kwargs):
# #     # return args
# #     return kwargs
# # print(f(2,4,x=39))



################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################


# l=['a','b','c','d']

# for i in range(len(l)):
#     if l[i]=='c':
#         l[i]='e'
# print(l)

# l=['a','b','c','d']

# print(l.index('d'))
# l.insert(0,'e')        
# print(l)

# l.remove('b') 
# print(l)

# l.extend([10,20,30])
# print(l)             # ['a', 'c', 'd', 10, 20, 30]

# insert, extend, append

# l.append([10,20,30])    
# print(l)                 # ['a', 'c', 'd', [10, 20, 30]]

# l.clear()
# print(l)   # []


# print(id(l))
# l2= l.copy()
# print(l)
# l.append(3000)
# print(l)
# print(id(l2))
# print(l2)

# print(l.count('b'))

# print(l.index('b'))

# print(l)
# l.insert(1,10000)
# print(l)

# l.pop(1)
# print(l)


# l=['a','b','c','d']
# l.remove('c')
# print(l)

# remove, pop, clear
# extend, append, insert
# count, index, reverse, sort, copy

# l.reverse()
# print(l)

########################################################################################################3

# tuple

# t=(10,4,7,'a',30,40,'a')
# print(t)
# print(t.count('a'))
# print(t.index(30))


# set
# s=(10,20,30,'a')
# print(s)
# print(s.count('a'))
# print(s.index('a'))


# d={'a':10,'b':20,'c':30}
# d.pop('b')
# print(d)
# d.popitem()
# print(d)
# print(d.fromkeys(d,100))

# print(d.get('d'))  # None
# print(d['d'])      # KeyError: 'd'
# print(d.get('d', 'NA')) 

# print(d.items())
# print(type(d.items()))

# print(d.keys())
# print(type(d.keys()))

# print(d.values())
# print(type(d.values()))

# d.update({'b':200,'e':500})
# print(d)


##########################################################################################3

# String

# a='Pravin'

# print(a.index('P'))

# print(a.capitalize())
# print(a.find('r'))
# print(a.lower())
# print(a.split('a'))


# a='P,r,a,v,i,n'
# print(a.split(','))
# print(''.join(a.split(',')))
# print(','.join(a.split(',')))

# str='pravin'
# str1=str.replace('pra','abc')
# print(str1)

# str1[0]='z'  # type error

# l=[10,3,56,111,43,99,12,43,56,22]

# def f(l):
#     max=l[0]
#     for i in l:
#         if i>max:
#             max=i
#     return max
# print(f(l))


# def f(l):
#     max=s_max=t_max=float('-inf')
#     for i in l:
#         if i>max:
#             max=i
#         elif max>i>s_max:
#             s_max=i
#         elif max>s_max>i>t_max:
#             t_max=i
#     return max, s_max, t_max
# print(f(l))


# def f(l):
#     min=l[0]
#     for i in l:
#         if i<min:
#             min=i
#     return min
# print(f(l))


# l=[2,5,4,1,3]
# def f(l):
#     le=0
#     re=len(l)-1
#     n=len(l)//2
#     for i in range(n):
#         if le<re:
#             l[le],l[re]= l[re], l[le]
#         le+=1
#         re -=1
#     return l
# print(f(l))


# def f(*args, **kwargs):
#     print(args[0])
#     print(kwargs['y'])
#     # return args
#     # return kwargs
# # f(10,30,'a','x'=100,'y'=200)  
# # f('d',10,30,'a',x=100,y=200, 'c')  
# # f(x=100,y=200,'d',10,30,'a', 'c')  
# f('d',10,30,'a',x=100,y=200)  




# def decor(g):
#     def inner(*args, **kwargs):
#         return g(*args, **kwargs)
#     return inner

# @decor
# def f(*args, **kwargs):
#     return args, kwargs['a']
# print(f(10,4,1,a=100,b=200))


# def f(x):
#     yield x[0]
#     yield x[1]

# print([i for i in f([10,20,30,40])])

# def f(l):
#     yield l[0]
#     yield l[1]

# print([i *2  for i in f([10,20,30,40]) ])


# print([i   for i in [10,11, 13, 20,30,40 ] if i%2==0 ])

# print([ i if i%2==0  for i in [10,11, 13, 20,30,40 ]  ])  # SyntaxError

# print([ i if i%2==0 else 'odd'  for i in [10,11, 13, 20,30,40 ]  ])

# print([ i if i%2==0  elif i>100 'greater than 100' else 'odd'  for i in [10,11, 13, 20,30,40,102, 103 ]  ])
# print([i if i % 2 == 0 else 'greater than 100' if i > 100 else 'odd' for i in [10, 11, 13, 20, 30, 40, 111, 103]])
 # dont use elif in list comprehension 

# print([ i  if i%2==0 else 'more 40' if i>40 else 'odd' for i in [10,11, 13, 20,30,40,41,43 ]  ])
 
 
# s='Pravin'
# s1=''
# for i in s:
#     s1=i+s1
# print(s1)



# list1 = [1, 2, 3,5]
# list2 = [3, 4]

# # common_elements = set(list1) & set(list2)
# # print(type(common_elements))
# # print("Common elements:", list(common_elements))
# list3=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             list3.append(i)
# print(list3)










# list1 = [1, 2, 3,5]
# list2 = [3, 4]

# def f(list1,list2):
#     l=[]
#     for i in list1:
#         if i in list2:
#             l.append(i)
#     return l
# print(f(list1, list2))


# max=float('-inf')
# print(type(max))



# max=float('-inf')


# l=[1,2,3,4,5,6,7,8,9,10]
# k=3
# def f(l,k):
#     le=0
#     re=len(l)-1
#     f1(l,k,le,re)
#     le=0
#     re=k-1
#     f1(l,k,le,re)
#     le=k
#     re=len(l)-1
#     f1(l,k,le,re)
#     return l

# def f1(l,k,le,re):
#     for i in l:
#         if le<re:
#             l[le], l[re]=l[re], l[le]
#         le+=1
#         re-=1
# print(f(l,k))



# l=[9,1,2,0,3,0,5]   
                                      # O(n^2)
# def f(l):
#     for i in range(len(l)):
#         if l[i]==0:
#             del l[i]
#             l.append(0)
#     return l
# print(f(l))



# l=[9,1,2,0,3,0,5]     #[9,1,2,3,5,]   # l[4]
# def f(l):
#     le=0
#     for i in range(len(l)):
#         if l[i] !=0:
#             l[le]=l[i]
#             le+=1
#     print('le: ',le)
#     # print(l)
 
#     for i in range(le,len(l)):
#         l[i]=0
#     return l
# print(f(l))
    
    

# l=[1,0,3,0,0,5,8]

# def f(l):
#     n=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             l[n],l[i]=l[i],l[n]
#             n+=1
#     return l
# print(f(l))



# n=10
# def f(n):
#     n1=''
#     while n>0:
#         i=n%2
#         n=n//2
#         n1=n1+str(i)
#     return n1
# print(f(n))



# l=[2,8,10,5,1]
# k=9
# def f(l,k):
#     l2=[]
#     d={}
#     for i in range(len(l)):
#         if k-l[i] in d:
#            return [l[i], k-l[i]]
#         d[l[i]]=i 
#     return -1

# print(f(l,k))


# fibonachi  0,1,1,2,3,5,8,13,21

# def f(n):
#     n1=0
#     n2=1
#     l=[]
#     # if n>2:
#     for _ in range(n):
#         l.append(n1)
#         # l.append(n2)
#         n1,n2=n2, n1+n2
            
#     return l
# print(f(5))
            
        
        
# str=')(}[)'   # (([)])    (([])      (([]))     )(}[)   ([)]    [{(})]
# def isValid(s):
#     dict = { ')':'(', '}':'{', ']':'[' }
#     stack = []
#     for i in s:
#         if i in dict:
#             # Check if stack is empty before accessing stack[-1]
#             if stack and stack[-1] == dict[i]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(i)
#     return not stack
# print(isValid(str))


# other way:
# str='(([]))'   # (([)])    (([])      (([]))     )(}[)   ([)]    [{(})]

# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack
# print(isValid(str))

# stack=[]
# # stack=[1,2]
# def f(stack):
#     return not stack
# print(f(stack))


# import pandas as pd
# df=pd.DataFrame({'a':['aa','bb','cc'], 'b':['aaa','bbb','ccc']})
# print(df)
# df['c']=df['b'].apply(lambda x:len(x))
# print(df)

# l=['(']
# print(l[-1])
# print(l[0])



# class A:
#     def __init__(self,x):
#         self.x=x
#     def m1(self,y):
#         return self.x+self.y   # AttributeError: 'A' object has no attribute 'y'
# a=A(10)
# print(a.m1(12))
        
        

# class A:
#     def __init__(self,x):
#         self.x=x
#     def m1(self,y):
#         return self.x+ y 
# a=A(10)
# print(a.m1(12))



# class A:
#     def __init__(self,x):
#         self.x=x
#     def m1(self,y):
#         return self.x+ y 
#     def m2(self):
#         return self.m1(3)
# a=A(10)
# print(a.m2())



# class A:
#     def __init__(self,x):   
#         self.x=x
#     def m1(self,y):
#         print('2')
#         return self.x+ y 
#     def m2(self):
#         print('1')
#         return self.m1(3)
#     def m5(self):
#         return self.x
    
# class B(A):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y=y
    
#     # def __init__(self,y):
#     #     self.y=y
        
#     def m3(self):
#         return self.m2()
    
#     def m4(self):
#         return self.m5()
#         return 'from m4'
    
        
# # a=A(10)
# print(B(100,10).m4())



# class C(A):
#     def __init__(self,x,y) -> None:
#         self.x=x
#         super().__init__(y)
#     def sum(self):
#         self.z=self.x+self.y
#     def result(self):
#         return self.z
    
# c=C(10,20)
# print(c.result())




# class C(A):
#     def __init__(self,x1,x) -> None:
#         self.x1=x1
#         super().__init__(x)
#     def sum(self):
#         z =self.x1+self.x
#         return z
#     def result(self):
#         return self.sum()
    
# c=C(10,20)
# # print(c.sum())
# print(c.result())


# from abc import ABC, abstractmethod

# class A(ABC):
#     print('hi')
#     @abstractmethod
#     def m1(self):
#         pass
# class B(A):
#     def m2(self):
#         return '* m1 from A'
# print(B().m2()) # TypeError: Can't instantiate abstract class B with abstract method m1



# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# class B(A):
#     def m1(self):
#         return '* m1 from A'
# print(B().m1()) 



# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
# class B(A):
#     def m1(self):
#         return '* m1 from A'
#     def m2(self):
#         return '* m2 from A'
# print(B().m1()) 



# a='abc'
# class A:
#     a=4
#     def __init__(self,x):
#         self.x:int =x
#     def m1(self):
#         # return self.x
#         return a
# # print(A(10).a)
# # print(A.a)
# print(A(10).m1())


# a=10
# def f():
#     return a
# print(f())


# a=[10,20,30]
# def f():
#     a.append(40)
# print(f())
# print(a)


# a=[10,20,30]
# def f():
#     b=[10,20,30]
#     def f1():
#         a.append(40)
#         b.append(40000)
        
#     f1()
# f()
# print(a)
# # print(f().b)


# def f():
#     b=[10,20,30]
# f().b        # AttributeError: 'NoneType' object has no attribute 'b'



# def f():
#     global b
#     b=[10,20,30]
# f().b        # AttributeError: 'NoneType' object has no attribute 'b'


# def f():
#     global b
#     b=[10,20,30]
# f()
# print(b)



# a=[10,20,30]
# def f():
#     global b
#     b=[10,20,30]
#     def f1():
#         a.append(40)
#         b.append(40000)
        
#     f1()
# f()
# print(a)
# print(b)




# a='abc'
# class A:
#     a=4
#     def __init__(self,x):
#         self.x:int =x
#     def m1(self):
#         # return self.x
#         return a    # a= abc
#         return self.a    # a= 4
# # print(A(10).a)
# # print(A.a)
# print(A(10).m1())




# class Car:
#     wheels = 4  # Class attribute

#     def __init__(self, model):
#         self.model = model

#     @classmethod
#     def change_wheels(cls, new_wheels):  # Class method
#         cls.wheels = new_wheels

# car1 = Car("Sedan")
# print(car1.wheels)
# Car.change_wheels(6)  # Change class attribute via class method
# print(Car.wheels)
# print(car1.wheels)


# n=4, 0,1,1,2

# dp=[0] * (4+1)
# print(dp)
# dp[1]=1
# for i in range(2,4+1):
#     dp[i]=dp[i-1]+ dp[i-2]
# print(dp)



# class Car:
#     def __init__(self, model):
#         self.__model = model  # Private attribute

#     def __start_engine(self):  # Private method
#         print("Engine started.")

#     def get_model(self):  # Public method to access private attribute
#         return self.__model

# car = Car("Sedan")

# # Accessing private attribute from outside the class will raise an error
# # print(car.__model)  # AttributeError

# # Accessing private attribute using a public method
# print(car.get_model())  # Output: Sedan

# # Accessing private method via name mangling (discouraged)
# car._Car__start_engine()  # Output: Engine started.


# class A:
#     def a(self):
#         return 'aaa'

# def b(self):
#     return 'bbb'

# A.a=b
# print(A().a())


# x='a'+'b'
# print(x)
# x=2+3
# print(x)



#   Types of Polymorphism in Python:
#       Method Overriding (Runtime Polymorphism)
#       Method Overloading (Not Directly Supported, but can be simulated using default arguments)
#       Operator Overloading


# def add(a, b=0, c=3):
#         return a + b + c
    
# print(add(10))
# print(add(10,20,c=11))
# print(add(10,1,c=11))
# print(add(10))
# print(add(10,c=11))



# Polymorphism:
# class Animal:
#         def speak(self):
#                 pass
# class Dog(Animal):
#         def speak(self):
#                 return 'spark'
# class Cat(Animal):
#         def speak(self):
#                 return 'meow'   
   

# def f(animal):
#         return animal.speak()   
# dog=Dog()    
# cat=Cat()

# print(f(dog))             
# print(f(cat))             




# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# # Example usage
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)

# # Using the overloaded + operator
# v3 = v1 + v2
# print(v3)  # Output: Vector(4, 6)

# # Using the overloaded - operator
# v4 = v1 - v2
# print(v4)  # Output: Vector(-2, -2)




# class Vector:
#     def __init__(self,x,y) -> None:
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return (self.x+other.x,self.y+other.y)
#     def __sub__(self,other):
#         return (self.x-other.x,self.y-other.y)
#     def __repr__(self) -> str:
#         return f'Vector({self.x, self.y})'
# v1=Vector(10,12)
# print(v1)
# v2=Vector(4,7)
# print(v2)
# print(v1-v2)
# print(v1+v2)


# def f(n):
#     if n>=1:       
#         return n * f(n-1)
#     return 1
# print(f(4))


# def decor(f):
#     def inner(x):
#         # x1='pravin'
#         l=x.split(' ')
#         x='_'.join(l)
#         return f(x)
#         # return f(x1)
    
#     return inner

# @decor
# def str(a):
#     return a            
# print(str('ab c'))



# dict={'a':10,'b':20,'c':30}
# def f(dict,x):
#     for v in dict.values():
#         if v ==x:
#             return v
#     else:
#         return f'value {x} not in {dict}'
# print(f(dict,30))
# print(f(dict,300))



# dict={'a':10,'b':20,'c':30}
# def f(dict,x):
#     for v in dict.values():
#         if v==x:
#             return f'value {x} in {dict}'
#         else:
#             raise ValueError
#         except: ValueError:
#             print(f'value {x} not in {dict}')
# print(f(dict,30))
# print(f(dict,300))



# dict={'a':10,'b':20,'c':30}
# def f(dict,x):
#     for v in dict.values():
#         if v ==x:
#             return f'value {x} in dictionary'
#     else:
#         raise ValueError (f'value {x} not in dictionary')
              
# try:        
#     print(f(dict,30))
#     print(f(dict,300))
# except ValueError as v:
#     print(f'{v}')


# sum of two 
# class Solution:
#     def twoSum(self, nums, target):
#         numMap = {}
#         n = len(nums)

#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i
#         print(numMap)
#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]

#         return []  # No solution found

# print(Solution().twoSum([3,3],6))



# l=[8,2,5,7]
# k=12
# def f(l,k):
#     d={}
#     for i in range(len(l)):
#         d[l[i]]=i
#     for i in l:
#         if k-i in d:
#             return [d[i], d[k-i]]
# print(f([8,2,5,7],12))
# print(f([8,8],16))    # [1, 1]  wrong
# print(f([8,2,9,7],16))  # [0, 0]  wrong

# Interview Questions:-

# l=[8,2,5,7]
# k=12
# def f(l,k):
#     d={}
#     for i in range(len(l)):
#         d[l[i]]=i
        
#     for i in range(len(l)):
#         if k-l[i] in d and d[k-l[i]] !=i:
#             return [i, d[k-l[i]]]
# print(f([8,2,5,7],12))
# print(f([5,5],10))
# print(f([8,2,9,7],16))  # i=0, l[i]=8, k-l[i]=16-8=8, d[8]---0 

# Find the Duplicate Number
# l= [4,3,2,7,8,2,3,1]
# def f(l):
#     list=[]
#     d={}
#     d1={}
#     for i in l:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     for i,v in d.items():
#         if v>1:
#             # list.append(i)
#             d1[i]=v
#     # return list
#     return d1
# print(f(l))



# Revrse the list

# l=[10,3,2,7,9,1]
# def f(l):
#     le=0
#     re=len(l)-1
#     for i in l:
#         if le<re:
#             l[le],l[re]=l[re],l[le]
#         le+=1
#         re-=1
#     return l

# print(f(l))






# l=[1,2,3,4,5]
# print(l[1:])     # [2, 3, 4, 5]
# print(l[1::2])     # 
# print(l[3:1:-1])   # 
# print(l[4::-2])   #
# print(l[50::-2])   #
# print(l[1::2])   #

# x='-'.join('pravin')
# print(x)


# l=['p','r','a','v','i','n']
# s=''.join(l)
# print(s)
    
# x=(char.lower() for char in 'pra' if char.isalnum())
# print(x)
# print(''.join(x))



# # palindrom string
# s = "A man, a plan, a canal: Panama"
# # s='prarp'
# def f(s):
#     s1=''
#     for i in s:
#         if i.isalnum():
#             s1=s1+i.lower()
#             # print(i.lower(),end='') # amanaplanacanalpanama
#     print(s1)
#     if s1==s1[::-1]:
#         return 'palindrom'
# print(f(s))


# for number palindrom
# def isPalindrome(x):
#     if x < 0:
#         return False
        
#     return str(x) == str(x)[::-1]
# print(isPalindrome(121))
# print(isPalindrome(-121))


#other way to it:
# x=-121
# print(type(str(x)))



# def isPalindrome(x):
#         x=str(x)
#         n=x[::-1]
#         print(n)
#         if x == n:
#             return True
#         else:
#             return False
# print(isPalindrome(-121))

# print(2%10)


# def rotate(nums, k):
#         n = len(nums)
#         k = k % n  # This handles cases where k > len(nums)

#         # Step 1: Reverse the entire list
#         le, ri = 0, n - 1
#         while le < ri:
#             nums[le], nums[ri] = nums[ri], nums[le]
#             le += 1
#             ri -= 1

#         # Step 2: Reverse the first k elements
#         le, ri = 0, k - 1
#         while le < ri:
#             nums[le], nums[ri] = nums[ri], nums[le]
#             le += 1
#             ri -= 1

#         # Step 3: Reverse the remaining n - k elements
#         le, ri = k, n - 1
#         while le < ri:
#             nums[le], nums[ri] = nums[ri], nums[le]
#             le += 1
#             ri -= 1

# nums = [1,2,3,4,5,6,7], 
# k = 3
# rotate([1,2,3,4,5,6,7], 3)
# print(nums)

# nums = [1,2,3,4,5,6,7]
# print(id(nums))             # 2279119022080
# print(id([1,2,3,4,5,6,7]))  # 2279122511232

# tup = (1,2,3,4,5,6,7)
# print(id(tup))              # 2279119353984
# print(id((1,2,3,4,5,6,7)))  # 2279119353984

# x=nums is [1,2,3,4,5,6,7]
# print(x)   # False 
# x= nums == [1,2,3,4,5,6,7]
# print(x)   # True


# x=tup is (1,2,3,4,5,6,7)  
# print(x)   # True 
# x= tup == (1,2,3,4,5,6,7)
# print(x)   # True


'''
Note: When id is same of two object then "is" operator is "True", otherwise "False"

'''

# Custom iterator:
# class Even:
#     def __init__(self,max):
#         self.n=0
#         self.max=max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<self.max:
#             result=self.n
#             self.n=result+2
#             return result
#         else:
#             raise StopIteration
            
# even=Even(10)
# number=iter(even)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

# # for i in even:
# #     print(i)

# l=list()
# print(dir(l))


'''
next is not the nethod of list. list is not iterstor, it is iterable but 
by using iter() function or __iter__() method you create iterater. nwxt is method of iterator 

 '''
# list=[1,2,3]
# x=list.__iter__()
# print(dir(x))


# # hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__',
# # '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# # '__setstate__', '__sizeof__', '__str__', '__subclasshook__']

# print(x.__next__())

# # list.__iter__() and iter(list) are same
# # x.__next__() and next(x) are same



# How for loop work internally:
# l=[1,2,3,4]
# n=iter(l)
# while(True):
#     try:
#         print(next(n))
#     except StopIteration:
#         # print(f'{StopIteration}')
#         break


# break and continue
# def f():
#     for i in [1,2,3,4]:
#         if i%2==0:
#             continue
#         print(i)      
#         break
# print(f())



# Generator

# def gen(n):
#     n1, n2 = 0, 1  # Initialize n1 and n2 before the loop
#     while n1 < n:
#         yield n1
#         n1, n2 = n2, n1 + n2  # Update n1 and n2 for the next iteration

# # Create the generator instance
# fibonacci_gen = gen(10)

# # Call next() on the same generator instance
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))

# for i in fibonacci_gen:
#     print(i,end=' ')



# dict={'a':30,'b':4,'c':8,'d':10}
# dict1={'b':400,'c':800,'d':1000}

# dict['a']=dict1.get('a', dict['a'])
# dict['a']=dict1.get('a',99)
# print(dict['a'])    # 99


''''
**dict is a way to unpack a dictionary into keyword arguments

dict = {'a': 30, 'b': 4, 'c': 8, 'd': 10}
some_function(**dict)   -------->> some_function(a=30, b=4, c=8, d=10)

Practical Use Case Example: 
def example_function(a, b, c, d):
    print(a, b, c, d)

example_function(**dict)
# Equivalent to:
example_function(a=30, b=4, c=8, d=10)
# output:
30 4 8 10

'''

# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

# nums = [3,4,1,6,5,2] 
# nums = [1,5,4,5]
# output= (5-1)*(4-1)=12

# def f(nums):
#     s_max=float('-inf')
#     maxval=float('-inf')
#     for i in nums:
#         if i>= maxval:
#             s_max=maxval
#             maxval=i   #
#         elif i> s_max:
#             s_max=i
    
#     # print(maxval, s_max)
#     return (maxval-1)*(s_max-1)
# print(f(nums))



# input:
# file_1.txt
# line1
# line2
# line3
# line4
# line5

# output:
# file_2.txt
# line1
# line2
# line4
# line5

# # Read from file_1.txt and write to file_2.txt, omitting the third line
# with open('file_1.txt', 'r') as file:
#     lines = file.readlines()  # Read all lines into a list

# # Remove the third line (index 2)
# lines.pop(2)  # Removes "line3" (third line)

# # Write the modified lines to file_2.txt
# with open('file_2.txt', 'w') as file:
#     file.writelines(lines)  # Write the updated list of lines


# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# l=[[1,3],[2,6],[8,10],[15,18]]
# l=[[1,4],[5,6],[8,13]]
# def f(l):
#     merge=[]
#     l.sort(key=lambda x:x[0])
#     print(l)
#     pre=l[0]
#     if pre[1]<l[1][0]:
#         merge.append(pre)
#     for i in range(1,len(l)):
#         if pre[1]>= l[i][0]:
#             print('l[i]: ',l[i], '********************************pre: ',pre)
#             interval=max(pre[1],l[i][1])
#             pre[1]=interval
#             print('@@@@',pre)
#             merge.append(pre)
#             pre=l[i]
#             print('pre:------------------------------------------------------------',pre)
#         else:
#             merge.append(l[i])
#     return merge
# f(l)
        
        

# intervals= [[1,4],[0,2],[3,5],[6,9],[7,10]] 
# def merge(intervals):        
#     merged = []
#     intervals.sort(key=lambda x: x[0])
#     prev = intervals[0]
#     for interval in intervals[1:]:
#         if interval[0] <= prev[1]:  # 0 < 2
#             prev[1] = max(prev[1], interval[1])  # =1,5
#         else:
#             merged.append(prev)
#             prev = interval
#     merged.append(prev)
#     return merged
# print(merge(intervals))        
   
   
   
        
# a= [1, 2, 3, 5, 6, 8, 10, 11]
# def f(a):
#     l=[]
#     temp=[a[0]]
#     for i in range(1,len(a)):
#         if a[i]-a[i-1]==1:
#             temp.append(a[i])
#         else:
#             l.append(temp)
#             temp=[a[i]]
#     l.append(temp)
#     return l 
# print(f(a))



# l=[1,2,3,4,5,6,7,8,9]
# print(l[::3])




# x=[1,2,4,10]
# y=[2,1,10,4]
# print(id(x))   # 2596757342208
# print(id(y))   # 2596757488960   # for both  False

# if x==y and x is y:
#     print('for both ',True)
# elif x == y:
#     print('for == : ',True)
# elif x is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)




# x=[1,2,4,10]
# y=[1,2,4,10]
# print(id(x))   
# print(id(y))  # for ==:  True   but different id

# if x==y and x is y:
#     print('for both ',True)
# elif x == y:
#     print('for == : ',True)
# elif x is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)




# x=[]
# y=[]
# print(id(x))   
# print(id(y))  # for ==:  True   but different id

# if x==y and x is y:
#     print('for both ',True)
# elif x == y:
#     print('for == : ',True)
# elif x is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)



# x=[1,2,3]
# y=[1,2,3]
# z=y
# print(id(x))   
# print(id(y))  # for ==:  True  for x, y but different id
# print(id(z))   # id same for y and z


# if x==y and x is y:
#     print('for both ',True)
# elif x == y:
#     print('for == : ',True)
# elif x is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)




# x=[1,2,3]
# y=[1,2,3]
# z=y
# print(id(x))   
# print(id(y))  # for both  True:  True  for y,z 
# print(id(z))   # id same for y and z


# if z==y and z is y:
#     print('for both ',True)
# elif z == y:
#     print('for == : ',True)
# elif z is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)





# x=[1,2,3]
# y=[1,2,3]
# z=y
# print(id(x))   
# print(id(y))  # for == :  True:  True  for x,z 
# print(id(z))   # id same for y and z


# if z==x and z is x:
#     print('for both ',True)
# elif z == x:
#     print('for == : ',True)
# elif z is x:
#     print('for is: ',True)
# else:
#     print('for both ',False)





# x=[]
# y=[]
# z=y
# print(id(x))   
# print(id(y))  # for both  True   same id  for y,z
# print(id(z))

# if z==y and z is y:
#     print('for both ',True)
# elif z == y:
#     print('for == : ',True)
# elif z is y:
#     print('for is: ',True)
# else:
#     print('for both ',False)




# x=[]
# y=[]
# z=x
# print(id(x))   
# print(id(y))  # for both  True   same id  for z,x
# print(id(z))

# if z==x and z is x:
#     print('for both ',True)
# elif z == x:
#     print('for == : ',True)
# elif z is x:
#     print('for is: ',True)
# else:
#     print('for both ',False)




# x=(1,2,3,4)
# y=(2,1,4,3)
# print(id(x))   
# print(id(y))  # for both  False
# # print(id(z))

# if y==x and y is x:
#     print('for both ',True)
# elif y == x:
#     print('for == : ',True)
# elif y is x:
#     print('for is: ',True)
# else:
#     print('for both ',False)






# x=(1,2,3,4)
# y=(1,2,3,4)
# print(id(x))   
# print(id(y))  # for both  True
# # print(id(z))

# if y==x and y is x:
#     print('for both ',True)
# elif y == x:
#     print('for == : ',True)
# elif y is x:
#     print('for is: ',True)
# else:
#     print('for both ',False)



# x=(1,2)
# y=(1,2)
# print(id(x))
# print(id(y))   # different id
# # 2087986692544
# # 2087986692544



# x=(1,2)
# y=(1,2)
# z=y
# print(id(x))
# print(id(y))   # same id for 3
# print(id(z))
# # 2003388694976
# # 2003388694976
# # 2003388694976



# x=(1,2,[10,20])
# y=(1,2,[10,20])
# print(id(x))
# print(id(y))      # different id
# # 2362721930304
# # 2362729846592



# x=(1,2,[10,20])
# y=(1,2,[10,20])
# z=y
# print(id(x))
# print(id(y))      # same id for z and y
# print(id(z))
# 2871398206592
# 2871406053376
# 2871406053376


# x=[1,2]
# y=[1,2]
# z=y
# print(id(x))
# print(id(y))   # same id for 3
# print(id(z))
# # 2003388694976
# # 2003388694976
# # 2003388694976
# if z==x:          # True
#     print(True)



# x=[1,2]
# y=[1,2]
# z=y
# z=x
# print(id(x))
# print(id(y))
# print(id(z))


# x=(1,2)
# y=(1,2)
# z=y
# print(id(x))
# print(id(y))
# print(id(z))

# x=(1,2,[10,20])
# y=(1,2,[10,20])
# z=y
# print(id(x))
# print(id(y))
# print(id(z))


# x='pravin'
# y='pravin'
# z=y
# print(id(x))
# print(id(y))
# print(id(z))




# x=(1,2,[10,20])
# print(id(x))
# y=x
# x[2].append(30)
# print(x)
# print(y)
# print(id(x))
# print(id(y))



# x=[1,2,[10,20]]
# print(id(x))
# y=x
# x[2].append(30)
# print(x)
# print(y)
# print(id(x))
# print(id(y))



# x=[1,2,[10,20]]
# print(id(x[2]))
# y=x
# x[2].append(30)
# print(x)
# print(y)
# print(id(x[2]))
# print(id(y[2]))


# a=[1,2,3]
# def f(x):
#     x.append(4)
#     return x
# print(f([1,2,3]))
# print(a)



# a=[1,2,3]
# def f(x):
#     x.append(4)
#     return x
# print(f(a))
# print(a)



# def f():
#     for i in range(4):
#         if i==2:
#             print('two')
#         print(i)
# f()


# def f():
#     for i in range(4):
#         if i==2:
#             print('two')
#         else:
#             print(i)
# f()



# l=['a','b','c']
# l+=['d']
# print(l)



# list1=[3,2,10,19,7,5,13,17,12, 14, 4]
# l1=list1.sort()
# print(list1)

# def prime(list1):
#     list2=[]
#     for i in list1:
#         if i>1:
#             for j in range(2,i):
#                 if i % j ==0:
#                     break
#             else:
#                 list2.append(i)
#     list2.sort()
#     return list2      
# print(prime(list1))



"""
quetion:
input:

def print_something(s, kwr = 1):
    for i in range(0,kwr):  print(s.upper())
    
print_something function is given above, after applyong decorator, output should be following:
abcdw
abcdw
abcdw
"""
# def decor(f):
#     def inner(str1,kwr = 1):
#        str1=str1.lower()
#        return f(str1,kwr)
#     return inner

# @decor
# def print_something(s, kwr = 1):
#     # for i in range(0,kwr):  print(s.upper())
#     for i in range(0,kwr):  print(s.upper())
    
# print_something('aBcdW', kwr = 3)
##  not getting proper solution for above




# def decor(f):
#     def inner(str1, kwr=1):
#         # Convert the string to lowercase before passing it to the function
#         # str1 = str1.lower()
#         return f(str1, kwr)  # Call the original function
#     return inner

# @decor
# def print_something(s, kwr=1):
#     for i in range(0, kwr):
#         print(s)  

# # Call the decorated function
# print_something('abcdW', kwr=3)




# def decor(f):
#     def inner(*args, **kwargs):  # Flexible argument handling
#         # print(args)
#         args = (args[0].lower(),) + args[1:]  # Convert the first argument to lowercase
#         f(*args, **kwargs)  # Pass all arguments to the original function
#     return inner

# @decor
# def print_something(s, kwr=1):
#     for i in range(0, kwr):
#         print(s)  # Remains unchanged

# print_something('abcdW',kwr=3)


""""
for keyword arguments, the inner function in a decorator must accept the same keyword argument 
names as the decorated function if you are not using flexible arguments like **kwargs

Keyword arguments rely on names. If the inner function doesn't explicitly define the same 
keyword argument names, Python won't know how to map the passed arguments, leading to an error.

otherwise use *args and **kwargs for Flexibility for inner function

"""




# list1=[{"name":"name1","employee_age":32,"salary":"2000"},

# {"name":"name2","employee_age":36,"salary":"4000"},

# {"name":"name3","employee_age":31,"salary":"500"}, {"name":"name4","employee_age":28,"salary":"200"}]


# def fun(list1):
#     for dict1 in range(len(list1)):
#         for dict2 in range(0, len(list1)-dict1-1):
#             if list1[dict2]['employee_age']>list1[dict2+1]['employee_age']:
#                 list1[dict2]['employee_age'], list1[dict2+1]['employee_age']= list1[dict2+1]['employee_age'],list1[dict2]['employee_age']
#     return list1
   
# print(fun(list1))




# list1 = [
#     {"name": "name1", "employee_age": 32, "salary": "2000"},
#     {"name": "name2", "employee_age": 36, "salary": "4000"},
#     {"name": "name3", "employee_age": 31, "salary": "500"},
#     {"name": "name4", "employee_age": 28, "salary": "200"},
# ]

# # Sort by employee_age in ascending order
# sorted_list = sorted(list1, key=lambda x: x["employee_age"])

# # Print the sorted list
# print(sorted_list)



# list2= sorted(list1, key= lambda x: x['employee_age'])
# print(list2)

# list2= sorted(list1, key= lambda x: x['employee_age'], reverse=True)
# print(list2)

# list2= sorted(list1, key= lambda x:x['salary'])
# print(list2)


# def get_employee_age(employee):
#     return employee["employee_age"]

# sorted_list = sorted(list1, key=get_employee_age)
# print(sorted_list)


# l=[10,5,2,11,8,9]
# l.sort(reverse=True)
# print(l)


# list1 = [
#     {"name": "name1", "employee_age": 32, "salary": "2000"},
#     {"name": "name2", "employee_age": 36, "salary": "4000"},
#     {"name": "name3", "employee_age": 31, "salary": "500"},
#     {"name": "name4", "employee_age": 28, "salary": "200"},
# ]

# list1.sort(key=lambda x:x['employee_age'])
# print(list1)



# class A:
#     def print1(self):
#         print('calling from A')
# class B(A):
#     def print1(self):
#         print('calling from B')
# class C(B,A):
#     pass

# c=C()
# c.print1()     # calling from B

# print(C.mro())


'''
Consistent MRO:

1. The inheritance B, A means Python will first check B for methods and attributes, then A.
2. Since B inherits from A, the MRO for C is consistent: C -> B -> A.
3. Python can resolve the print1 method correctly without any ambiguity.


'''





# class A:
#     def print1(self):
#         print('calling from A')
# class B(A):
#     def print1(self):
#         print('calling from B')
# class C(A, B):
#     pass

# c=C()
# c.print1()  # TypeError: Cannot create a consistent method resolution 
            # order (MRO) for bases A, B

'''
Inconsistent MRO:
1. Python tries to build the MRO for class C based on its inheritance (A, B).
2. Class B already inherits from A. By declaring C(A, B), 
Python detects a conflict because the linearization of the classes (C -> A -> B) violates the MRO rules.
3. Python raises an error indicating that the MRO is inconsistent.

'''

# print(C.mro())


# str1='abccdeeffg'
# def f(str1):
#     set1= set()
#     left= max1= 0
#     for right in range(len(str1)):
#         while str1[right] in set1:
#             set1.remove(str1[left])
#             left +=1
#         else:
#             set1.add(str1[right])
#         max1= max(max1, right-left+1)
#     return max1
# print(f(str1))


# def f():
#     l=[10,20,30]
#     try:
#         return l[5]
#     except IndexError as er: 
#         return f'{er}: value not found'
# print(f())


# l=[10,20,30]
# # print(l[5])
# # print(l.index(29))   # ValueError: 29 is not in list
# print('hi')



# def f():
#     num = int(input('enter a number: '))  # User might enter non-numeric input
#     if num < 0:
#         raise ValueError("Negative numbers are not allowed.")  # Raising an exception
#     return f"The number is: {num}"


# try:
#     print(f())
# except ValueError as e:  # Catching specific exception
#     print(f"Error: {e}")


# x = int(input("Enter a number greater than 10: "))

# class CustomError(Exception):
#     pass


# def f():
#     x = int(input("Enter a number greater than 10: "))
#     if x <= 10:
#         raise CustomError("The number must be greater than 10.")
#     return f'{x} is valid number'



# try:
#     print(f())
# except CustomError as e:
#     print(f"CustomError: {e}")
# except ValueError as e:  # Catching other exceptions
#     print(f"Value error: {e}")
# except Exception as e:  # Catching other exceptions
#     print(f"Unexpected error: {e}")



# try:
#     n=int(input('number: '))
#     if n==0:
#         raise AttributeError('this is atrribute error')
#     print(n)
# except AttributeError as at:
#     print(f'Error: {at}')

# # Raising an Exception to Propagate It
# def check_number(num):
#     try:
#         if num < 0:
#             raise ValueError("Negative number not allowed.")
#         return num
#     except ValueError as e:
#         print(f"Error caught in function: {e}")
#         raise  # Re-raises the exception

# try:
#     print(check_number(5))
#     print(check_number(-5))
#     print(check_number('qcqdq'))
# except ValueError as e:
#     print(f"Error caught in main: {e}")



# remove odd keys from dictionay

# d={1:10, 2:21, 3:23, 4:54, 5:'dc', 6:43}

# d1={ k:v  for k,v in d.items() if k%2 !=0 }
# print(d1)

# dictionay can't modified when iterating over it

# for i in list(d.keys()):
#     if i%2==0:
#         del d[i]
# print(d)



# file = open('sample.txt', 'r')
# x=file.read()
# print('x:',x)
# # print('file',file)
# # print(file.close())
# file.close()
# # print('x',x)
# # print('file',file)


# with open('sample.txt','r') as file:
#     x=file.read()
#     print(x)

# print(file.close())    # 






# class A:
#     y=29
#     def __init__(self) -> None:
#         self.x='1000'
#         self.z=self.y
        
# print(A().x)
# print(A().y)
# print(A.y)
# print(A().z)



# l=[4,7,1,8,3,9,2,0,9]
# def f(l):
#     s_max=max= float('-inf')
#     for i in l:
#         if i >max:
#             s_max=max
#             max=i
#         elif max>i>s_max:
#             s_max=i
#     return (max,s_max)
# print(f(l))


# l=[2,5,4,5,6,9]
# k=10
# def f(l,k):
#     d={}
#     for n1 in l:
#         n2= k-n1
#         if n2 in d and n1 !=n2:
#             return (n1, n2)
#         else:
#             d[n1]=True
# print(f(l,k))



# class A:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         if isinstance(other, A):
#             return self.x+ other.x
# a=A(13)
# b=A(7)
# print(a+b)


# list1=[{"name":"name1","employee_age":32,"salary":"2000"},

# {"name":"name2","employee_age":36,"salary":"4000"},

# {"name":"name3","employee_age":31,"salary":"500"}, {"name":"name4","employee_age":28,"salary":"200"}]

# list2= sorted(list1, key=lambda x:x["employee_age"])
# print(list2)



# dict1={'m':13, 'a': 10, 'p':16, 'c': 3, 'b': 2 }
# # sort by value

# list1= dict1.items()  # list  [('m', 13), ('a', 1), ('p', 16), ('c', 3), ('b', 2)]
# # print(list1)
# # list2= sorted(list1)
# # print(list2)

# list3= sorted(list1, key= lambda x:x[1])
# print(list3)
# print(dict(list3))   # {'b': 2, 'c': 3, 'a': 10, 'm': 13, 'p': 16}

# def f(n):
#     a,b=0,1
#     for _ in range(5):
#         print(a, end=' ')
#         a,b=b,a+b
# f(4)  # 0,1,1,2,3,5


# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
# print(f(5))


# l=[2,5,5,3,3,4,1]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)


# l=[100,20,300,40]
# d=enumerate(l)
# l1=list(d)

# l1.sort(key= lambda x:x[1])
# print(l1)

# l2=sorted(l1, key= lambda x:x[1])
# print(l2)

# d={'a':21,'b':12, 'c':32, 'd':20}
# d1=d.items()
# # print(type(d1))
# # # print(list(d1))
# # # l1=list(d1)
# d2=sorted(d1,key=lambda x:x[1])
# # print(d2) # [('b', 12), ('d', 20), ('a', 21), ('c', 32)]
# print(dict(d2))  # {'b': 12, 'd': 20, 'a': 21, 'c': 32}



# l=[100,20,300,40]
# # l='abcde'
# d=enumerate(l)
# l1=list(d)
# print(l1)
# d1=dict(l1)
# print(d1)


# s='abcdd'
# d={}
# for i,v in enumerate(s):
#     d[i]=v
# print(d)


# s='abccdde'
# def f(s):
#     set1=set()
#     left=max1=0
#     for right in range(len(s)):
#         while s[right] in set1:
#             set1.remove(s[left])
#             left+=1
         
#         set1.add(s[right])
#         max1=max(max1, right-left+1)    
#     return max1
# print(f(s))


# l=[10,20,30]
# print(list(enumerate(l)))


# l=[1,2,3,4,5,6,7]
# k=3
# def f(l,left,right):
#     while right>left:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
#     return l
# print(f(l,0,len(l)-1))
# print(f(l,0,k-1))
# print(f(l,k,len(l)-1))

# l1=[1,2,3]
# l2=[4,5,6]
# l3=zip(l1,l2)
# l4=[i+v for i,v in l3]
# print(l4)


# n=5
# for i in range(n):
#     # print(n*'*')
#     # print(i*' ',n*'*')
#     n-=1

# for i in range(n):
#     print(' '*i + '*'*(n-i) )

# for i in range(n):
#     print(    '' * i    +    '* ' * n + '0' * i   ) # print('0'*i + '*1'*n + '0'*i)
#     n=n-1    

    
# for i in range(n):
#     print('0'*i + '*1'*n + '0'*i) 
#     n=n-1


"""
SELECT age,  country
FROM Customers group by country order by age desc;

select first_name , max(age) as age, country from Customers group by country
    
    
"""
'''
select max(age), country from Customers where age <
(select max(age) from Customers c2 where c2.country= country) group by country
'''

'''
SELECT 
    c1.country, 
    COALESCE(
        (SELECT MAX(age) 
         FROM Customers c2 
         WHERE c2.country = c1.country 
           AND c2.age < (SELECT MAX(age) FROM Customers c3 WHERE c3.country = c1.country)
        ), 
        (SELECT MAX(age) FROM Customers c2 WHERE c2.country = c1.country)
    ) AS age
FROM Customers c1
GROUP BY c1.country;

'''


# def decor(g):
#     def inner(x,y):
       
#         a1,b1=x*x,y*y
#         print(g(a1,b1))
#         return True
#     return inner

# @decor
# def f(a,b):
#     return a+b
# print(f(2,3))


"""
Write a Python program that takes a list of integers and returns a new list with each integer squared. However, if the squared value is greater than 50, replace it with the string 'Over 50'. The program should handle any exceptions that may arise from incorrect inputs gracefully without using inbuilt functions.
 
input_numbers = [1, 7, 8, 4, 'a', 3]
 
Output - [1, 49, 'Over 50', 16, 'Invalid input: Not an integer', 9]
has context menu
"""

# input_numbers = [1, 7, 8, 4, 'a', 3]
# def f(input_numbers):
#     l1=[]
#     for i in input_numbers:
#         try:
#             if isinstance(i,int):
#                 if i*i<50:
#                     l1.append(i*i)
#                 else:
#                     l1.append('Over 50')
#             else:
#                 raise ValueError('Invalid input: Not an integer')
#         except ValueError as e:
#                 l1.append(str(e))
            
#     return l1
# print(f(input_numbers))

# print(type(ValueError('Invalid input: Not an integer')))




# nums = [1,3,4,4,2,2,7,7,7,7] 
# # Output: [2,4,7]
# def f(nums):
#     d,n,l,l2,l3={},1,[],[],[]
#     for i in nums:
#         if i not in d:
#             d[i]=n
#         else:    
#             d[i]=d[i]+1
#     for i,v in d.items():
#         if v>1:
#             l.append(i)
#         else:
#             l2.append(i)
#     return l, l2

# print(f(nums))



# nums = [1,3,4,4,2,2,7,7,7,7]  
# # Output: [1,3,4,2,7]
# def f(nums):
#     d,n,l,l2,l3={},1,[],[],[]
#     for i in nums:
#         if i not in d:
#             d[i]=n
#         else:    
#             d[i]=d[i]+1
#     for i,v in d.items():
#         l.append(i)
#     return l
# print(f(nums))



# nums = [1,3,4,4,2,2,7,7,7]
# def f(nums):
#     s,l1=[],[]
#     for i in nums:
#         if i not in s:
#             s.append(i)
#         else:
#             l1.append(i)
#     return s
# print(f(nums))


# l = [1,3,4,4,2,2,7,7,9,9,9]
# def f(l):
#     s_max=max=float('-inf') # <class 'float'>
#     for i in l:
#         if max<i:
#             max, s_max=i , max
#         elif s_max<i and i!= max:
#             s_max=i 
#     return max,s_max   
# print(f(l))   



# class CustomError(Exception):
#     pass

# input_numbers = [1, 7, 8, 4, 'a', 3]
# def f(input_numbers):
#     l1=[]
#     for i in input_numbers:
#         try:
#             if isinstance(i,int):
#                 if i*i<50:
#                     l1.append(i*i)
#                 else:
#                     l1.append('Over 50')
#             else:
#                 raise CustomError('Invalid input: Not an integer')
#         except CustomError as e:
#                 l1.append(str(e))
#     return l1
# print(f(input_numbers))




# l1=l2=[]
# l1.append(1)
# l2.append(2)
# print(l1)
# print(l2)


# x=[]
# y=[]
# z=y
# print(id(z),id(y))
# z=x
# print(id(z),id(x))

# t1=()
# t2=()
# t3=t2
# print(id(t1),'\n',id(t2),'\n',id(t3))


# t1=(1,2)
# t2=(1,2)
# t3=t2
# print(id(t1),'\n',id(t2),'\n',id(t3))

# t1=(1,2,[])
# t2=(1,2,[])
# t3=t2
# print(id(t1),'\n',id(t2),'\n',id(t3))
# print(id(t1[2]),'\n',id(t2[2]),'\n',id(t3[2]))
# print(id(t1[1]),'\n',id(t2[1]),'\n',id(t3[1]))



# t1=(1,2,[])
# print(id(t1[2]))
# t1[2].append(1)
# print(id(t1[2]))

# t1=[1,2,[]]
# print(id(t1[2]))
# t1[2].append(1)
# print(id(t1[2]))


# x=(1,2,[])
# y=x
# x[2].append(1)
# print(id(x[2]),id(y[2]))

# t1=(1)
# t2=(1)
# t3=t2
# print(id(t1), id(t2), id(t3))


# t1=(1,[2])
# t2=(1,[2])
# t3=t2
# print(id(t1), id(t2), id(t3))

# a='a'
# b='a'
# print(id(a),id(b))

# a=[]
# b=[]
# print(id(a),id(b))

# a=()
# b=()
# print(id(a),id(b))

# a=(1,[])
# b=(1,[])
# print(id(a),id(b))


# s='leetcode'
# s=[1,3,4,4,2,2,7,7,7,7] 
# def f(s):
#     l, l1, l2 = set(), set(), []
#     for i in s:
#         if i not in l:
#             l.add(i)
#         elif i not in l1:
#             l1.add(i)
#     return list(l), list(l1)
# print(f(s))


# s=[1,3,4,4,2,2,7,7,7,7]
# # output= [1,3]
# s='leetcodeltc'
# def f(s):
#     d,l={},[]
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]=d[i]+1
#     # print(d)
#     for i in d:
#         if d[i]==1:
#             l.append(i)
#     if l !=[]:        
#         return l
#     else:
#         return -1
# print(f(s))


# l=list(filter(lambda x:x%2==0, [i for i in range(10)]))
# print(l)

# l=list(map(lambda x:x*2, [i for i in range(10)]))
# print(l)



# def f(n):
#     while n>0:
#         yield n
#         n-=1
# try:
#     gen=f(4)
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except StopIteration as e:
#     print(e)
 
    
# def f(n):
#     while n>0:
#         yield n
#         n-=1
# gen=f(4)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in f(4):
#     print(i)


# def f(n):
#     a,b=0,1
#     while n>0:
#         if n>=2:
#             yield a
#             a,b=b,a+b
#             n-=1
# gen=f(6)
# for i in gen:
#     print(i)




# strs = ["eat","tea","tan","ate","nat","bat"]
# # output: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
# def f(strs):
#     dict1={}
#     for i in strs:
#         key= ''.join(sorted(i))
#         if key in dict1:
#             dict1[key].append(i)
#         else:
#             dict1[key]= [i]
#     print(dict1)
# print(f(strs))



# person_string='pravin thombal'
# a,b= person_string.split(" ")
# print(a)
# print(b)


# # Why class method needed?
# class Counter:
#     count = 10  # Class-level attribute

#     def m(self):
#         self.count = 100  # Instance-level attribute
#         # Counter.count=1000
#         # self.__class__.count=10000


# c = Counter()
# # print(Counter.count)  # Output: 10 (class-level)
# # print(c.count)        # Output: 10 (accessing class-level attribute through instance)

# c.m()  # Modify via instance method
# print(c.count)        # Output: 100 (instance-level attribute now overrides)
# print(Counter.count)  # Output: 10 (class-level remains unchanged)




# # why use statice method
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5/9

# print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
# # Normal Function (Utility Without Class Context):


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print(celsius_to_fahrenheit(25))  # Output: 77.0
# # Both approaches are valid, but using a static method keeps related functionality grouped and clear in its purpose.

