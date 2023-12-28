# exercise 1
# read words.txt and store each word as a key in a dictionary
# and then check for a word in the dictionary as it is a faster way to search the word.

def txt2dict(fin, name):
    filedict = dict()
    print len(filedict)
    for word in fin:
        # print word
        word1 = word.split()
        # print word1[0]
        filedict[word1[0]] = ''

    # return filedict
    # print len(filedict)
    if name in filedict:
        return True


fin = open('words.txt')
print txt2dict(fin, 'aa')
# print 'aa' in d
