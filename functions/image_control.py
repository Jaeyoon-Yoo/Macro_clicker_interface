import pyautogui

def screenshot(input_list, storages):
    img_name = input_list[0]
    if img_name in storages.keys():
        img_name = storages[img_name]
                
    if len(input_list) > 1:
        region = input_list[1:]
    else:
        region = None
    
    if img_name != '':
        if region is not None:
            pyautogui.screenshot(img_name,region = (int(region[0]),int(region[1]),
                                                     int(region[2]),int(region[3])))
        else:
            pyautogui.screenshot(img_name)

def check_img(input_list, storages):
    # input_list : [img_name, result_name, confidence]
    img_name = input_list[0]
    result_name = input_list[1]
    if img_name in storages.keys():
        img_name = storages[img_name]
        
    if len(input_list) == 2:
        confidence = 0.7
    else:
        confidence = float(input_list[-1])
    
    if pyautogui.locateCenterOnScreen(img_name, confidence = confidence) is None:
        storages[result_name] = 0
    else:
        storages[result_name] = 1
    
    return storages
        
    
def click_img(input_list, storages):
    # input_list : [img_name, confidence, criteria if multiple(x,y)]
    img_name = input_list[0]
    if img_name in storages.keys():
        img_name = storages[img_name]
        
    if len(input_list) > 1:
        confidence = 0.7
    else:
        confidence = float(input_list[1])
        
    if len(input_list) > 3:
        criteria_x, criteria_y = int(input_list[2]), int(input_list[3])
    else:
        criteria_x, criteria_y = None, None
    
    if pyautogui.locateCenterOnScreen(img_name, confidence = confidence) is not None:
        if criteria_x is None:
            start = pyautogui.locateCenterOnScreen(img_name, confidence = confidence)
            pyautogui.moveTo(start)
            pyautogui.click()
        else:
            candi = pyautogui.locateAllOnScreen(img_name, confidence = confidence)
            candi_len = len(list(candi))
            if candi_len == 1:
                start = pyautogui.locateCenterOnScreen(img_name, confidence = confidence)
                pyautogui.moveTo(start)
                pyautogui.click()
            else:
                start_candi = pyautogui.locateAllOnScreen(img_name, confidence = confidence)
                candi_min = 1e8
                final_loc = [1,1]
                for candi in start_candi:
                    candi_left, candi_top= int(candi.left + candi.width/2), int(candi.top + candi.height/2)
                    candi_dist = (criteria_x-candi_left)**2 + (criteria_y-candi_top)**2
                    if candi_dist < candi_min:
                        candi_min = candi_dist
                        final_loc = [candi_left, candi_top]
                pyautogui.moveTo(final_loc[0],final_loc[1])
                pyautogui.click()

    