if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
import re
#for counting the application runtime
#from datetime import datetime
#start_time = datetime.now()
import sys
f = open(sys.argv[1], 'r')

line = 0
allvarlist = []
result = []
rows = []
read = f.readlines()
stamplist = []
number = 0
stampline = 0

#print(len(read))
while stampline <= len(read):
    while line < len(read):
        readline = read[line]
        if readline[0] == ':':
            #print('yes')
            readstamp = readline.replace('\n', '')
            readstamp = readstamp.replace(',', '')
            readstamp = readstamp.replace('[', '')
            readstamp = readstamp.replace(']', '')
            readstamp = readstamp.replace("'", '')
            readstamp = readstamp.replace(":", '')
            readstamp = readstamp.split(' ')
            stamplist.append(readstamp[0])
            stamplist.append(line)
        line += 1
    stampline += 1 
line = 0
while True:
    readline = read[line]
    if readline[:4] == 'pass':
        line += 1

    if readline[:4] == 'goto':
        goto = readline.replace('goto','')
        goto = goto.replace('\n','')
        goto = goto.replace(' ','')
        number = goto.isdigit()
        if number == True:
            goto = int(goto)
            line = goto -2
        else:
            goto2 = stamplist.index(goto)
            stampgoto = stamplist[goto2 + 1]
            line = stampgoto

    if readline[0] == ".":
        readpoint = readline.replace('.', '')
        readpoint = readpoint.replace('\n', '')
        print(readpoint)


    if readline[:2] == 'op':
        countprep = str(readline)
        countprep = countprep.replace('op', '')
        countprep = countprep.replace(' ', '')
        countprep = countprep.replace('\n', '')

        if '+' in countprep:
            add = countprep.replace(' ', '')
            add = add.split('+')
            add = map(int,add)
            add = list(add)
            x = add[0]
            y = add[1]
            print(eval('x + y'))
        if '-' in countprep:
            sub = countprep.replace(' ', '')
            sub = sub.split('-')
            sub = map(int,sub)
            sub = list(sub)
            x = sub[0]
            y = sub[1]
            print(eval('x - y'))
        if 'x' in countprep:
            mul = countprep.replace(' ', '')
            mul = mul.split('x')
            mul = map(int,mul)
            mul = list(mul)
            x = mul[0]
            y = mul[1]
            print(eval('x * y'))
        if '/' in countprep:
            div = countprep.replace(' ', '')
            div = div.split('/')
            div = map(int,div)
            div = list(div)
            x = div[0]
            y = div[1]
            #print(x)
            if y == 0 or x == 0:
                print('you cannot divide by 0','line:',line)
                break
            print(eval('x / y'))
           
        if '^' in countprep:
            div = countprep.replace(' ', '')
            div = div.split('^')
            div = map(int,div)
            div = list(div)
            x = div[0]
            y = div[1]
            print(eval('x ** y'))
    if readline[:1] == '<':
        readvar = readline.replace('\n','')
        readvar = readvar.replace('<','')
        readvar = readvar.split('=')
        for i in range(1):
            allvarlist.append(readvar)
            allvarlist = str(allvarlist)
            allvarlist = allvarlist.replace(' ','')
            allvarlist = allvarlist.split(',')
            allvarlist = str(allvarlist)
            allvarlist = allvarlist.replace('[','')
            allvarlist = allvarlist.replace(']','')
            allvarlist = allvarlist.replace('"','')
            allvarlist = allvarlist.replace("'",'')
            allvarlist = allvarlist.replace(' ','')
            allvarlist = allvarlist.split(',')
    if readline[:3] == 'mem':
        print(allvarlist)

    #Garbage Collector
    if readline[:1] == 'c':
        memlist = allvarlist
        number = 0
        dup = [x for i, x in enumerate(memlist) if i != memlist.index(x)]
        dup = str(dup)
        dup = dup.replace('[','')
        dup = dup.replace(']','')
        dup = dup.replace("'",'')
        dup = dup.replace(" ",'')
        dup = dup.split(',')
        while number < len(dup):
            dup2 = dup[number]
            dup3 = memlist.index(dup2)
            number += 1
            memlist.pop(dup3)

        digit = memlist[0].isdigit()
        if digit == True:
            memlist.pop(0)

        for number2 in memlist:
            if number2 in "0123456789":
                var = memlist.index(number2)
                var2 = var - 1
                digitvar = memlist[var2].isdigit()
                if digitvar == True:
                    memlist.pop(var)
                #if digitvar == False:
                    #memlist.pop(var)
        for number2 in memlist:
            if number2 in "0123456789":
                var = memlist.index(number2)
                var2 = var - 1
                digitvar = memlist[var2].isdigit()
                if digitvar == True:
                    print('memory error program panic','line:',line)
        allvarlist = memlist

    if readline[:3] == 'del':
        readdel = readline.replace('del', '')
        readdel = readdel.replace(' ', '')
        readdel = readdel.replace('\n', '')
        place = allvarlist.index(readdel)
        del allvarlist[place]
        del allvarlist[place]



    if readline[:1] == '$':
        readline = readline.replace('\n','')
        readline = readline.split('$')
        readline = str(readline)
        readline = readline.replace('[','')
        readline = readline.replace(']','')
        readline = readline.replace(',','')
        readline = readline.replace("'",'')
        readline = readline.replace(" ",'')
        var = allvarlist.index(readline)
        newvar = var + 1
        allvarlist[newvar] = input()
        #input_check += 1

    if readline[:2] == 'ov':
        countprep = str(readline)
        countprep = countprep.replace('ov', '')
        countprep = countprep.replace(' ', '')
        countprep = countprep.replace('\n', '')
        if '+' in countprep:
            add = countprep.replace(' ', '')
            add = add.split('+')
            reset = str(add)
            reset = reset.replace('[', '')
            reset = reset.replace(']', '')
            reset = reset.replace("'", '')
            reset = reset.replace(" ", '')
            reset = reset.replace(",", '')
            out = reset.split('>>')
            out = out[1]
            var = allvarlist.index(out)
            var = var + 1
            add = reset
            if add[0] in allvarlist:
                x = allvarlist.index(add[0])
                x = x + 1
                x = allvarlist[x]
                if add[1] in allvarlist:
                    y = allvarlist.index(add[1])
                    y = y + 1
                    y = allvarlist[y]
                    x = int(x)
                    y = int(y)
                    result = eval('x + y')
                    result = str(result)
                    allvarlist[var] = result
                    
        if '-' in countprep:
            sub = countprep.replace(' ', '')
            sub = sub.split('-')
            reset = str(sub)
            reset = reset.replace('[', '')
            reset = reset.replace(']', '')
            reset = reset.replace("'", '')
            reset = reset.replace(" ", '')
            reset = reset.replace(",", '')
            out = reset.split('>>')
            out = out[1]
            var = allvarlist.index(out)
            var = var + 1
            #variable = allvarlist.append(out)
            sub = reset
            if sub[0] in allvarlist:
                x = allvarlist.index(sub[0])
                x = x + 1
                x = allvarlist[x]
                if sub[1] in allvarlist:
                    y = allvarlist.index(sub[1])
                    y = y + 1
                    y = allvarlist[y]
                    x = int(x)
                    y = int(y)
                    result = eval('x - y')
                    result = str(result)
                    allvarlist[var] = result
        if countprep[1] == 'x':
            mul = countprep.replace(' ', '')
            mul = mul.split('x')
            reset = str(mul)
            reset = reset.replace('[', '')
            reset = reset.replace(']', '')
            reset = reset.replace("'", '')
            reset = reset.replace(" ", '')
            reset = reset.replace(",", '')
            out = reset.split('>>')
            out = out[1]
            var = allvarlist.index(out)
            var = var + 1
            mul = reset
            if mul[0] in allvarlist:
                x = allvarlist.index(mul[0])
                x = x + 1
                x = allvarlist[x]
                if mul[1] in allvarlist:
                    y = allvarlist.index(mul[1])
                    y = y + 1
                    y = allvarlist[y]
                    x = int(x)
                    y = int(y)
                    result = eval('x * y')
                    result = str(result)
                    allvarlist[var] = result

        if '/' in countprep:
            div = countprep.replace(' ', '')
            div = div.split('/')
            reset = str(div)
            reset = reset.replace('[', '')
            reset = reset.replace(']', '')
            reset = reset.replace("'", '')
            reset = reset.replace(" ", '')
            reset = reset.replace(",", '')
            out = reset.split('>>')
            out = out[1]
            var = allvarlist.index(out)
            var = var + 1
            div = reset
            if div[0] in allvarlist:
                x = allvarlist.index(div[0])
                x = x + 1
                x = allvarlist[x]
                if div[1] in allvarlist:
                    y = allvarlist.index(div[1])
                    y = y + 1
                    y = allvarlist[y]
                    x = int(x)
                    y = int(y)
                    if y == 0 or x == 0:
                        print('you cannot divide by 0','line:',line)
                        break
                    result = eval('x / y')
                    result = str(result)
                    allvarlist[var] = result
        if '^' in countprep:
            pwr = countprep.replace(' ', '')
            pwr = pwr.split('^')
            reset = str(pwr)
            reset = reset.replace('[', '')
            reset = reset.replace(']', '')
            reset = reset.replace("'", '')
            reset = reset.replace(" ", '')
            reset = reset.replace(",", '')
            out = reset.split('>>')
            out = out[1]
            var = allvarlist.index(out)
            var = var + 1
            pwr = reset
            if pwr[0] in allvarlist:
                x = allvarlist.index(pwr[0])
                x = x + 1
                x = allvarlist[x]
                if pwr[1] in allvarlist:
                    y = allvarlist.index(pwr[1])
                    y = y + 1
                    y = allvarlist[y]
                    x = int(x)
                    y = int(y)
                    result = eval('x ** y')
                    result = str(result)
                    allvarlist[var] = result

    if readline[:5] == 'roast':
        print('C is gay')
        print('C++ too unnecessary')
        print('Rust is too dificult')
        print('Python is too mainstream')
        print('Functional programming sucks')
        print('OOP sucks dick')
        print('MaltaLang is king')

    if readline[:2] == 'if':
        readif = readline.replace('\n','')
        readif = readif.replace('if','')
        readif = readif.replace(' ','')
        readif = readif.split(':')
        readvar = readif[0]
        if '=' in readline:
            readvar = readvar.split('=')
        if '<' in readline:
            readvar = readvar.split('<')
        if '>' in readline:
            readvar = readvar.split('>')
        if readvar[0] not in allvarlist:
            line += 1
            continue
        if '=' in readline:
                readvarcheck = allvarlist.index(readvar[0])
                readvarcheck1 = allvarlist.index(readvar[0])
                readvarcheck1 = readvarcheck1 + 1
                readvar[1] = int(readvar[1])
                allvarlist[readvarcheck1] = int(allvarlist[readvarcheck1])
                if readvar[0] == allvarlist[readvarcheck]:
                    if readvar[1] == allvarlist[readvarcheck1]:
                        readline = read[line]
                        if 'op' in readif[1]:
                            countprep = str(readif[1])
                            countprep = countprep.replace('op', '')
                            countprep = countprep.replace(' ', '')
                            countprep = countprep.replace('\n', '')
                            if 'v' in readif[1]:
                                pass
                            else:
                                if '+' in countprep:
                                    add = countprep.replace(' ', '')
                                    add = add.split('+')
                                    add = map(int,add)
                                    add = list(add)
                                    x = add[0]
                                    y = add[1]
                                    print(eval('x + y'))
                                if '-' in countprep:
                                    sub = countprep.replace(' ', '')
                                    sub = sub.split('-')
                                    sub = map(int,sub)
                                    sub = list(sub)
                                    x = sub[0]
                                    y = sub[1]
                                    print(eval('x - y'))
                                if 'x' in countprep:
                                    mul = countprep.replace(' ', '')
                                    mul = mul.split('x')
                                    mul = map(int,mul)
                                    mul = list(mul)
                                    x = mul[0]
                                    y = mul[1]
                                    print(eval('x * y'))
                                if '/' in countprep:
                                    div = countprep.replace(' ', '')
                                    div = div.split('/')
                                    div = map(int,div)
                                    div = list(div)
                                    x = div[0]
                                    y = div[1]
                                    if y == 0 or x == 0:
                                        print('you cannot divide by 0','line:',line)
                                        break
                                    print(eval('x / y'))
                                if '^' in countprep:
                                    pwr = countprep.replace(' ', '')
                                    pwr = pwr.split('/')
                                    pwr = map(int,pwr)
                                    pwr = list(pwr)
                                    x = pwr[0]
                                    y = pwr[1]
                                    print(eval('x ** y'))
                        else: pass
                        if '.' in readif[1]:
                            replacepoint = readif[1]
                            replacepoint = replacepoint.replace('.','')
                            print(replacepoint)
                        else: pass
                        if 'ov' in readif[1]:
                            countprep = str(readif[1])
                            countprep = countprep.replace('ov', '')
                            countprep = countprep.replace(' ', '')
                            countprep = countprep.replace('\n', '')
                            if '+' in countprep:
                                add = countprep.replace(' ', '')
                                add = add.split('+')
                                if add[0] in allvarlist:
                                    x = allvarlist.index(add[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if add[1] in allvarlist:
                                        y = allvarlist.index(add[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x + y'))
                                    
                            if '-' in countprep:
                                sub = countprep.replace(' ', '')
                                sub = sub.split('-')
                                if sub[0] in allvarlist:
                                    x = allvarlist.index(sub[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if sub[1] in allvarlist:
                                        y = allvarlist.index(sub[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x - y'))
                                
                            if 'x' in countprep:
                                mul = countprep.replace(' ', '')
                                mul = mul.split('x')
                                if mul[0] in allvarlist:
                                    x = allvarlist.index(mul[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if mul[1] in allvarlist:
                                        y = allvarlist.index(mul[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x * y'))

                            if '/' in countprep:
                                div = countprep.replace(' ', '')
                                div = div.split('/')
                                if div[0] in allvarlist:
                                    x = allvarlist.index(div[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if div[1] in allvarlist:
                                        y = allvarlist.index(div[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        if y == 0 or x == 0:
                                            print('you cannot divide by 0','line:',line)
                                            break
                                        print(eval('x / y'))
                            if '^' in countprep:
                                pwr = countprep.replace(' ', '')
                                pwr = pwr.split('^')
                                if pwr[0] in allvarlist:
                                    x = allvarlist.index(pwr[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if pwr[1] in allvarlist:
                                        y = allvarlist.index(pwr[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x ** y'))
                        if 'goto' in readif[1]:
                            goto = readif[1].replace('goto','')
                            goto = goto.replace('\n','')
                            goto = goto.replace(' ','')
                            goto = goto.replace(':','')

                            number = goto.isdigit()
                            if number == True:
                                goto = int(goto)
                                line = goto -2
                                fread_op = goto -2 
                            else:
                                goto2 = stamplist.index(goto)
                                fread_op = stamplist.index(goto)
                                line = goto2
                        if 'pass' in readif[1]:
                            line +=1
                        if 'and' in readif[1]:
                            andread = readif[1]
                            andread = andread.replace('and','')
                            andread = andread.split('=')
                            varcomp = allvarlist[readvarcheck + 2]
                            valuecomp = allvarlist[readvarcheck1 + 2]
                            if andread[0] == varcomp:
                                if andread[1] == valuecomp:
                                    readline = readif[2]
                                    if readline[0] == ':':
                                        readstamp = readline.replace('\n', '')
                                        readstamp = readstamp.replace(',', '')
                                        readstamp = readstamp.replace('[', '')
                                        readstamp = readstamp.replace(']', '')
                                        readstamp = readstamp.replace("'", '')
                                        readstamp = readstamp.replace(":", '')
                                        readstamp = readstamp.split(' ')
                                        stamplist.append(readstamp[0])

                                    if readline[:4] == 'goto':
                                        goto = readline.replace('goto','')
                                        goto = goto.replace('\n','')
                                        goto = goto.replace(' ','')
                                        number = goto.isdigit()
                                        if number == True:
                                            goto = int(goto)
                                            line = goto -2
                                        else:
                                            goto2 = stamplist.index(goto)
                                            line = goto2

                                    if readline[0] == ".":
                                        readpoint = readline.replace('.', '')
                                        readpoint = readpoint.replace('\n', '')
                                        print(readpoint)


                                    if readline[:2] == 'op':
                                        countprep = str(readline)
                                        countprep = countprep.replace('op', '')
                                        countprep = countprep.replace(' ', '')
                                        countprep = countprep.replace('\n', '')

                                        if '+' in countprep:
                                            add = countprep.replace(' ', '')
                                            add = add.split('+')
                                            add = map(int,add)
                                            add = list(add)
                                            x = add[0]
                                            y = add[1]
                                            print(eval('x + y'))
                                        if '-' in countprep:
                                            sub = countprep.replace(' ', '')
                                            sub = sub.split('-')
                                            sub = map(int,sub)
                                            sub = list(sub)
                                            x = sub[0]
                                            y = sub[1]
                                            print(eval('x - y'))
                                        if 'x' in countprep:
                                            mul = countprep.replace(' ', '')
                                            mul = mul.split('x')
                                            mul = map(int,mul)
                                            mul = list(mul)
                                            x = mul[0]
                                            y = mul[1]
                                            print(eval('x * y'))
                                        if '/' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('/')
                                            div = map(int,div)
                                            div = list(div)
                                            x = div[0]
                                            y = div[1]
                                            if y == 0 or x == 0:
                                                print('you cannot divide by 0','line:',line)
                                                break
                                            print(eval('x / y'))
                                        if '^' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('^')
                                            div = map(int,div)
                                            div = list(div)
                                            x = div[0]
                                            y = div[1]
                                            print(eval('x ** y'))
                                    if readline[:1] == '<':
                                        readvar = readline.replace('\n','')
                                        readvar = readvar.replace('<','')
                                        readvar = readvar.split('=')
                                        for i in range(1):
                                            allvarlist.append(readvar)
                                            allvarlist = str(allvarlist)
                                            allvarlist = allvarlist.replace(' ','')
                                            allvarlist = allvarlist.split(',')
                                            allvarlist = str(allvarlist)
                                            allvarlist = allvarlist.replace('[','')
                                            allvarlist = allvarlist.replace(']','')
                                            allvarlist = allvarlist.replace('"','')
                                            allvarlist = allvarlist.replace("'",'')
                                            allvarlist = allvarlist.replace(' ','')
                                            allvarlist = allvarlist.split(',')

                                    if readline[:1] == '$':
                                        readline = readline.replace('\n','')
                                        readline = readline.split('$')
                                        readline = str(readline)
                                        readline = readline.replace('[','')
                                        readline = readline.replace(']','')
                                        readline = readline.replace(',','')
                                        readline = readline.replace("'",'')
                                        readline = readline.replace(" ",'')
                                        var = allvarlist.index(readline)
                                        newvar = var + 1
                                        allvarlist[newvar] = input()
                                        input_check += 1

                                    if readline[:2] == 'ov':
                                        countprep = str(readline)
                                        countprep = countprep.replace('ov', '')
                                        countprep = countprep.replace(' ', '')
                                        countprep = countprep.replace('\n', '')
                                        if '+' in countprep:
                                            add = countprep.replace(' ', '')
                                            add = add.split('+')
                                            reset = str(add)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            add = reset
                                            if add[0] in allvarlist:
                                                x = allvarlist.index(add[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if add[1] in allvarlist:
                                                    y = allvarlist.index(add[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x + y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                                    
                                        if '-' in countprep:
                                            sub = countprep.replace(' ', '')
                                            sub = sub.split('-')
                                            reset = str(sub)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            #variable = allvarlist.append(out)
                                            sub = reset
                                            if sub[0] in allvarlist:
                                                x = allvarlist.index(sub[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if sub[1] in allvarlist:
                                                    y = allvarlist.index(sub[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x - y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                        if countprep[1] == 'x':
                                            mul = countprep.replace(' ', '')
                                            mul = mul.split('x')
                                            reset = str(mul)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            mul = reset
                                            if mul[0] in allvarlist:
                                                x = allvarlist.index(mul[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if mul[1] in allvarlist:
                                                    y = allvarlist.index(mul[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x * y')
                                                    result = str(result)
                                                    allvarlist[var] = result

                                        if '/' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('/')
                                            reset = str(div)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            div = reset
                                            if div[0] in allvarlist:
                                                x = allvarlist.index(div[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if div[1] in allvarlist:
                                                    y = allvarlist.index(div[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    if y == 0 or x == 0:
                                                        print('you cannot divide by 0','line:',line)
                                                        break
                                                    result = eval('x / y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                        if '^' in countprep:
                                            pwr = countprep.replace(' ', '')
                                            pwr = pwr.split('^')
                                            reset = str(pwr)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            pwr = reset
                                            if pwr[0] in allvarlist:
                                                x = allvarlist.index(pwr[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if pwr[1] in allvarlist:
                                                    y = allvarlist.index(pwr[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x ** y')
                                                    result = str(result)
                                                    allvarlist[var] = result

                                    if readline[:5] == 'roast':
                                        print('C is gay')
                                        print('C++ too unnecessary')
                                        print('Rust is too dificult')
                                        print('Python is too mainstream')
                                        print('Functional programming sucks')
                                        print('OOP sucks dick')
                                        print('MaltaLang is king')
                                    if readline[:4] == 'pass':
                                        line +=1
                                                                    
                                                                    
                                                                    
        else:
            if '<' in readline:
                readvarcheck = allvarlist.index(readvar[0])
                readvarcheck1 = allvarlist.index(readvar[0])
                readvarcheck1 = readvarcheck1 + 1
                readvar[1] = int(readvar[1])
                allvarlist[readvarcheck1] = int(allvarlist[readvarcheck1])
                if readvar[0] == allvarlist[readvarcheck]:
                    if readvar[1] > allvarlist[readvarcheck1]:
                        readline = read[line]
                        if 'op' in readif[1]:
                            countprep = str(readif[1])
                            countprep = countprep.replace('op', '')
                            countprep = countprep.replace(' ', '')
                            countprep = countprep.replace('\n', '')
                            if 'v' in readif[1]:
                                pass
                            else:
                                if '+' in countprep:
                                    add = countprep.replace(' ', '')
                                    add = add.split('+')
                                    add = map(int,add)
                                    add = list(add)
                                    x = add[0]
                                    y = add[1]
                                    print(eval('x + y'))
                                if '-' in countprep:
                                    sub = countprep.replace(' ', '')
                                    sub = sub.split('-')
                                    sub = map(int,sub)
                                    sub = list(sub)
                                    x = sub[0]
                                    y = sub[1]
                                    print(eval('x - y'))
                                if 'x' in countprep:
                                    mul = countprep.replace(' ', '')
                                    mul = mul.split('x')
                                    mul = map(int,mul)
                                    mul = list(mul)
                                    x = mul[0]
                                    y = mul[1]
                                    print(eval('x * y'))
                                if '/' in countprep:
                                    div = countprep.replace(' ', '')
                                    div = div.split('/')
                                    div = map(int,div)
                                    div = list(div)
                                    x = div[0]
                                    y = div[1]
                                    if y == 0 or x == 0:
                                        print('you cannot divide by 0','line:',line)
                                        break
                                    print(eval('x / y'))
                                if '^' in countprep:
                                    pwr = countprep.replace(' ', '')
                                    pwr = pwr.split('^')
                                    pwr = map(int,pwr)
                                    pwr = list(pwr)
                                    x = pwr[0]
                                    y = pwr[1]
                                    print(eval('x ** y'))
                        else: pass
                        if '.' in readif[1]:
                            replacepoint = readif[1]
                            replacepoint = replacepoint.replace('.','')
                            print(replacepoint)
                        else: pass
                        if 'ov' in readif[1]:
                            countprep = str(readif[1])
                            countprep = countprep.replace('ov', '')
                            countprep = countprep.replace(' ', '')
                            countprep = countprep.replace('\n', '')
                            if '+' in countprep:
                                add = countprep.replace(' ', '')
                                add = add.split('+')
                                if add[0] in allvarlist:
                                    x = allvarlist.index(add[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if add[1] in allvarlist:
                                        y = allvarlist.index(add[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x + y'))
                                    
                            if '-' in countprep:
                                sub = countprep.replace(' ', '')
                                sub = sub.split('-')
                                if sub[0] in allvarlist:
                                    x = allvarlist.index(sub[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if sub[1] in allvarlist:
                                        y = allvarlist.index(sub[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x - y'))
                                
                            if 'x' in countprep:
                                mul = countprep.replace(' ', '')
                                mul = mul.split('x')
                                if mul[0] in allvarlist:
                                    x = allvarlist.index(mul[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if mul[1] in allvarlist:
                                        y = allvarlist.index(mul[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x * y'))

                            if '/' in countprep:
                                div = countprep.replace(' ', '')
                                div = div.split('/')
                                if div[0] in allvarlist:
                                    x = allvarlist.index(div[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if div[1] in allvarlist:
                                        y = allvarlist.index(div[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        if y == 0 or x == 0:
                                            print('you cannot divide by 0','line:',line)
                                            break
                                        print(eval('x / y'))
                            if '^' in countprep:
                                pwr = countprep.replace(' ', '')
                                pwr = pwr.split('^')
                                if pwr[0] in allvarlist:
                                    x = allvarlist.index(pwr[0])
                                    x = x + 1
                                    x = allvarlist[x]
                                    if pwr[1] in allvarlist:
                                        y = allvarlist.index(pwr[1])
                                        y = y + 1
                                        y = allvarlist[y]
                                        x = int(x)
                                        y = int(y)
                                        print(eval('x ** y'))
                        if 'goto' in readif[1]:
                            goto = readif[1].replace('goto','')
                            goto = goto.replace('\n','')
                            goto = goto.replace(' ','')
                            goto = goto.replace(':','')

                            number = goto.isdigit()
                            if number == True:
                                goto = int(goto)
                                line = goto -2
                                fread_op = goto -2 
                                #print(line)
                            else:
                                goto2 = stamplist.index(goto)
                                fread_op = stamplist.index(goto)
                                line = goto2
                        if 'pass' in readif[1]:
                            line +=1
                        if 'and' in readif[1]:
                            andread = readif[1]
                            andread = andread.replace('and','')
                            andread = andread.split('<')
                            #print(andread)
                            varcomp = allvarlist[readvarcheck + 2]
                            valuecomp = allvarlist[readvarcheck1 + 2]
                            if andread[0] == varcomp:
                                if andread[1] > valuecomp:
                                    readline = readif[2]
                                    if readline[0] == ':':
                                        readstamp = readline.replace('\n', '')
                                        readstamp = readstamp.replace(',', '')
                                        readstamp = readstamp.replace('[', '')
                                        readstamp = readstamp.replace(']', '')
                                        readstamp = readstamp.replace("'", '')
                                        readstamp = readstamp.replace(":", '')
                                        readstamp = readstamp.split(' ')
                                        stamplist.append(readstamp[0])

                                    if readline[:4] == 'goto':
                                        goto = readline.replace('goto','')
                                        goto = goto.replace('\n','')
                                        goto = goto.replace(' ','')
                                        number = goto.isdigit()
                                        if number == True:
                                            goto = int(goto)
                                            line = goto -2
                                        else:
                                            goto2 = stamplist.index(goto)
                                            line = goto2

                                    if readline[0] == ".":
                                        readpoint = readline.replace('.', '')
                                        readpoint = readpoint.replace('\n', '')
                                        print(readpoint)


                                    if readline[:2] == 'op':
                                        countprep = str(readline)
                                        countprep = countprep.replace('op', '')
                                        countprep = countprep.replace(' ', '')
                                        countprep = countprep.replace('\n', '')

                                        if '+' in countprep:
                                            add = countprep.replace(' ', '')
                                            add = add.split('+')
                                            add = map(int,add)
                                            add = list(add)
                                            x = add[0]
                                            y = add[1]
                                            print(eval('x + y'))
                                        if '-' in countprep:
                                            sub = countprep.replace(' ', '')
                                            sub = sub.split('-')
                                            sub = map(int,sub)
                                            sub = list(sub)
                                            x = sub[0]
                                            y = sub[1]
                                            print(eval('x - y'))
                                        if 'x' in countprep:
                                            mul = countprep.replace(' ', '')
                                            mul = mul.split('x')
                                            mul = map(int,mul)
                                            mul = list(mul)
                                            x = mul[0]
                                            y = mul[1]
                                            print(eval('x * y'))
                                        if '/' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('/')
                                            div = map(int,div)
                                            div = list(div)
                                            x = div[0]
                                            y = div[1]
                                            if y == 0 or x == 0:
                                                print('you cannot divide by 0','line:',line)
                                                break
                                            print(eval('x / y'))
                                        if '^' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('^')
                                            div = map(int,div)
                                            div = list(div)
                                            x = div[0]
                                            y = div[1]
                                            print(eval('x ** y'))
                                    if readline[:1] == '<':
                                        readvar = readline.replace('\n','')
                                        readvar = readvar.replace('<','')
                                        readvar = readvar.split('=')
                                        for i in range(1):
                                            allvarlist.append(readvar)
                                            allvarlist = str(allvarlist)
                                            allvarlist = allvarlist.replace(' ','')
                                            allvarlist = allvarlist.split(',')
                                            allvarlist = str(allvarlist)
                                            allvarlist = allvarlist.replace('[','')
                                            allvarlist = allvarlist.replace(']','')
                                            allvarlist = allvarlist.replace('"','')
                                            allvarlist = allvarlist.replace("'",'')
                                            allvarlist = allvarlist.replace(' ','')
                                            allvarlist = allvarlist.split(',')

                                    if readline[:1] == '$':
                                        readline = readline.replace('\n','')
                                        readline = readline.split('$')
                                        readline = str(readline)
                                        readline = readline.replace('[','')
                                        readline = readline.replace(']','')
                                        readline = readline.replace(',','')
                                        readline = readline.replace("'",'')
                                        readline = readline.replace(" ",'')
                                        var = allvarlist.index(readline)
                                        newvar = var + 1
                                        allvarlist[newvar] = input()
                                        input_check += 1

                                    if readline[:2] == 'ov':
                                        countprep = str(readline)
                                        countprep = countprep.replace('ov', '')
                                        countprep = countprep.replace(' ', '')
                                        countprep = countprep.replace('\n', '')
                                        if '+' in countprep:
                                            add = countprep.replace(' ', '')
                                            add = add.split('+')
                                            reset = str(add)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            add = reset
                                            if add[0] in allvarlist:
                                                x = allvarlist.index(add[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if add[1] in allvarlist:
                                                    y = allvarlist.index(add[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x + y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                                    
                                        if '-' in countprep:
                                            sub = countprep.replace(' ', '')
                                            sub = sub.split('-')
                                            reset = str(sub)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            #variable = allvarlist.append(out)
                                            sub = reset
                                            if sub[0] in allvarlist:
                                                x = allvarlist.index(sub[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if sub[1] in allvarlist:
                                                    y = allvarlist.index(sub[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x - y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                        if countprep[1] == 'x':
                                            mul = countprep.replace(' ', '')
                                            mul = mul.split('x')
                                            reset = str(mul)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            mul = reset
                                            if mul[0] in allvarlist:
                                                x = allvarlist.index(mul[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if mul[1] in allvarlist:
                                                    y = allvarlist.index(mul[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x * y')
                                                    result = str(result)
                                                    allvarlist[var] = result

                                        if '/' in countprep:
                                            div = countprep.replace(' ', '')
                                            div = div.split('/')
                                            reset = str(div)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            div = reset
                                            if div[0] in allvarlist:
                                                x = allvarlist.index(div[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if div[1] in allvarlist:
                                                    y = allvarlist.index(div[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    if y == 0 or x == 0:
                                                        print('you cannot divide by 0','line:',line)
                                                        break
                                                    result = eval('x / y')
                                                    result = str(result)
                                                    allvarlist[var] = result
                                        if '^' in countprep:
                                            pwr = countprep.replace(' ', '')
                                            pwr = pwr.split('^')
                                            reset = str(pwr)
                                            reset = reset.replace('[', '')
                                            reset = reset.replace(']', '')
                                            reset = reset.replace("'", '')
                                            reset = reset.replace(" ", '')
                                            reset = reset.replace(",", '')
                                            out = reset.split('>>')
                                            out = out[1]
                                            var = allvarlist.index(out)
                                            var = var + 1
                                            pwr = reset
                                            if pwr[0] in allvarlist:
                                                x = allvarlist.index(pwr[0])
                                                x = x + 1
                                                x = allvarlist[x]
                                                if pwr[1] in allvarlist:
                                                    y = allvarlist.index(pwr[1])
                                                    y = y + 1
                                                    y = allvarlist[y]
                                                    x = int(x)
                                                    y = int(y)
                                                    result = eval('x ** y')
                                                    result = str(result)
                                                    allvarlist[var] = result

                                    if readline[:5] == 'roast':
                                        print('C is gay')
                                        print('C++ too unnecessary')
                                        print('Rust is too dificult')
                                        print('Python is too mainstream')
                                        print('Functional programming sucks')
                                        print('OOP sucks dick')
                                        print('MaltaLang is king')
                                    if readline[:4] == 'pass':
                                        line +=1
                                    
            else:
                if '>' in readline:
                    readvarcheck = allvarlist.index(readvar[0])
                    readvarcheck1 = allvarlist.index(readvar[0])
                    readvarcheck1 = readvarcheck1 + 1
                    readvar[1] = int(readvar[1])
                    allvarlist[readvarcheck1] = int(allvarlist[readvarcheck1])
                    if readvar[0] == allvarlist[readvarcheck]:
                        if readvar[1] < allvarlist[readvarcheck1]:
                            readline = read[line]
                            if 'op' in readif[1]:
                                countprep = str(readif[1])
                                countprep = countprep.replace('op', '')
                                countprep = countprep.replace(' ', '')
                                countprep = countprep.replace('\n', '')
                                if 'v' in readif[1]:
                                    pass
                                else:
                                    if '+' in countprep:
                                        add = countprep.replace(' ', '')
                                        add = add.split('+')
                                        add = map(int,add)
                                        add = list(add)
                                        x = add[0]
                                        y = add[1]
                                        print(eval('x + y'))
                                    if '-' in countprep:
                                        sub = countprep.replace(' ', '')
                                        sub = sub.split('-')
                                        sub = map(int,sub)
                                        sub = list(sub)
                                        x = sub[0]
                                        y = sub[1]
                                        print(eval('x - y'))
                                    if 'x' in countprep:
                                        mul = countprep.replace(' ', '')
                                        mul = mul.split('x')
                                        mul = map(int,mul)
                                        mul = list(mul)
                                        x = mul[0]
                                        y = mul[1]
                                        print(eval('x * y'))
                                    if '/' in countprep:
                                        div = countprep.replace(' ', '')
                                        div = div.split('/')
                                        div = map(int,div)
                                        div = list(div)
                                        x = div[0]
                                        y = div[1]
                                        if y == 0 or x == 0:
                                            print('you cannot divide by 0','line:',line)
                                            break
                                        print(eval('x / y'))
                                    if '^' in countprep:
                                        pwr = countprep.replace(' ', '')
                                        pwr = pwr.split('/')
                                        pwr = map(int,pwr)
                                        pwr = list(pwr)
                                        x = pwr[0]
                                        y = pwr[1]
                                        print(eval('x ** y'))

                            else: pass
                            if '.' in readif[1]:
                                replacepoint = readif[1]
                                replacepoint = replacepoint.replace('.','')
                                print(replacepoint)
                            else: pass
                            if 'ov' in readif[1]:
                                countprep = str(readif[1])
                                countprep = countprep.replace('ov', '')
                                countprep = countprep.replace(' ', '')
                                countprep = countprep.replace('\n', '')
                                if '+' in countprep:
                                    add = countprep.replace(' ', '')
                                    add = add.split('+')
                                    if add[0] in allvarlist:
                                        x = allvarlist.index(add[0])
                                        x = x + 1
                                        x = allvarlist[x]
                                        if add[1] in allvarlist:
                                            y = allvarlist.index(add[1])
                                            y = y + 1
                                            y = allvarlist[y]
                                            x = int(x)
                                            y = int(y)
                                            print(eval('x + y'))
                                        
                                if '-' in countprep:
                                    sub = countprep.replace(' ', '')
                                    sub = sub.split('-')
                                    if sub[0] in allvarlist:
                                        x = allvarlist.index(sub[0])
                                        x = x + 1
                                        x = allvarlist[x]
                                        if sub[1] in allvarlist:
                                            y = allvarlist.index(sub[1])
                                            y = y + 1
                                            y = allvarlist[y]
                                            x = int(x)
                                            y = int(y)
                                            print(eval('x - y'))
                                    
                                if 'x' in countprep:
                                    mul = countprep.replace(' ', '')
                                    mul = mul.split('x')
                                    if mul[0] in allvarlist:
                                        x = allvarlist.index(mul[0])
                                        x = x + 1
                                        x = allvarlist[x]
                                        if mul[1] in allvarlist:
                                            y = allvarlist.index(mul[1])
                                            y = y + 1
                                            y = allvarlist[y]
                                            x = int(x)
                                            y = int(y)
                                            print(eval('x * y'))

                                if '/' in countprep:
                                    div = countprep.replace(' ', '')
                                    div = div.split('/')
                                    if div[0] in allvarlist:
                                        x = allvarlist.index(div[0])
                                        x = x + 1
                                        x = allvarlist[x]
                                        if div[1] in allvarlist:
                                            y = allvarlist.index(div[1])
                                            y = y + 1
                                            y = allvarlist[y]
                                            x = int(x)
                                            y = int(y)
                                            if y == 0 or x == 0:
                                                print('you cannot divide by 0','line:',line)
                                                break
                                            print(eval('x / y'))
                                if '>' in countprep:
                                    pwr = countprep.replace(' ', '')
                                    pwr = pwr.split('>')
                                    if pwr[0] in allvarlist:
                                        x = allvarlist.index(pwr[0])
                                        x = x + 1
                                        x = allvarlist[x]
                                        if pwr[1] in allvarlist:
                                            y = allvarlist.index(pwr[1])
                                            y = y + 1
                                            y = allvarlist[y]
                                            x = int(x)
                                            y = int(y)
                                            print(eval('x ** y'))
                        
                            if 'goto' in readif[1]:
                                goto = readif[1].replace('goto','')
                                goto = goto.replace('\n','')
                                goto = goto.replace(' ','')
                                goto = goto.replace(':','')

                                number = goto.isdigit()
                                if number == True:
                                    goto = int(goto)
                                    line = goto -2
                                    fread_op = goto -2 
                                else:
                                    goto2 = stamplist.index(goto)
                                    fread_op = stamplist.index(goto)
                                    line = goto2
                            if 'pass' in readif[1]:
                                line +=1
                            if 'and' in readif[1]:
                                andread = readif[1]
                                andread = andread.replace('and','')
                                andread = andread.split('>')
                                #print(andread)
                                varcomp = allvarlist[readvarcheck + 2]
                                valuecomp = allvarlist[readvarcheck1 + 2]
                                if andread[0] == varcomp:
                                    if andread[1] < valuecomp:
                                        readline = readif[2]
                                        #print('yes')
                                        if readline[0] == ':':
                                            readstamp = readline.replace('\n', '')
                                            readstamp = readstamp.replace(',', '')
                                            readstamp = readstamp.replace('[', '')
                                            readstamp = readstamp.replace(']', '')
                                            readstamp = readstamp.replace("'", '')
                                            readstamp = readstamp.replace(":", '')
                                            readstamp = readstamp.split(' ')
                                            stamplist.append(readstamp[0])

                                        if readline[:4] == 'goto':
                                            goto = readline.replace('goto','')
                                            goto = goto.replace('\n','')
                                            goto = goto.replace(' ','')
                                            number = goto.isdigit()
                                            if number == True:
                                                goto = int(goto)
                                                line = goto -2
                                            else:
                                                goto2 = stamplist.index(goto)
                                                line = goto2

                                        if readline[0] == ".":
                                            readpoint = readline.replace('.', '')
                                            readpoint = readpoint.replace('\n', '')
                                            print(readpoint)


                                        if readline[:2] == 'op':
                                            countprep = str(readline)
                                            countprep = countprep.replace('op', '')
                                            countprep = countprep.replace(' ', '')
                                            countprep = countprep.replace('\n', '')

                                            if '+' in countprep:
                                                add = countprep.replace(' ', '')
                                                add = add.split('+')
                                                add = map(int,add)
                                                add = list(add)
                                                x = add[0]
                                                y = add[1]
                                                print(eval('x + y'))
                                            if '-' in countprep:
                                                sub = countprep.replace(' ', '')
                                                sub = sub.split('-')
                                                sub = map(int,sub)
                                                sub = list(sub)
                                                x = sub[0]
                                                y = sub[1]
                                                print(eval('x - y'))
                                            if 'x' in countprep:
                                                mul = countprep.replace(' ', '')
                                                mul = mul.split('x')
                                                mul = map(int,mul)
                                                mul = list(mul)
                                                x = mul[0]
                                                y = mul[1]
                                                print(eval('x * y'))
                                            if '/' in countprep:
                                                div = countprep.replace(' ', '')
                                                div = div.split('/')
                                                div = map(int,div)
                                                div = list(div)
                                                x = div[0]
                                                y = div[1]
                                                if y == 0 or x == 0:
                                                    print('you cannot divide by 0','line:',line)
                                                    break
                                                print(eval('x / y'))
                                            if '^' in countprep:
                                                div = countprep.replace(' ', '')
                                                div = div.split('^')
                                                div = map(int,div)
                                                div = list(div)
                                                x = div[0]
                                                y = div[1]
                                                print(eval('x ** y'))
                                        if readline[:1] == '<':
                                            readvar = readline.replace('\n','')
                                            readvar = readvar.replace('<','')
                                            readvar = readvar.split('=')
                                            for i in range(1):
                                                allvarlist.append(readvar)
                                                allvarlist = str(allvarlist)
                                                allvarlist = allvarlist.replace(' ','')
                                                allvarlist = allvarlist.split(',')
                                                allvarlist = str(allvarlist)
                                                allvarlist = allvarlist.replace('[','')
                                                allvarlist = allvarlist.replace(']','')
                                                allvarlist = allvarlist.replace('"','')
                                                allvarlist = allvarlist.replace("'",'')
                                                allvarlist = allvarlist.replace(' ','')
                                                allvarlist = allvarlist.split(',')

                                        if readline[:1] == '$':
                                            readline = readline.replace('\n','')
                                            readline = readline.split('$')
                                            readline = str(readline)
                                            readline = readline.replace('[','')
                                            readline = readline.replace(']','')
                                            readline = readline.replace(',','')
                                            readline = readline.replace("'",'')
                                            readline = readline.replace(" ",'')
                                            var = allvarlist.index(readline)
                                            newvar = var + 1
                                            allvarlist[newvar] = input()
                                            input_check += 1

                                        if readline[:2] == 'ov':
                                            countprep = str(readline)
                                            countprep = countprep.replace('ov', '')
                                            countprep = countprep.replace(' ', '')
                                            countprep = countprep.replace('\n', '')
                                            if '+' in countprep:
                                                add = countprep.replace(' ', '')
                                                add = add.split('+')
                                                reset = str(add)
                                                reset = reset.replace('[', '')
                                                reset = reset.replace(']', '')
                                                reset = reset.replace("'", '')
                                                reset = reset.replace(" ", '')
                                                reset = reset.replace(",", '')
                                                out = reset.split('>>')
                                                out = out[1]
                                                var = allvarlist.index(out)
                                                var = var + 1
                                                add = reset
                                                if add[0] in allvarlist:
                                                    x = allvarlist.index(add[0])
                                                    x = x + 1
                                                    x = allvarlist[x]
                                                    if add[1] in allvarlist:
                                                        y = allvarlist.index(add[1])
                                                        y = y + 1
                                                        y = allvarlist[y]
                                                        x = int(x)
                                                        y = int(y)
                                                        result = eval('x + y')
                                                        result = str(result)
                                                        allvarlist[var] = result
                                                        
                                            if '-' in countprep:
                                                sub = countprep.replace(' ', '')
                                                sub = sub.split('-')
                                                reset = str(sub)
                                                reset = reset.replace('[', '')
                                                reset = reset.replace(']', '')
                                                reset = reset.replace("'", '')
                                                reset = reset.replace(" ", '')
                                                reset = reset.replace(",", '')
                                                out = reset.split('>>')
                                                out = out[1]
                                                var = allvarlist.index(out)
                                                var = var + 1
                                                #variable = allvarlist.append(out)
                                                sub = reset
                                                if sub[0] in allvarlist:
                                                    x = allvarlist.index(sub[0])
                                                    x = x + 1
                                                    x = allvarlist[x]
                                                    if sub[1] in allvarlist:
                                                        y = allvarlist.index(sub[1])
                                                        y = y + 1
                                                        y = allvarlist[y]
                                                        x = int(x)
                                                        y = int(y)
                                                        result = eval('x - y')
                                                        result = str(result)
                                                        allvarlist[var] = result
                                            if countprep[1] == 'x':
                                                mul = countprep.replace(' ', '')
                                                mul = mul.split('x')
                                                reset = str(mul)
                                                reset = reset.replace('[', '')
                                                reset = reset.replace(']', '')
                                                reset = reset.replace("'", '')
                                                reset = reset.replace(" ", '')
                                                reset = reset.replace(",", '')
                                                out = reset.split('>>')
                                                out = out[1]
                                                var = allvarlist.index(out)
                                                var = var + 1
                                                mul = reset
                                                if mul[0] in allvarlist:
                                                    x = allvarlist.index(mul[0])
                                                    x = x + 1
                                                    x = allvarlist[x]
                                                    if mul[1] in allvarlist:
                                                        y = allvarlist.index(mul[1])
                                                        y = y + 1
                                                        y = allvarlist[y]
                                                        x = int(x)
                                                        y = int(y)
                                                        result = eval('x * y')
                                                        result = str(result)
                                                        allvarlist[var] = result

                                            if '/' in countprep:
                                                div = countprep.replace(' ', '')
                                                div = div.split('/')
                                                reset = str(div)
                                                reset = reset.replace('[', '')
                                                reset = reset.replace(']', '')
                                                reset = reset.replace("'", '')
                                                reset = reset.replace(" ", '')
                                                reset = reset.replace(",", '')
                                                out = reset.split('>>')
                                                out = out[1]
                                                var = allvarlist.index(out)
                                                var = var + 1
                                                div = reset
                                                if div[0] in allvarlist:
                                                    x = allvarlist.index(div[0])
                                                    x = x + 1
                                                    x = allvarlist[x]
                                                    if div[1] in allvarlist:
                                                        y = allvarlist.index(div[1])
                                                        y = y + 1
                                                        y = allvarlist[y]
                                                        x = int(x)
                                                        y = int(y)
                                                        if y == 0 or x == 0:
                                                            print('you cannot divide by 0','line:',line)
                                                            break
                                                        result = eval('x / y')
                                                        result = str(result)
                                                        allvarlist[var] = result
                                            if '^' in countprep:
                                                pwr = countprep.replace(' ', '')
                                                pwr = pwr.split('^')
                                                reset = str(pwr)
                                                reset = reset.replace('[', '')
                                                reset = reset.replace(']', '')
                                                reset = reset.replace("'", '')
                                                reset = reset.replace(" ", '')
                                                reset = reset.replace(",", '')
                                                out = reset.split('>>')
                                                out = out[1]
                                                var = allvarlist.index(out)
                                                var = var + 1
                                                pwr = reset
                                                if pwr[0] in allvarlist:
                                                    x = allvarlist.index(pwr[0])
                                                    x = x + 1
                                                    x = allvarlist[x]
                                                    if pwr[1] in allvarlist:
                                                        y = allvarlist.index(pwr[1])
                                                        y = y + 1
                                                        y = allvarlist[y]
                                                        x = int(x)
                                                        y = int(y)
                                                        result = eval('x ** y')
                                                        result = str(result)
                                                        allvarlist[var] = result

                                        if readline[:5] == 'roast':
                                            print('C is gay')
                                            print('C++ too unnecessary')
                                            print('Rust is too dificult')
                                            print('Python is too mainstream')
                                            print('Functional programming sucks')
                                            print('OOP sucks dick')
                                            print('MaltaLang is king')
                                        if readline[:4] == 'pass':
                                            line += 1

    if readline[:3] == 'END':
        break
        f.close()
    if readline[0] in allvarlist and '++' in readline:
        pp = allvarlist.index(readline[0])
        pp = pp + 1
        number = int(allvarlist[pp])
        number += 1
        allvarlist[pp] = number
        allvarlist[pp] = str(allvarlist[pp])

    if readline[0] in allvarlist and '--' in readline:
        pp = allvarlist.index(readline[0])
        pp = pp + 1
        number = int(allvarlist[pp])
        number -= 1
        allvarlist[pp] = number
        allvarlist[pp] = str(allvarlist[pp])

    if readline[:1] == '>':
        readline = readline.replace('\n','')
        readline = readline.replace(' ','')
        readline = readline.split('>')
        varprint = allvarlist.index(readline[1])
        varprint = varprint + 1
        print(allvarlist[varprint])
    line += 1
