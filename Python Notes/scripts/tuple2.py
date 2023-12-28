# relational operators works on tuple. python starts compares the first element from each sequences. if they are equal,
# it goes on to next elements, and so on, until it finds elements that differ.
print (1, 2, 3) == (1, 2, 3)
print (1, 2, 3) < (2, 3, 4)
print('a', 'b', 'c') > ('a', 'b', 'z')

# Tuple assignment
# we can avoid a temp variable in swappinng of variables by using tuple
a = 2
b = 5
print 'before ', a, b
a, b = b, a  # the left side is tuple of variables and right side tuple of expressions.
print 'after ', a, b

# the number of variables on the left and right sbould be equal
c = 3
# a, b, c = a, b  --> this throws an error, since left side has more arguments than that of on the right side. ValueError

# addr = 'vivek@gmail.com'
# name_list = addr.split('@')
# print name_list[1]

# more generally, the right side of the assignment can be any sequence like a list or string or tuple
addr = 'vivek@gmail.com'
(uname, domain) = addr.split('@')
print uname
