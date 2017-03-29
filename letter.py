def k(a):
        import numpy as np
        import cv2
	import os
	dirname = 'runtime'
        img = cv2.imread('A-Z/'+str(a)+'.jpg')
        seba = cv2.imread('vj.png')
        returner= [[[] for i in range(3)]for j in range(3)]
        i = 1
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        #print x , "," , y, "," , h
        box_w=w/3
        box_h=h/3
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        arr = []
        p=0
        q=0	
        for j in range(x,w,box_w):
                for k in range(y,h,box_h):
                        roi = img[k:k+box_h,j:j+box_w]
                        gray = cv2.bitwise_not(cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY))
                        ret,thresh = cv2.threshold(gray,127,255,0)
                        contours1, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        #cv2.drawContours(roi,contours1,0,(0,255,0),3)
                        #cent_x = j+box_w/2
                        #cent_y = k+box_h/2
                        #print (cent_x) , "," , (cent_y)
			if a==0 or a==5:
				if p==1 and q==2:
					continue
			if a==1:
				if p==2 and q==0:
					returner[p][q] = [338,160]
					cv2.circle(seba,(338,160), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==0:
					returner[p][q] = [260,94]
					cv2.circle(seba,(260,94), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==1:
					returner[p][q] = [260,241]
					cv2.circle(seba,(260,241), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==2:
					returner[p][q] = [254,406]
					cv2.circle(seba,(254,406), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==1:
					returner[p][q] = [338,290]
					cv2.circle(seba,(338,290), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==2:
					returner[p][q] = [334,375]
					cv2.circle(seba,(334,375), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==16:
				if p==1 and q==1:
					returner[p][q]=[312,322]
                                	cv2.circle(seba,(312,322), 15, (0,0,255), -1)
				if p==2 and q==2:
					returner[p][q]=[407,428]
                                	cv2.circle(seba,(407,428), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==25:
				if p==0 and q==1:
					returner[p][q]=[165,332]
                                	cv2.circle(seba,(165,332), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==0:
					returner[p][q]=[412,94]
                                	cv2.circle(seba,(412,94), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==1:
					returner[p][q]=[248,260]
                                	cv2.circle(seba,(248,260), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==1:
					returner[p][q]=[336,180]
                                	cv2.circle(seba,(336,180), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==24:
				if p==1 and q==0:
					q=q+1
					continue
				if p==1 and q==1:
					returner[p][q]=[247,278]
                                	cv2.circle(seba,(247,278), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==23:				
				if p==2 and q==1:
					returner[p][q]=[289,314]
                                	cv2.circle(seba,(289,314), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==2:
					returner[p][q]=[199,314]
                                	cv2.circle(seba,(199,314), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==1 and q==0:
					returner[p][q]=[290,162]
                                	cv2.circle(seba,(290,162), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==0 and q==1:
					returner[p][q]=[200,162]
                                	cv2.circle(seba,(200,162), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==22:
				if p==1 and q==0:
					q=q+1
					continue
				if p==1 and q==2:
					q=q+1
					continue
				if p==0 and q==2:
					returner[p][q]=[140,344]
                                	cv2.circle(seba,(140,344), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==2:
					returner[p][q]=[354,344]
                                	cv2.circle(seba,(354,344), 15, (0,0,255), -1)
					q=q+1
					continue
			if a==21:
				if p==1 and q==1:
					q=q+1
					continue
				if p==0 and q==1:
					returner[p][q]=[193,247]
                                	cv2.circle(seba,(193,247), 15, (0,0,255), -1)
					q=q+1
					continue
				if p==2 and q==1:
					returner[p][q]=[309,247]
                                	cv2.circle(seba,(309,247), 15, (0,0,255), -1)
					q=q+1
					continue
					
			if a==13:
				if p==1 and q==0:
					q=q+1
					continue
				if p==1 and q==2:
					q=q+1
					continue	
				if p==0 and q==1:
					returner[p][q]=[140,238]
                                	cv2.circle(seba,(140,238), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==0 and q==2:
					returner[p][q]=[108,353]
                                	cv2.circle(seba,(108,353), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==2 and q==1:
					returner[p][q]=[366,238]
                                	cv2.circle(seba,(366,238), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==2 and q==2:
					returner[p][q]=[334,353]
                                	cv2.circle(seba,(334,353), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==2 and q==0:
					returner[p][q]=[400,118]
                                	cv2.circle(seba,(400,118), 15, (0,0,255), -1)
					q = q+1
					continue
			if a==9 and q==0 and p==1:
				returner[p][q]=[270,164]
                                cv2.circle(seba,(270,164), 15, (0,0,255), -1)
				q=q+1
				continue
			if a==10 and p==1 and q==1:
				returner[p][q]=[220,252]
                                cv2.circle(seba,(220,252), 15, (0,0,255), -1)
				q=q+1
				continue				
			if a==12 :				
				if q==0 and p==1:
					q = q+1					
					continue
				if p==0 and q==1:
					returner[p][q]=[93,243]
                                	cv2.circle(seba,(93,243), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==0 and q==2:
					returner[p][q]=[43,384]
                                	cv2.circle(seba,(43,384), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==1 and q==1:
					returner[p][q]=[250,210]
                                	cv2.circle(seba,(250,210), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==2 and q==1:
					returner[p][q]=[407,243]
                                	cv2.circle(seba,(407,243), 15, (0,0,255), -1)
					q = q+1
					continue
				if p==2 and q==2:
					returner[p][q]=[457,384]
                                	cv2.circle(seba,(457,384), 15, (0,0,255), -1)
					q = q+1
					continue
							
															
                        if len(contours1) >0 :
                                if len(contours1)<2:
                                        if cv2.contourArea(contours1[0])>1120:                                
                                                c = contours1[len(contours1)-1]
                                                M = cv2.moments(c)
                                                cx1 = int(M['m10']/M['m00'])
                                                cy1 = int(M['m01']/M['m00'])						
                                                returner[p][q] =[j+cx1,k+cy1]
                                                cv2.circle(seba,(j+cx1,k+cy1), 15, (0,0,255), -1)
                                                cv2.circle(img,(j+cx1,k+cy1), 5, (0,0,255), -1)
                                else:
                                        if cv2.contourArea(contours1[0])>0:                                
                                                c = contours1[len(contours1)-1]
                                                M = cv2.moments(c)
                                                cx1 = int(M['m10']/M['m00'])
                                                cy1 = int(M['m01']/M['m00'])
                                                returner[p][q]=[j+cx1,k+cy1]
                                                cv2.circle(seba,(j+cx1,k+cy1), 15, (0,0,255), -1)
                                                cv2.circle(img,(j+cx1,k+cy1), 5, (0,0,255), -1)
                        #cv2.rectangle(img,(j,k),(j+box_w,k+box_h),(0,0,255),2)
                        q = q+1
			if a==9:
				cv2.circle(seba,(160,164), 15, (0,0,255), -1)
				returner[0][0]=[160,164]
				cv2.circle(seba,(380,164),15,(0,0,255),-1)
				returner[2][0]=[380,164]
				
                p=p+1
                q=0
         
        cv2.imshow('seba',seba)
	face_file_name = 'runtime'+str(a)+'.jpg'
        cv2.imwrite(os.path.join(dirname, face_file_name),seba)
        cv2.imshow('image',img)
        return returner        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
