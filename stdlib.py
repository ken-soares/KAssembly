# Kasm standard library 

import random
from math import floor

# MATH FUNCTIONS
def add(addtype, a,b,usr_vars:dict):
    if addtype == "float":
        if a in usr_vars.keys() and b in usr_vars.keys():
            return float(usr_vars[a]) + float(usr_vars[b])
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return float(usr_vars[a]) + float(b)
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return float(a) + float(usr_vars[b])
        else:
            return float(a)+float(b)
    else:
        if a in usr_vars.keys() and b in usr_vars.keys():
            return floor(usr_vars[a] + usr_vars[b])
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return floor(float(usr_vars[a]) + float(b))
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return floor(float(a) + float(usr_vars[b]))
        else:
            return floor(float(a)+float(b))

def sub(addtype, a,b,usr_vars:dict):
    if addtype == "float":
        if a in usr_vars.keys() and b in usr_vars.keys():
            return float(usr_vars[a]) - float(usr_vars[b])
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return float(usr_vars[a]) - float(b)
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return float(a) - float(usr_vars[b])
        else:
            return float(a)-float(b)
    else:
        if a in usr_vars.keys() and b in usr_vars.keys():
            return floor(float(usr_vars[a]) - float(usr_vars[b]))
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return floor(float(usr_vars[a]) - float(b))
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return floor(float(a) - float(usr_vars[b]))
        else:
            return floor(float(a)-float(b))

def mul(addtype, a,b,usr_vars:dict):
    if addtype == "float":
        if a in usr_vars.keys() and b in usr_vars.keys():
            return float(usr_vars[a]) * float(usr_vars[b])
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return float(usr_vars[a]) * float(b)
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return float(a) * float(usr_vars[b])
        else:
            return float(a)*float(b)
    else:
        if a in usr_vars.keys() and b in usr_vars.keys():
            return floor(float(usr_vars[a]) * float(usr_vars[b]))
        elif a in usr_vars.keys() and b not in usr_vars.keys():
            return floor(float(usr_vars[a]) * float(b))
        elif a not in usr_vars.keys() and b in usr_vars.keys():
            return floor(float(a) * float(usr_vars[b]))
        else:
            return floor(a*b)

def div(addtype, a,b,usr_vars:dict,i):
    if float(b) != 0:
        if addtype == "float":
            if a in usr_vars.keys() and b in usr_vars.keys():
                return float(usr_vars[a]) / float(usr_vars[b])
            elif a in usr_vars.keys() and b not in usr_vars.keys():
                return float(usr_vars[a]) / float(b)
            elif a not in usr_vars.keys() and b in usr_vars.keys():
                return float(a) / float(usr_vars[b])
            else:
                return float(a) / float(b)
        else:
            if a in usr_vars.keys() and b in usr_vars.keys():
                return floor(float(usr_vars[a]) / float(usr_vars[b]))
            elif a in usr_vars.keys() and b not in usr_vars.keys():
                return floor(float(usr_vars[a]) / float(b))
            elif a not in usr_vars.keys() and b in usr_vars.keys():
                return floor(float(a) / float(usr_vars[b]))
            else:
                return floor(float(a)/float(b))
    else:
        print(f"error division by 0 (line {i})")
        return "NaN"

# VERIFICATIONS AND BOOLEAN CHECKS
def ifcond(i,line,usr_vars):
    if not usr_vars[line[1]]:
        #-1 for index(0 based) and -1 because of line increment so -2
        if line[2].isnumeric():
            i = int(line[2]) - 2
        else:
            i = int(usr_vars[line[2]]) - 2
    return i

def ifnotcond(i,line,usr_vars):
    if usr_vars[line[1]]:
        #-1 for index(0 based) and -1 because of line increment so -2
        if line[2].isnumeric():
            i = int(line[2]) - 2
        else:
            i = int(usr_vars[line[2]]) - 2
    return i

def cheq(param1,param2, usr_vars):
    aVar = param1 in usr_vars
    bVar = param2 in usr_vars
    if aVar and bVar:
        return usr_vars[param1] == usr_vars[param2] 
    elif not aVar and bVar:
        return param1 == usr_vars[param2]
    elif aVar and not bVar:
        return usr_vars[param1] == param2 
    else:
        return param1 == param2
    
def is_greater(param1,param2, usr_vars):
    aVar = param1 in usr_vars
    bVar = param2 in usr_vars
    if aVar and bVar:
        return usr_vars[param1] > usr_vars[param2] 
    elif not aVar and bVar:
        return param1 > usr_vars[param2]
    elif aVar and not bVar:
        return usr_vars[param1] > param2 
    else:
        return param1 > param2

# LOOPS AND LABELS
def jump(line,usr_vars):
    i = line.isnumeric()
    if i:
        return int(i) - 2
    else:
        return int(usr_vars[line]) - 1

# USR INPUT
def usrin(type,message):
    match(type):
        case 'str':
            var = str(input(message))
        case 'int':
            var = int(input(message))
        case 'float':
            var = float(input(message))
        case 'bool':
            var = bool(input(message))
        case _: 
            var = "error during input"
    return var

# MANUAL MEMORY MANAGEMENT
def del_all(usr_vars):
    usr_vars.clear()

# VERITY TABLES
def randintgen(lim1, lim2):
    return random.randint(lim1,lim2)


def or_table(param1, param2, usr_vars):
    if usr_vars[param1] or usr_vars[param2]:
        return True
    else:
        return False

def and_table(param1, param2, usr_vars):
    if usr_vars[param1] or usr_vars[param2]:
        return True
    else:
        return False

def xor_table(param1, param2, usr_vars):
    if usr_vars[param1] and not usr_vars[param2]:
        return True
    elif not usr_vars[param1] and usr_vars[param2]:
        return True
    else:
        return False
