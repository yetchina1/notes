#Catching Exceptions
#
# try:
#     fin=open('otput.txt')
#     print fin.readline()
# except:
#     print 'Inside caught exception: sorry there is an error'

# Databases

import anydbm,pickle
db=anydbm.open('captions','c')
db['firstpic.png']='this is first pic'
print db['firstpic.png']
db['firstpic.png']='this is edited version of the first.png\'s caption'
print db['firstpic.png']

t=[1,2,3]
s=pickle.dumps(t)

t2=pickle.loads(s)
# print t2
# print t == t2
# print t is t2

for key in db:
    print key,db[key]

db.close()

# Pickling

import pickle





