if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
import sys
import os
version = 'alpha 0.2'
fp = open('config.txt','r')
readline = fp.readlines()
#print(readline[0])

if sys.argv[1] == 'createmalta':
    f = open('main.mlt','w')
    info = str('config')
    info = info.replace('.mlt','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use maltalang')
    #f.close()

if sys.argv[0] == 'createmalta':
    f = open('main.mlt','w')
    info = str('config')
    info = info.replace('.mlt','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use maltalang')

    #f.close()
'''if sys.argv[1] == 'createpobre':
    f = open('main.pbr','w')
    info = str('config')
    info = info.replace('.pbr','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use pobrelang')
    #f.close()

if sys.argv[0] == 'createpobre':
    f = open('main.pbr','w')
    info = str('config')
    info = info.replace('.pbr','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use pobrelang')
    #f.close()'''

if readline[0] == 'use maltalang':
    if sys.argv[1] == 'version' or sys.argv[0] == 'version':
        print(version)

    if sys.argv[0] == 'version' or  sys.argv[0] == 'version':
        print(version)
    if sys.argv[1] == 'run':
        os.system('python interpreter.py main.mlt')
    if sys.argv[0] == 'run':
        f = open(sys.argv[0],'r')
        os.system('MaltaLang main.mlt')

'''if readline[0] == 'use pobrelang':
    if sys.argv[1] == 'version' or sys.argv[0] == 'version':
        print(version)

    if sys.argv[0] == 'version' or  sys.argv[0] == 'version':
        print(version)

    if sys.argv[1] == 'run':
        os.system('python pobrelang.py main.pbr')
    '''