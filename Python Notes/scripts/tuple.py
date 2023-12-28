t = 1, 2, 3
print t
t1 = (2, 3, 4, 5)
print t1
t2 = (1,)
print t2
t3 = tuple()  # empty tuple
print t3
# tuple() argument can be list, tuple or any string
t4 = tuple([1, 2, 3])
print t4
t5 = tuple('vivek')
print t5

# Bracket opererator indexes an element in a tuple
print t5[2]

# slice operator selects a range of elements
print t5[1:3]

# you can NOT  modify a tuple element as tuple is immutable.
print t5[1]
# t5[1] = 's'

# But you can replace one tuple with another.
print 'before ', t5
t5 = t5[1:3] + ('a',)  # this statement makes a new tuple and assigns t5 to this new one.
print 'after ', t5

