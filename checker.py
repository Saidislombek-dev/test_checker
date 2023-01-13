import numpy as np
import cv2

def Check_answers(img, keys):
    
    #------------------ Inputs --------------------------------------------------
    
    img = cv2.resize(img,(1275,1650),cv2.INTER_CUBIC)    # test image

    gray_img = cv2.inRange(cv2.cvtColor(np.copy(img),cv2.COLOR_RGB2GRAY),0,200)   # gray image
    
    img_copy = np.copy(img)    # copy image
    colors = [(255,255,0),(0,255,0),(255,0,0)]  # yellow, green, red
    
    pos = [170, 195, 193, 184, 181, 181]  # position point in x coordinate
    
    #------------------ Checking answers ----------------------------------------
    
    num_ans = []
    for i in range(431,1468,148):
        for j in range(6):
            a = 0
            square = np.copy(gray_img[i-60:i+59,sum(pos[:j+1])-59:sum(pos[:j+1])+60])
            circle1 = cv2.circle(np.copy(square), (59,59), 50, 0, -1)
            circle2 = cv2.circle(np.copy(square), (59,59), 50, 0, 25)
            if circle1.sum()>27000:
                a = 2
            else:
                if circle2.sum()>20000:
                    a = 2
                if circle2.sum()>880000:
                    a = 1
                    
            cv2.rectangle(img_copy,(sum(pos[:j+1])-59,i-60),(sum(pos[:j+1])+60,i+59),colors[a],3)
            num_ans.append(a)
            
    #------------------- Counting correct answers ----------------------------------
            
    s = 0
    k = ['A','B','C','D','E','F']
    for i in range(8):
        if sum(num_ans[i*6:(i+1)*6])==1:
            ans = k[num_ans[i*6:(i+1)*6].index(1)]
        else:
            ans = 'X'
        
        if ans==keys[i]:
            s += 1
            
            
    return img_copy,s     # checked image vs correct answers count
