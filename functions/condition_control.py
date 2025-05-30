

def loop_start(input_list,storages,line_idx,check_points,check_condi,type_condi):
    # input_list : [cp_name bool_condition(run loop if 0) (not if you want to run loop when 1)]
    # if 문은 bool condition이 1일때 작동한다
    cp_name = input_list[0]
    condi_name = input_list[1]
    condi_check = 1-storages[condi_name]
    if type_condi == 'if':
        condi_check = 1-condi_check
    if len(input_list) > 2:
        if input_list[2] == 'not': # if 문은 not 붙여주어 사용하면 됨
            condi_check = 1-condi_check
    check_points[cp_name] = line_idx-1
    check_condi[cp_name] = condi_check
    return check_points,check_condi

def loop_end(input_list,line_idx,check_points,check_condi,type_condi):
    # input_list : [cp_name (pass)]
    # if 문은 pass안적어도 된다.
    cp_name = input_list[0]
    if len(input_list) >1:
        cp_pass = input_list[1]
    elif type_condi == 'if':
        cp_pass = 'pass'
    else:
        cp_pass = None
        
    if check_condi[cp_name] == 1:
        if cp_pass != 'pass':
            line_idx = check_points[cp_name]
    else:
        check_condi[cp_name] = 1
    
    
    return line_idx,check_condi