import cv2
import numpy as np
import time


vid = cv2.imread('ball.jpg')

###function to get contour from an image
def get_cont(img):
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    _,img=cv2.threshold(cv2.bitwise_not(img),127,255,0)
    contour,hier=cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    return contour


###function to get centroids of all contours
def get_centers(cont):
    n=len(cont)
    centers=[[0 for i in range (2)]for j in range(n)]
    for i in range(n):
        M=cv2.moments(cont[i])
        centers[i][0]=int(M['m10']/M['m00'])
        centers[i][1]=int(M['m01']/M['m00'])
    return centers


###function to get centroid of a single contour
def get_center(cont):
    M=cv2.moments(cont)
    center=[int(M['m10']/M['m00']),int(M['m01']/M['m00'])]
    return center

    
    
###calibrating arena
calib_pts=np.float32([[0,0]for i in range(4)])
four=0
start = False
new_calib=np.float32([[0,0],[0,500],[500,0],[500,500]])
M=[[0,0]for i in range(3)]

def calib(event,x,y,flags,param):
    global four,start,M
    if(event==cv2.EVENT_LBUTTONDOWN):
        print x,y
        if(four<4):
            cv2.circle(calib_frame,(x,y),10,(255,0,0),-1)
            cv2.imshow('calib',calib_frame)
            calib_pts[four][0]=x
            calib_pts[four][1]=y            
            if(four==3):
                start=True
                print "starting......."
                print calib_pts
                print new_calib
                cv2.destroyWindow('calib')
                M=cv2.getPerspectiveTransform(calib_pts,new_calib)                
            four=four+1
            
##in case of slow capturing
for i in range(10):          
    calib_frame = vid
    first_frame=np.copy(calib_frame)
    
cv2.imshow('calib',calib_frame)
cv2.setMouseCallback('calib',calib)



key = 0
esc=False
first_prev=True


###tracking
while (True):

    while start:
        if (first_prev):  
            prev_frame=cv2.warpPerspective(first_frame,M,(500,500))

            ##initial assignment
            initial_frame=np.copy(prev_frame)
            ini_cont=get_cont(initial_frame)
            unordered=get_centers(ini_cont)

            ##unordered to ordered
            '''
                x-->
            y
            |   0    1    2
            V
                3    4    5

                6    7    8

            '''
            sort_x=sorted([x[0] for x in unordered])
            x_sort = [sort_x[:3],sort_x[3:6],sort_x[6:]]
            
            sort_y=sorted([y[1] for y in unordered])
            y_sort = [sort_y[:3],sort_y[3:6],sort_y[6:]]
            

            ordered=[[0,0]for i in range(9)]
            
            order=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]] #as per the above order
            
            for i in range(9):
                ordered[i]=[elem for elem in unordered if(elem[0] in x_sort[order[i][0]] and elem[1] in y_sort[order[i][1]])]

            ordered=[al[0] for al in ordered]

            ##centers to contours
            ord_cont=np.copy(ini_cont)
            print ord_cont
            
            
            for i in range(9):
                ord_cont[i]=[elem for elem in ini_cont if (get_center(elem)==ordered[i])]
            ord_cont=[al[0] for al in ord_cont]

            #print "one",ordered
            #print 'two',get_centers(ord_cont)
                       

                                  
            
            ##order check
            #for each in get_centers(ord_cont):
            #    cv2.circle(initial_frame,(each[0],each[1]),10,(255,0,0),-1)
            #    cv2.imshow('check',initial_frame)
            #    cv2.waitKey(500)    

            prev_pts=ord_cont                        
            first_prev=False


            
        frame=vid
        current_frame=cv2.warpPerspective(frame,M,(500,500))
        current_pts=get_cont(current_frame)
        
        cv2.imshow('current',current_frame)
        print 'current',current_pts
        cv2.imshow('previous',prev_frame)
        print 'previous',prev_pts

        prev_frame=current_frame
        prev_pts=current_pts
        
        key=cv2.waitKey(1)
        if key==27:
            esc=True
            break
            
            
    if(esc==True):break  
        
    cv2.waitKey(1)
    
    
    
  
    
cv2.destroyAllWindows()





   
