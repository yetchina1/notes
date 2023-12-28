fout = open('output.txt', 'w')
str1 = 'Aum Namah Shivaya'
fout.write(str1)
fout.close()
# Format operator

print 'the great mahamantra is: %s' % str1
x=11
print 'I have spotted %d camels' % x

print 'it is good to utter %s everday %d times' %(str1,x)

# File names and paths

import os
print os.getcwd()
# for filename in os.listdir(os.getcwd()):
#     print filename

print os.path.abspath('output.txt')
print os.path.isfile('output.txt')

print os.path.isdir(os.getcwd())

# def walk(dirname):
#     for name in os.listdir(dirname):
#         path=os.path.join(dirname,name)
#         if os.path.isfile(path):
#             print path
#         else:
#             walk(path)
#
# walk(os.getcwd())

import walk.py

