import pprint

print "vivek"
# pprint.pprint('vivek')
pprint.pprint('vivek', indent=20, width=200)

# Global variables
been_called = False


def example1():
    global been_called
    been_called = True


example1()
# print been_called

####################################################################################################3
# Memos
known = {0: 0, 1: 1}


def fibonocci_memo(n):
    if n in known:
        return known[n]

    result = fibonocci_memo(n - 1) + fibonocci_memo(n - 2)
    known[n] = result
    return result


# print fibonocci_memo(16)


#####################################################################################################

def inverse_dict(d):
    inverse = dict()
    for key_item in d:
        val = d[key_item]
        inverse.setdefault(val,[key_item])
        if
        inverse[val].append(key_item)
    return inverse


d = {'one': 'vivek', 'two': 'dell', 'three': 'toshiba', 'four': 'vivek', 'five': 'toshiba'}
print inverse_dict(d)
# #################################################################################################


d = dict()
d['one'] = 'vivek'
# print d
d = {'one': 'vivek', 'two': 'dell', 'three': 'toshiba', 'four': 'vivek', 'five': 'toshiba'}


# print d
# print d['three']
# print len(d)
# print 'tone' in d
# vals = d.values()
# keys = d.keys()
# print keys
# print vals


# print 'toshiba' in vals


# python uses an algorithm called hashtable for 'in' operator. no matter, how many items are there in the dictionary, it
# will take approximately equal time to search in a dictionary

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


# print histogram('vivek')

# Looping and Dictionaries

def print_keys_vals(d):
    #   using dictionary in a for loop
    for key_item in sorted(d):
        print key_item, d[key_item]


# print_keys_vals(d)

# Reverse Lookup
def reverse_lookup(d, val):
    for key_item in d:
        if d[key_item] == val:
            return key_item
    raise LookupError

# d=histogram('vivek')
# print reverse_lookup(d,3)
