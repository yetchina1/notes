def nested_sum(nest_list):
        sum = 0
        for item in nest_list:
            if type(item)==list:
                for nested_item in item:
                        sum+=nested_item
            else:
                sum+=item

        return sum
# print nested_sum([[1,2,3],[3,4,5],9])


def cumsum(item_list):
    cumsum_list=[]
    sum=0
    for i in range(len(item_list)):
        sum+=item_list[i]
        cumsum_list.append(sum)

    return cumsum_list
# print cumsum([1,2,3,4,5])

def middle(item_list):
    middle_list=[]
    middle_list=item_list[1:-1]

    return middle_list

# print middle([1,2,3,4,5])

def chop(item_list):
    item_list.pop(0)
    item_list.pop(-1)

    return None
# nums=[1,2,3,4,6]
# print nums
# chop(nums)
# print nums

def is_sorted(item_list):
    for i in range(len(item_list)-1):
        if item_list[i]>item_list[i+1]:
            return False

    return True


# print is_sorted([1,2,3,40,59])

def is_anagram(str1,str2):
    list1 = list(str1)
    # list2 = list(str2)
    for i in list1:
        if i not in str2:
            return False
    return True

# print is_anagram('dormitory','dirtyroom')

def has_duplicate(item_list):
    for i in range(len(item_list)-1):
        j=i+1
        while(j<len(item_list)):
            if item_list[i]==item_list[j]:
                return True
            j+=1

    return False
# print has_duplicate([1,2,9,4,1])

def birthday():

    import random
    birthdays=[]
    for i in range(23):
        rand=random.randint(1,23)
        birthdays.append(rand)
    # print len(birthdays)
    return birthdays

# print birthday()

def word_list():
    import time
    fin = open('words.txt')
    wordlist=[]
    wordlist1=[]
    start_time=time.time()
    # print start_time
    for i in fin:
        x = i.strip()
        wordlist.append(x)
        # print wordlist
    end_time=time.time()
    # print end_time
    runtime_append_method = end_time - start_time
    print runtime_append_method

    fin1=open('words.txt')
    print fin1
    start_time = time.time()
    for i in fin1:
        x=i.strip()
        # print x
        wordlist1 = wordlist1+[x]
        # print wordlist1
    end_time=time.time()
    runtime_plus_method = end_time - start_time
    print runtime_plus_method

    print runtime_append_method, runtime_plus_method
    print len(wordlist)
    print len(wordlist1)

word_list()
































