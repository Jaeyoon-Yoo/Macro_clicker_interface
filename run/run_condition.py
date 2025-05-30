from functions import condition_control

def run_condition(condition_use, function_variables, storages, line_idx, check_points,check_condi):
    if condition_use == 'loop_start':
        check_points,check_condi = condition_control.loop_start(function_variables,storages,line_idx,check_points,check_condi,'loop')
    elif condition_use == 'loop_end':
        line_idx,check_condi = condition_control.loop_end(function_variables,line_idx,check_points,check_condi,'loop')
    elif condition_use == 'if_start':
        check_points,check_condi = condition_control.loop_start(function_variables,storages,line_idx,check_points,check_condi,'if')
    elif condition_use == 'if_end':
        line_idx,check_condi = condition_control.loop_end(function_variables,line_idx,check_points,check_condi,'if')    
    elif condition_use == 'clear':
        check_condi = {}
    return line_idx, check_points,check_condi