from functions import device_control
from functions import data_control
from functions import image_control

def run_functions(function_use,function_variables = None, storages = {}):
    # -------------------------------------------------------
    # device control (mouse, keyboard)
    if function_use == 'click':
        device_control.click(function_variables,storages)
    elif function_use == 'press_keyboard':
        device_control.press_keyboard(function_variables,storages)
    elif function_use == 'press_hotkey':
        device_control.press_hotkey(function_variables)
    elif function_use == 'wait':
        device_control.wait(function_variables)
    elif function_use == 'get_loc':
        device_control.get_loc()
    elif function_use == 'write_str':
        device_control.write_str(function_variables,storages)
    # -------------------------------------------------------
    # data control
    elif function_use == 'load_data':
        storages = data_control.load_data(function_variables,storages)
    elif function_use == 'new_var':
        storages = data_control.new_var(function_variables,storages)
    elif function_use == 'string_from':
        storages = data_control.string_from(function_variables,storages)
    elif function_use == 'clear_clip':
        data_control.clear_clip()
    elif function_use == 'check_type':
        data_control.check_type(function_variables,storages)
    elif function_use == 'change_type':
        storages = data_control.change_type(function_variables,storages)
    elif function_use == 'save_txt':
        data_control.save_txt(function_variables,storages)
    elif function_use == 'concat_str':
        storages = data_control.concat_str(function_variables,storages)
    elif function_use == 'compare_comp':
        storages = data_control.compare_comp(function_variables,storages)   
    elif function_use == 'calculate_comp':
        storages = data_control.calculate_comp(function_variables,storages)
    elif function_use == 'count_comp':
        storages = data_control.count_comp(function_variables,storages)
    # -------------------------------------------------------
    # image control
    elif function_use == 'screenshot':
        image_control.screenshot(function_variables,storages)
    elif function_use == 'check_img':
        storages = image_control.check_img(function_variables,storages)
    elif function_use == 'click_img':
        image_control.click_img(function_variables,storages)    
    # -------------------------------------------------------
    else:
        print(f'wrong function {function_use}')
    return storages