def fn():
	import numpy
	import cv2
	img = cv2.imread('ball.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray,127,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	print len(contours)
	test = []
	point= [[[] for i in range(3)]for j in range(3)]	
	for i in range(1,len(contours)):
		cv2.drawContours(img,contours,i,(0,255,0),3)
		M = cv2.moments(contours[i])
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		#print "Centroid = ", cx, ", ", cy
		cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
		test.append(tuple([cx,cy]))		
	test = sorted(test , key=lambda k: [k[0]])	
	first = test[:3]
	second = test[3:6]
	third = test[6:9]
	first = sorted(first, key=lambda k: [k[1]])
	second = sorted(second, key=lambda k: [k[1]])
	third = sorted(third, key=lambda k: [k[1]])
	test = first+second+third
	print test	
	k=0
	for i in range (0,3):
		for j in range (0,3):
			point[i][j] = [test[k]]
			k+=1
	return point

	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
