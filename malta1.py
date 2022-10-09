if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
#for counting the application runtime
#from datetime import datetime
#start_time = datetime.now()

import sys
f = open(sys.argv[1], 'r')
#import time
read_header = -1
read_op = -1
read_end = -1
read_var = -1
read_cout = -1
var_count = -1
if_count = -1
read_loop = -1
read_input = -1
input_count = -1
input_check = -1
#ifs
fread_header = -1
fread_op = -1
fread_end = -1
fread_var = -1
fread_cout = -1
fvar_count = -1

line = 0
allvarlist = []
result = []
rows = []
read = f.readlines()
stamplist = []
while True:
    
    
    readline = read[line]

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
        var_count += 1
        readvar = readline.replace('\n','')
        readvar = readvar.replace('<','')
        readvar = readvar.split('=')
        for i in range(1):
            #var_count += 1
            #print(var_count,'var')
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
            #print(allvarlist)

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
    #print('yes')   
    '''if readline[:1] == '>':
        #print(allvarlist)
        readline = readline.replace('\n','')
        readline = readline.replace(' ','')
        readline = readline.split('>')
        varprint = allvarlist.index(readline[1])
        varprint = varprint + 1
        print(allvarlist[varprint])'''

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
                    #print(eval('x - y'))
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
            variable = allvarlist.append(out)
            #print(allvarlist)
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
            print(reset)
            variable = allvarlist.append(out)
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
            variable = allvarlist.append(out)
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
    if readline[:1] == '_':
        print(readline)
        
    #print(readline[:2])
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
            #readvar[1] = int(readvar[1])
        if '>' in readline:
            readvar = readvar.split('>')
        if readvar[0] not in allvarlist:
            line += 1
            continue
        if '=' in readline:
            readvarcheck = allvarlist.index(readvar[0])
            readvarcheck1 = allvarlist.index(readvar[1])
            if readvar[0] == allvarlist[readvarcheck]:
                if readvar[1] == allvarlist[readvarcheck1]:
                    fread_op += 1
                    readline = read[fread_op]
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
                                print(eval('x / y'))
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
                            #print(line)
                        else:
                            goto2 = stamplist.index(goto)
                            fread_op = stamplist.index(goto)
                            line = goto2
                        #print(line)
            
        else:
            if '<' in readline:
                readvarcheck = allvarlist.index(readvar[0])
                readvarcheck1 = allvarlist.index(readvar[0])
                readvarcheck1 = readvarcheck1 + 1
                readvar[1] = int(readvar[1])
                allvarlist[readvarcheck1] = int(allvarlist[readvarcheck1])
                if readvar[0] == allvarlist[readvarcheck]:
                    if readvar[1] > allvarlist[readvarcheck1]:
                        fread_op += 1
                        readline = read[fread_op]
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
                                    print(eval('x / y'))
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
                                #print(line)
                            else:
                                goto2 = stamplist.index(goto)
                                fread_op = stamplist.index(goto)
                                line = goto2
            else:
                if '>' in readline:
                    readvarcheck = allvarlist.index(readvar[0])
                    readvarcheck1 = allvarlist.index(readvar[0])
                    readvarcheck1 = readvarcheck1 + 1
                    readvar[1] = int(readvar[1])
                    allvarlist[readvarcheck1] = int(allvarlist[readvarcheck1])
                    if readvar[0] == allvarlist[readvarcheck]:
                        if readvar[1] < allvarlist[readvarcheck1]:
                            fread_op += 1
                            readline = read[fread_op]
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
                                        print(eval('x / y'))
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

    if readline[:3] == 'END':
        break
        f.close()

    if readline[:2] == 'lp':
        readlp = readline.replace('lp','')
        readlp = readlp.replace('\n','')
        readlp = readlp.replace(' ','')
        readlp = readlp.split('/')
        #print(readlp)
        loopnumber = int(readlp[1])
        if '.' in readline:
            readlp = str(readlp[0])
            readlp = readlp.replace('.','')
            while loopnumber > 0:
                loopnumber -= 1
                print(readlp)

        if 'ov' in readline:
            countprep = str(readline)
            #print()
            countprep = countprep.replace('ov', '')
            countprep = countprep.replace(' ', '')
            countprep = countprep.replace('\n', '')
            countprep = countprep.replace('lp','')
            countprep = countprep.split('/')
            loopnumber = int(countprep[1])
            countprep=str(countprep[0])
            if '+' in countprep:
                while loopnumber > 0:
                    loopnumber -= 1
                    add = countprep.replace(' ', '')
                    add = add.split('+')
                    reset = str(add)
                    reset = reset.replace('[', '')
                    reset = reset.replace(']', '')
                    reset = reset.replace("'", '')
                    reset = reset.replace(" ", '')
                    reset = reset.replace(",", '')
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
                while loopnumber > 0:
                    loopnumber -= 1
                    sub = countprep.replace(' ', '')
                    sub = sub.split('-')
                    reset = str(sub)
                    reset = reset.replace('[', '')
                    reset = reset.replace(']', '')
                    reset = reset.replace("'", '')
                    reset = reset.replace(" ", '')
                    reset = reset.replace(",", '')
                    #print(reset)
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
                while loopnumber > 0:
                    loopnumber -= 1
                    mul = countprep.replace(' ', '')
                    mul = mul.split('x')
                    reset = str(mul)
                    reset = reset.replace('[', '')
                    reset = reset.replace(']', '')
                    reset = reset.replace("'", '')
                    reset = reset.replace(" ", '')
                    reset = reset.replace(",", '')
                    #print(reset)
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
                while loopnumber > 0:
                    loopnumber -= 1
                    div = countprep.replace(' ', '')
                    div = div.split('/')
                    reset = str(div)
                    reset = reset.replace('[', '')
                    reset = reset.replace(']', '')
                    reset = reset.replace("'", '')
                    reset = reset.replace(" ", '')
                    reset = reset.replace(",", '')
                    #print(reset)
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
                            print(eval('x / y'))
            if '^' in countprep:
                while loopnumber > 0:
                    loopnumber -= 1
                    pwr = countprep.replace(' ', '')
                    pwr = pwr.split('^')
                    reset = str(pwr)
                    reset = reset.replace('[', '')
                    reset = reset.replace(']', '')
                    reset = reset.replace("'", '')
                    reset = reset.replace(" ", '')
                    reset = reset.replace(",", '')
                    #print(reset)
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
           

    if readline[:3] == 'lpo':
        readlp = readline.replace('lpo','')
        readlp = readlp.replace('\n','')
        readlp = readlp.replace(' ','')
        readlp = readlp.split('/')
        loopnumber = int(readlp[1])
        if '+' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('+')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x + y'))
        if '-' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('-')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x - y'))
        if 'x' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('x')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x * y'))
        if '/' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('/')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x / y'))

    if readline[0] in allvarlist and '++' in readline:
        pp = allvarlist.index(readline[0])
        pp = pp + 1
        number = int(allvarlist[pp])
        number += 1
        allvarlist[pp] = number
        allvarlist[pp] = str(allvarlist[pp])
        #print(allvarlist[pp])

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

    #if readline[:1] == '&':
        #print(allvarlist[pp])
    line += 1

#end_time = datetime.now()
#print(end_time - start_time)

    