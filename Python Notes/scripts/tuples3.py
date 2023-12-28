# Tuples as return values
# strictly speaking,  a function can return one value. but a function can return tuple. so by returning a tuple , we can
# return multiple values.

# list1=[1,2,4,5,0]
# list1.sort()
# print list1
# return list1[0],list1[-1]

# we have min and max in-built functions.


def min_max(num_list):
    minimum = num_list[1]
    maximum = num_list[-1]
    for num in num_list:
        if num < minimum:
            minimum = num
        elif num >= maximum:
            maximum = num

    return (minimum, maximum)


num_list = [1, -3, 409, 7, 90, 9]


# print min_max(num_list)

##############################################

def divmod(top, bottom):
    quot = top / bottom
    mod = top % bottom
    return quot, mod


q, m = divmod(9, 2)
# print q,m

# '*' acts as gatherer and scatterer. gatherer means it allows the function to take variable number of arguments
# Gatherer: function definition should have *args as its argument to take variable number of arguments. 'arg' is jsut a
# convenitonal term
# Scaterer: when the funciton definition expecting multiple arguments, but the caller has given only one argument as
# tuple, error will be thrown. to overcome this, caller should use the * notation to scatter the arguemnts into the function.



def sumall(*args):
    # print args[0]
    return sum(args[0],0)

t = (4, 5,90,987)
print sumall(t)


# print sum(t,0)

# print divmod(t) # throws error
# print divmod(*t)


def printall(*args):
    print args

# printall('vivek',1,2,3,'shiva')

# def sumall(*args):
