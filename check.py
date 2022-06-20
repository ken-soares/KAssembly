from stdlib import * 


def eval_lines(lines,usr_vars):
    # we read all the lines twice to check for labels then to check individual lines
    #first time reading
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[0] == 'label':
            usr_vars[line[1]] = i+1
        else:
            pass
        i+= 1
    
    # Define constants BEGIN and END to jump at the beginning or end of a program
    usr_vars["BEGIN"] = 0
    usr_vars["END"] = len(lines) - 1

    # second time reading
    i = 0
    while i < len(lines):

        line = lines[i]
        #check every line if stdlib

        match line[0]:
            case '':
                pass
            case '+':
                pass
            case 'del':
                del usr_vars[line[1]]
            case 'put':
                s = " " 
                usr_vars[line[1]] = s.join(line[2::])
            case 'add':
                usr_vars[line[4]] = add(line[1],line[2],line[3],usr_vars) 
            case 'sub':
                usr_vars[line[4]] = sub(line[1],line[2],line[3],usr_vars) 
            case 'mul':
                usr_vars[line[4]] = mul(line[1],line[2],line[3],usr_vars) 
            case 'div':
                usr_vars[line[4]] = div(line[1],line[2],line[3],usr_vars,i+1) 
            case 'yeet':
                s = " "
                if line[1] != ',':
                    print(usr_vars[line[1]])
                else:
                    print(s.join(line[2::]))
            case 'iseq':
                usr_vars[line[3]] = cheq(line[1],line[2],usr_vars)
            case 'isgrt':
                usr_vars[line[3]] = is_greater(line[1],line[2],usr_vars)
            case 'islwr':
                usr_vars[line[3]] = is_greater(line[2],line[1],usr_vars)
            case 'jump':
                #-1 for index(0 based) and -1 because of line increment so -2
                i = jump(line[1],usr_vars)
            case 'yav':
                print(usr_vars)
            case 'del_all!':
                del_all(usr_vars)
            case 'if':
                i = ifcond(i,line,usr_vars)
            case 'ifnot':
                i = ifnotcond(i,line,usr_vars)
            case 'usrin':
                s = " "
                usr_vars[line[2]] = usrin(line[1],s.join(line[3::]))
            case 'randin':
                usr_vars[line[1]] = randintgen(int(line[2]),int(line[3]))
            case 'and':
                usr_vars[line[3]] = and_table(line[1],line[2],usr_vars)
            case 'or':
                usr_vars[line[3]] = or_table(line[1],line[2],usr_vars)
            case 'xor':
                usr_vars[line[3]] = xor_table(line[1],line[2],usr_vars)

        # line check, go to next line
        i+=1
