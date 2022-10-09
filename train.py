if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
import sys
import os
version = 'alpha 0.2'
#print(readline[0])

if sys.argv[1] == 'createmalta1':
    f = open('main.mlt','w')
    info = str('config')
    info = info.replace('.mlt','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use maltalang1')

if sys.argv[1] == 'createmalta2':
    f = open('main.mlt','w')
    info = str('config')
    info = info.replace('.mlt','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use maltalang2')

if sys.argv[0] == 'createmalta':
    f = open('main.mlt','w')
    info = str('config')
    info = info.replace('.mlt','')
    info = info+'.txt'
    info_open = open(info,'w')
    info_open.write('use maltalang')


fp = open('config.txt','r')
readline = fp.readlines()
if readline[0] == 'use maltalang1':
    if sys.argv[1] == 'version' or sys.argv[0] == 'version':
        print(version)

    if sys.argv[0] == 'version' or  sys.argv[0] == 'version':
        print(version)

    if sys.argv[1] == 'run':
        os.system('python malta1.py main.mlt')
    if sys.argv[0] == 'run':
        f = open(sys.argv[0],'r')
        os.system('MaltaLang main.mlt')

if readline[0] == 'use maltalang2':
    if sys.argv[1] == 'version' or sys.argv[0] == 'version':
        print(version)

    if sys.argv[0] == 'version' or  sys.argv[0] == 'version':
        print(version)

    if sys.argv[1] == 'run':
        os.system('python malta2.py main.mlt')
    if sys.argv[0] == 'run':
        f = open(sys.argv[0],'r')
        os.system('MaltaLang main.mlt')
