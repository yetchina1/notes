a = 'banana'
b = 'banana'
print a is b
a = [1,2,3]
b = [1,2,3]
# print a is b

b = a
# print a is b
# associating a variable with an object is called referencing
# an object with more than one reference has more than one names. so we say that the object is aliased

# List Arguemnents: When a list has been an argurment to a function, if the funciton gets a reference to the list object.
# if the function has done any modifications, the caller will see the changes
def delete_head(t_list):
        del t_list[0]


# append and return value: append modifies the list and returns None

t = [1,2,3]
t2 = t.append(5)
print t
# print t2

# Plus + does not modifies the list, and returns the modified value

t2=t+[340588]
# print t2

# Bad deletion technique. this below opereation slices out a new list and assigns to the variable. But it does not delete
# the head of the list. the caller will not see changes
t2=t2[1:]
# print t2
print t, ' before'
def bad_delete(t_list):
        t2=t[1:]
bad_delete(t)
print t, 'after'


