import pyperclip
import os

def load_data(input_list, storages):
    # input_list : [(variable names) data_loc]
    if input_list[-1] in storages.keys():
        f = open(storages[input_list[-1]], "r")
    else:
        f = open(input_list[-1], "r")
    check_len = 1
    while True:
        line = f.readline().replace('\n','')
        if not line:
            print('<<< data loaded ! >>>')
            f.close()
            for var in var_list:
                print(f'{var} | total : {len(storages[var])}, example : {storages[var][0]}')
            return storages
        if line == '':
            continue
        if check_len:
            if len(line.split('\t')) != (len(input_list)-1):
                print("<< number of variable is wrong >>")
                return storages
            else:
                var_list = input_list[:-1]
                for var in var_list:
                    storages[var] = []
                check_len = 0
        for var, str_in in zip(var_list, line.split('\t')):
            storages[var] += [str_in]
        

def new_var(input_list, storages):
    # input_list : [variable_type, variable_name, (string if single)]
    var_type = input_list[0]
    new_var = input_list[1]    
    if var_type == 'single':
        if len(input_list) > 2:
            storages[new_var] = input_list[2]
        else:        
            storages[new_var] = ''
    elif 'like' in var_type:
        storages[new_var] = ['' for _ in range(len(storages[var_type.replace('like_','')]))]
    print('<<< new variable ! >>>')
    print(f'{new_var} | var_type : {var_type}, detail : {storages[new_var]}')

    return storages

def string_from(input_list, storages):
    # input_list : [from(clip or list_name) index(if list) to(str)]
    
    if input_list[0] == 'clipboard':
        storages[input_list[-1]] = pyperclip.paste()
    else:
        index_use = input_list[1]
        if index_use in storages.keys():
            index_use = storages[index_use]
        if len(input_list) == 3:
            storages[input_list[-1]] = storages[input_list[0]][int(index_use)]
    print(f'String in | {input_list[-1]} : {storages[input_list[-1]]}')
    return storages

def clear_clip():
    pyperclip.copy('')

    
def check_type(input_list, storages):
    # input_list : [variable_name (index if list)]
    var_name = input_list[0]
    if type(storages[var_name]) == list:
        if len(input_list) > 1:
            print(f"type of {input_list[1]} component of {input_list[0]} is {type(storages[var_name][int(input_list[1])])}")
        else:
            print(f"type of {var_name} is list (sub : {type(storages[var_name][0])})")
    else:
        print(f"type of {var_name} is {type(storages[var_name])}")
        
def change_type(input_list, storages):
    # input_list : [variable_name type]
    var_name = input_list[0]
    var_type = input_list[1]
    if var_type == 'int':
        storages[var_name] = int(storages[var_name])
    elif var_type == 'float':
        storages[var_name] = float(storages[var_name])
    elif var_type == 'string' or var_type == 'str':
        storages[var_name] = str(storages[var_name])
    print(f"type of {var_name} changed to {type(storages[var_name])}")
    return storages
        
def save_txt(input_list, storages):
    # input_list : [save_name save_type var_name]
    save_name = input_list[0]
    if save_name in storages.keys():
        save_name = storages[save_name]
    save_type = input_list[1] # w, a will be used
    var_name = input_list[2]
    if not os.path.exists(save_name):
        f = open(save_name,"w")
        f.close()
        
    with open(save_name,save_type) as f:
        if type(storages[var_name]) == list:
            for i in storages[var_name]:
                f.write(i)
                f.write('\n')
        else:
            f.write(str(storages[var_name]))
            f.write('\n')
    print(f"{save_name} saved!")

def concat_str(input_list, storages):
    # input_list : [var_name changes(can be var also can be str but not list)]
    var_name = input_list[0]
    changes = input_list[1].split('+')
    new_str = ''
    for sub_str in changes:
        if sub_str in storages.keys():
            if type(storages[sub_str]) == list:
                print(f"{storages[sub_str]} is list ...")
                return storages
            else:
                new_str += str(storages[sub_str])
        else:
            new_str += sub_str
    storages[var_name] = new_str
    print(f' << modified string >> {var_name} | {storages[var_name]}')
    return storages

def compare_comp(input_list, storages):
    # input_list [two var_name or str and one result_name]
    comp_1 = input_list[0]
    comp_2 = input_list[1]
    result_name = input_list[2]
    if comp_1 in storages.keys():
        comp_1 = storages[comp_1]
    if comp_2 in storages.keys():
        comp_2 = storages[comp_2]
        
    if comp_1 == comp_2:
        storages[result_name] = 1
    else:
        storages[result_name] = 0
    return storages

def calculate_comp(input_list, storages):
    # input_list [var_name cal_symbol num]
    var_name = input_list[0]
    cal_symbol = input_list[1]
    
    num_type = type(storages[var_name])
    num_use = int(input_list[2]) if num_type is int else float(input_list[2])
    
    if cal_symbol == '+':
        storages[var_name] += num_use
    elif cal_symbol == '-':
        storages[var_name] -= num_use
    elif cal_symbol == '*':
        storages[var_name] *= num_use
    return storages

def count_comp(input_list,storages):
    # input_list [var_name save_var (finding char)]
    # var이 str인지 list인지에 따라 다르게 act하도록 짜기
    var_name = input_list[0]
    save_name = input_list[1]
    if len(input_list) >2:
        finding_char = input_list[2]
        if finding_char in storages.keys():
            finding_char = storages[finding_char]
    else:
        finding_char = None
    if finding_char is None: 
        storages[save_name] = len(storages[var_name])
    else:
        storages[save_name] = storages[var_name].count(finding_char)
    return storages