import cv2
import letter
import contour
import json
import math
pos= [[[] for i in range(3)]for j in range(3)]
can1=cv2.imread('vj.png')
s = raw_input("Enter a word \n")
s = s.upper()
word = list(s)
length = len(s)
#p = 0
#q = 0
'''for i in range (147,400,111):
        for j in range(117,400,132):
                pos[p][q] =[(i,j)]
                q = q+1
        p = p+1
        q=0'''
pos = contour.fn()
previous = [[[] for i in range(3)]for j in range(3)]
for i in range(0,3):
	for j in range(0,3):
		previous[j][i] = pos[j][i]
#print pos
         
for i in range(0,length):
    can=cv2.imread('vj.png',0)
    can1=cv2.imread('vj.png')
    let = word[i]
    kq = ord(let)-65
    finalpos=letter.k(kq)    
    #print finalpos[0][0]    
    for i in range(3):
            for j in range(3):                    
                    if len(finalpos[i][j])>0:                            
                            cv2.circle(can1,(finalpos[i][j][0],finalpos[i][j][1]),10,(0,0,255),-1)
    
    for i in range (3):
            for j in range(3):                   
                    cv2.circle(can1,(pos[i][j][0][0],pos[i][j][0][1]),5,(255,0,0),-1) 
                   
	    
    flag = 0    
    for i in range(0,3):            
            for j in range(0,3):                    
                    if len(finalpos[i][j])==0:
                            if i==1 and j==1 and len(finalpos[1][0]) is not 0:
                                    cv2.line(can1,pos[i][j][0],tuple(finalpos[1][0]),(0,255,255),2)
                                    pos[i][j] = [tuple(finalpos[1][0])]
                                    pos[1][0] = [(pos[1][0][0][0],30)]
                                    flag = 1
				
                            elif i==0:
                                    cv2.line(can1,pos[i][j][0],(30,pos[i][j][0][1]),(0,255,0),2)
                                    pos[i][j] = [(30,pos[i][j][0][1])]
                            elif i==2:

                                    cv2.line(can1,pos[i][j][0],(470,pos[i][j][0][1]),(0,255,0),2)
                                    pos[i][j] = [(470,pos[i][j][0][1])]                                   
                            elif i==1 and j == 0:
                                    cv2.line(can1,pos[i][j][0],(pos[i][j][0][0],30),(0,255,0),2)
                                    pos[i][j] = [(pos[i][j][0][0],30)]
                            elif i==1 and j == 2:
                                    cv2.line(can1,pos[i][j][0],(pos[i][j][0][0],480),(0,255,0),2)
                                    pos[i][j] = [(pos[i][j][0][0],480)]
                                    
			    elif i==1 and j==1 and len(finalpos[1][0]) is 0:
                                   	cv2.line(can1,pos[i][j][0],(pos[1][1][0][0],30),(0,255,0),2)
                                   	pos[i][j] = [(pos[i][j][0][0],30)]
                                   	
                    elif len(finalpos[i][j])>0:                           
                            if flag=1:
                               cv2.line(can1,temp,(pos[1][0][0][0],30),(0,255,0),2)
                              
                            cv2.line(can1,pos[i][j][0],tuple(finalpos[i][j]),(0,255,255),2)
                            temp = pos[1][0][0]                        
                            pos[i][j] = [tuple(finalpos[i][j])]
        		    
    dis = [[[] for i in range(3)]for j in range(3)]
    deg = [[[] for i in range(3)]for j in range(3)]
    #print previous[0][0]
    for i in range(0,3):
	for j in range(0,3):
		#print pos[j][i]
		#dis = math.sqrt(math.pow((pos[j][i][0][1]-previous[j][i][0][1]),2)-math.pow((pos[j][i][0][0]-previous[j][i][0][0]),2))
		lega = math.pow((pos[j][i][0][1]-previous[j][i][0][1]),2) 
		pega = math.pow((pos[j][i][0][0]-previous[j][i][0][0]),2)
		dis[i][j]= math.sqrt(lega+pega)
		print dis[i][j]
		y2 = pos[j][i][0][1]
		y1 = previous[j][i][0][1]
		x2 = pos[j][i][0][0]
		x1 = previous[j][i][0][0]
		rad = math.atan2((y2-y1),(x2-x1))				
		deg[i][j] = rad*180/math.pi
		if deg[i][j]<0:
			deg[i][j] = 360 + deg[i][j]
		if x2-x1>=0 and y2-y1<=0:
			deg[i][j] = deg[i][j] - 270
		else:
			deg[i][j] = deg[i][j] + 90		
		print deg[i][j] , " clockwise"
		previous[j][i] = pos[j][i]
		
		
	print " "
                                         
    '''out = {'distance': dis[0][0]}
    with open('/var/www/html/test/light.json', 'w')as outfile:  
    	json.dump(out, outfile)'''
    cv2.imshow('k',can1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
