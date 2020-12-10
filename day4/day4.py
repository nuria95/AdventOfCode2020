import numpy as np
import re


data = open("input").read().split("\n\n")
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']#,'cid']

def isValid(passport):
    return all(f+':' in passport for f in fields)

def countValid():
    num_valid = 0
    for passport in data:
        if isValid(passport):
            num_valid+=1
    return num_valid


print('Num valid passports Day4.1', countValid() )

valid_hcl = ['a', 'b', 'c', 'd', 'e', 'f'] + [str(e) for e in np.arange(0, 10)]
valid_ecl = ['amb','blu','brn','gry','grn','hzl','oth'] 

def countStrictValid():
    num_invalid = 0
    for passport in data:
        
        if isValid(passport):
            pieced_pass = re.split(' |\n', passport)
            for piece in pieced_pass:
                if not valid_params(piece):
                    num_invalid +=1
                    break
        else:
            num_invalid += 1

                
    return (len(data) - num_invalid)
            

def valid_params(piece):
    field, data = piece.split(':')[0], piece.split(':')[1]
    if field == 'byr':
        if not len(data) == 4:
            return False
        return 1920 <= int(data) <= 2002
    elif field == 'iyr':
        if not len(data) == 4:
            return False
        return 2010 <= int(data) <= 2020
    elif field == 'eyr':
        if not len(data) == 4:
            return False
        return 2020 <= int(data) <= 2030
    elif field == 'hgt':
        if not ('in' or 'cm' in data):
            return False
        if 'in' in data:
            return 59<=int(data[:-2])<=76
        elif 'cm' in data:
            return 150 <= int(data[:-2]) <= 193
    elif field == 'hcl':
        if len(data) < 7 or not '#' == data[0]:
            return False
        return all(e in valid_hcl for e in data[1:])

    elif field =='ecl':
        return data in valid_ecl

    elif field =='pid':
        return len(data)==9
    
    elif field == 'cid':
        return True
    else:
        raise ValueError(f'Field {field} not found')

print('Num valid passports Day4.2', countStrictValid() )
