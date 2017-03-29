import cv2
import letter
import contour
import json
import math

pos = [[[] for i in range(3)] for j in range(3)]
can1 = cv2.imread('vj.png')
s = raw_input("Enter a word \n")
s = s.upper()
word = list(s)
length = len(s)
# p = 0
# q = 0
counter = 0
'''for i in range (147,400,111):
        for j in range(117,400,132):
                pos[p][q] =[(i,j)]
                q = q+1
        p = p+1
        q=0'''
pos = contour.fn()
previous = [[[] for i in range(3)] for j in range(3)]
for i in range(0, 3):
    for j in range(0, 3):
        previous[j][i] = pos[j][i]
# print pos

for i in range(0, length):
    can = cv2.imread('vj.png', 0)
    can1 = cv2.imread('vj.png')
    let = word[i]
    kq = ord(let) - 65
    finalpos = letter.k(kq)
    # print finalpos[0][0]
    for i in range(3):
        for j in range(3):
            if len(finalpos[i][j]) > 0:
                cv2.circle(can1, (finalpos[i][j][0], finalpos[i][j][1]), 10, (0, 0, 255), -1)

    for i in range(3):
        for j in range(3):
            cv2.circle(can1, (pos[i][j][0][0], pos[i][j][0][1]), 5, (255, 0, 0), -1)

    flag = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if len(finalpos[i][j]) == 0:
                if i == 1 and j == 1 and len(finalpos[1][0]) is not 0:
                    cv2.line(can1, pos[i][j][0], tuple(finalpos[1][0]), (0, 255, 255), 2)
                    pos[i][j] = [tuple(finalpos[1][0])]
                    pos[1][0] = [(pos[1][0][0][0], 15)]
                    flag = 1
                elif i==1 and j==1 and len(finalpos[1][0])is 0 and len(finalpos[0][1]) is not 0:
                    cv2.line(can1, pos[i][j][0], tuple(finalpos[0][1]), (0, 255, 255), 2)
                    pos[i][j] = [tuple(finalpos[0][1])]
                    pos[0][1] = [(1,pos[0][1][0][1])]


                elif i == 0:
                    cv2.line(can1, pos[i][j][0], (30, pos[i][j][0][1]), (0, 255, 0), 2)
                    pos[i][j] = [(1, pos[i][j][0][1])]
                elif i == 2:

                    cv2.line(can1, pos[i][j][0], (480, pos[i][j][0][1]), (0, 255, 0), 2)
                    pos[i][j] = [(500, pos[i][j][0][1])]
                elif i == 1 and j == 0:
                        cv2.line(can1, pos[i][j][0], (pos[i][j][0][0], 20), (0, 255, 0), 2)
                        pos[i][j] = [(pos[i][j][0][0], 10)]

                elif i == 1 and j == 1 and len(finalpos[1][0]) is 0:
                    cv2.line(can1, pos[i][j][0], (pos[1][1][0][0], 20), (0, 255, 0), 2)
                    pos[i][j] = [(pos[i][j][0][0], 10)]
                elif i == 1 and j == 2:
                    cv2.line(can1, pos[i][j][0], (pos[i][j][0][0], 480), (0, 255, 0), 2)
                    pos[i][j] = [(pos[i][j][0][0], 500)]

            elif len(finalpos[i][j]) > 0:
                if len(finalpos[1][0]) > 0 and len(finalpos[1][1]) == 0 and i == 1 and j == 0:
                    cv2.line(can1, pos[1][0][0], (pos[1][0][0][0], 20), (0, 255, 0), 2)
                    pos[1][0] = [(pos[1][0][0][0], 1)]

                elif len(finalpos[0][1]) > 0 and len(finalpos[1][1]) == 0 and i == 0 and j == 1 and len(finalpos[1][0])==0:
                    cv2.line(can1, pos[0][1][0], (30,pos[0][1][0][1]), (0, 255, 0), 2)
                    pos[0][1] = [(500,pos[0][1][0][1])]
                else:
                    cv2.line(can1, pos[i][j][0], tuple(finalpos[i][j]), (0, 255, 255), 2)
                    pos[i][j] = [tuple(finalpos[i][j])]

    dis = [[[] for i in range(3)] for j in range(3)]
    deg = [[[] for i in range(3)] for j in range(3)]
    # print previous[0][0]
    for i in range(0, 3):
        for j in range(0, 3):
            # print pos[j][i]
            # dis = math.sqrt(math.pow((pos[j][i][0][1]-previous[j][i][0][1]),2)-math.pow((pos[j][i][0][0]-previous[j][i][0][0]),2))
            lega = math.pow((pos[j][i][0][1] - previous[j][i][0][1]), 2)
            pega = math.pow((pos[j][i][0][0] - previous[j][i][0][0]), 2)
            dis[i][j] = math.sqrt(lega + pega)
            print dis[i][j]
            y2 = pos[j][i][0][1]
            y1 = previous[j][i][0][1]
            x2 = pos[j][i][0][0]
            x1 = previous[j][i][0][0]
            if x1 == x2 and y1 == y2:
                deg[i][j] = 0
            elif x1 == x2 and y1 is not y2 :
                if y1 > y2:
                    deg[i][j] = 0
                else:
                    deg[i][j] = 90
            elif y1 == y2 and x1 is not x2 :
                if x1 > x2 :
                    deg[i][j] = 270
                else:
                    deg[i][j] = 90
            else:
                rad = math.atan2((y2 - y1), (x2 - x1))
                deg[i][j] = rad * 180 / math.pi
                if deg[i][j] < 0:
                    deg[i][j] = 360 + deg[i][j]
                if x2 - x1 >= 0 and y2 - y1 <= 0:
                    deg[i][j] = deg[i][j] - 270
                else:
                    deg[i][j] = deg[i][j] + 90
            print deg[i][j], " clockwise"
            previous[j][i] = pos[j][i]

        print " "
    counter = counter + 1
    out = {'distance': dis[0][0], 'counter' : counter, 'angle' : deg[0][0]}
    with open('/var/www/html/swarm1/light.json', 'w')as outfile:
    	json.dump(out, outfile)
    out1 = {'distance': dis[0][1], 'counter' : counter, 'angle' : deg[0][1]}
    with open('/var/www/html/swarm2/light.json', 'w')as outfile:
    	json.dump(out1, outfile)
    out2 = {'distance': dis[0][2], 'counter' : counter, 'angle' : deg[0][2]}
    with open('/var/www/html/swarm3/light.json', 'w')as outfile:
    	json.dump(out2, outfile)
    out3 = {'distance': dis[1][0], 'counter' : counter, 'angle' : deg[1][0]}
    with open('/var/www/html/swarm4/light.json', 'w')as outfile:
    	json.dump(out3, outfile)
    out4 = {'distance': dis[1][1], 'counter' : counter, 'angle' : deg[1][1]}
    with open('/var/www/html/swarm5/light.json', 'w')as outfile:
    	json.dump(out4, outfile)
    out5 = {'distance': dis[1][2], 'counter' : counter, 'angle' : deg[1][2]}
    with open('/var/www/html/swarm6/light.json', 'w')as outfile:
    	json.dump(out5, outfile)
    out6 = {'distance': dis[2][0], 'counter' : counter, 'angle' : deg[2][0]}
    with open('/var/www/html/swarm7/light.json', 'w')as outfile:
    	json.dump(out6, outfile)
    out7 = {'distance': dis[2][1], 'counter' : counter, 'angle' : deg[2][1]}
    with open('/var/www/html/swarm8/light.json', 'w')as outfile:
    	json.dump(out7, outfile)
    out8 = {'distance': dis[2][2], 'counter' : counter, 'angle' : deg[2][2]}
    with open('/var/www/html/swarm9/light.json', 'w')as outfile:
    	json.dump(out8, outfile)
    
    cv2.imshow('k', can1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
out = {'distance': 0, 'counter' : 0, 'angle' : 0}
with open('/var/www/html/swarm1/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm2/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm3/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm4/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm5/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm6/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm7/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm8/light.json', 'w')as outfile:
    	json.dump(out, outfile)
with open('/var/www/html/swarm9/light.json', 'w')as outfile:
    	json.dump(out, outfile)
