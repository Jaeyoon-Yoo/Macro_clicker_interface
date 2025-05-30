from run.run_functions import run_functions
from run.run_storage import run_storage
from run.run_condition import run_condition
import os

def run_order(order_in, storages, line_idx =None, check_points =None, check_condi= {'global' : 1}):
    stat = 1
    if order_in == '':
        line_idx += 1
        return storages, stat, line_idx, check_points, check_condi
    order_in = order_in.split(' ')
    order_in = [x for x in order_in if x]
    
    chk = 1
    for i in check_condi.values():
        chk *= i
        
    if chk == 1:
        if order_in[0] == 'condition':
            condition_use = order_in[1]
            function_variables = order_in[2:]
            line_idx, check_points,check_condi = run_condition(condition_use,function_variables,storages,line_idx,check_points,check_condi)
        elif order_in[0] == 'check_condi':
            print(check_condi)
        elif order_in[0] == 'macro':
            macro_use = order_in[1]
            storages = run_macro(macro_use,storages)
        elif order_in[0] == 'storage':
            if len(order_in) > 1:
                run_storage(order_in[1:], storages)
        elif order_in[0] == 'exit': # macro 안에서의 exit은 macro를 exit하는 용이다.
            print('----- end program -----')
            stat = 0
        else:
            function_use = order_in[0]
            if len(order_in) == 1:
                function_variables = []
            else:
                function_variables = order_in[1:]
            storages = run_functions(function_use,function_variables,storages)
    else:
        if order_in[0] == 'condition':
            condition_use = order_in[1]
            function_variables = order_in[2:]
            if function_variables[0] in check_condi.keys():
                line_idx, check_points,check_condi = run_condition(condition_use,function_variables,storages,line_idx,check_points,check_condi)
    if line_idx is not None:
        line_idx += 1
    return storages, stat, line_idx, check_points, check_condi

def run_macro(macro_use, storages):
    check_points = {}
    check_condi= {'global' : 1}
    stat = 1
    macro_loc = storages['macro_dir']+macro_use
    if not os.path.exists(macro_loc):
        macro_loc = storages['sub_macro_dir']+macro_use
    f = open(macro_loc, "r")
    
    lines = f.readlines()
    lines = [line.replace('\n','') for line in lines]
    total_line = len(lines)
    line_idx = 0
    
    while stat:
        
        if line_idx == total_line:
            print(f'<<< {macro_use} macro done ! >>>')
            f.close()
            return storages
        
        line = lines[line_idx]
        if len(line) == 0:
            line_idx += 1
        elif line[0] == "-":
            print(line)
            line_idx += 1
        elif line[0] == "#":
            line_idx += 1
        else:
            storages, stat, line_idx, check_points, check_condi= run_order(line, storages,line_idx,check_points,check_condi)