a = [1, 2, 3]
b = [4, 5, 6]
# print a+b


#   for item in b:
#       print item

t = ['a', 'b', 'c', 'd']
# print t[:3]
x = t
# print x
t.append('e')
# print t
a.extend(b)
# print a
# print b
# print a+b
# print a
names=['isha', 'shiva', 'sadhguru','SADHGURU']
# print names
#names = names.sort()
print names # sort() method returns None. so you sorted out but the assignment will be None, since sort() returns None.
# print sum(a+b)
# print a , b
# Pop, del, remove
# print a
poppy = a.pop(1)
# print poppy
# print a
del a[1]
# print a
a.remove(4)
# print a
a.append(8)
# print a
a.extend('vivek')
# print a
name='vivek'
name2='isha'
name = name+name2
# print name
# print names

def add_all(a_list):
    sum=0
    for item in a_list:
        sum+=item
    return sum
# print add_all([1,2,3])
# print sum([23,234,56])

# map implementation
def to_upper(names_list):
        upper_list=[]
        for name in names_list:
                upper_list.append(name.upper())
        return upper_list

# filter implementation

def filter_upper(names_list):
        upper_list=[]
        for name in names_list:
            if name.isupper():
                upper_list.append(name)

        return upper_list

print filter_upper(names)












