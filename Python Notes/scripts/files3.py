# Pipes
import os

cmd = 'echo %PATH%'
fp = os.popen(cmd)
res = fp.read()
print res
stat = fp.close()
print stat


def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


# print linecount('words.txt')

if __name__=='__main__':
    print linecount('output.txt')

