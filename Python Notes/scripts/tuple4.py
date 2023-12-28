# zipper will join and interleaves two rows of teeth.
# zipper function takes 2 or more sequences and produces a zipper object, which has the
# capability to iterate through the pair of the tuples in the list.
# str1 = 'abc'
# l1 = [1, 2, 3]
# zip(str1, l1)
# # print zip
# for x, y in zip(str1, l1):
#     print x, y
#
# for index, elm in enumerate('acbd'):
#     print (index, elm)

# Tuples and Dictionaries

# # items() method returns a dict_item where we can traverse the list of tuples produced out of the dictionary
#
# d = {'a': 'vivek', 'b': 'shiva', 'c': 'isha'}
# d1 = d.items()
# print d1
# for letter, name in d1:
#     print letter, name

# d_list = [('a', 1000), ('b', 2000), ('c', 3000)]
# print d_list
# dict_list = dict(d_list)
# print dict_list
# letters = dict_list.keys()
# print letters
# values = dict_list.values()
# print values
# print dict(zip(letters, values))
# for x, y in zip(letters, values):
#     print x, y
# dict_list.update([('d', 4000)])
# print dict_list

# converting a tuple to list
t = ('a', 'dell')
print t

list_tup = [t]
print list_tup

# for 2 sequences to be converted to a list of tuples, you can use zip function. along with that use for and assignment
# to traverse the list

# for a single sequence like a string to convert it into a list of tuples with its index, use enumerate along with for and
# assignment

str2 = 'isha sadhgguru'
enum_list_obj = enumerate(str2)
print enum_list_obj  # it gives just the enum object,which can be iterated. so  use for and assignment to traverse the list

enum_list = []
for index, elm in enum_list_obj:
    # enum_list.append((index, elm))
    enum_list = enum_list + [(index, elm)]
print enum_list
