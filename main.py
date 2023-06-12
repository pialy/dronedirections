

from djitellopy import tello
import time
import cv2
import threading
from threading import Thread, Event
from production.linedetection.src.scripts.lines import detect_line
import json
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent


me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamoff()
me.streamon()
me.takeoff()

# temp = 0
# while (temp < 8):
#     me.rotate_clockwise(45)
#     time.sleep(1)
#     temp=temp+1

# me.move_forward(60)


def rotation():
        me.rotate_clockwise(90)
        time.sleep(2)



def camera():    
    n = 0
    temp = 0
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Image", img)
        

        # typesOpt = {
        #     "names" : {
        #         "LINES" : 0,
        #         "FILTERED_LINES" : 1,
        #         "LONG_LINES" : 2
        #     },
        #     "values" : [
        #         "lines",
        #         "filtered_lines",
        #         "long_lines"
        #     ],
        #    "criterias" : {
        #         "MIN_LENGTH" : 120,
        #         "MAX_VERTICAL_POSITION" : 120,
        #         "MAX_CENTER_DISTANCE" : 150,
        #         "MIN_ANGLE" : 1
        #     },
        #     "filters" : {
        #         "LENGTH" : 0,
        #         "FORWARD" : 1,
        #         "BOTTOM" : 2
        #     }
        # }

        # r, line = detect_line(img, typesOpt['filters']['FORWARD'])
        # if line is not None :
        #     print(f"Tracking line : {line}")
        #     moves = line['moves']
        #     mx = moves['horizontalMove']
        #     my1 = moves['firstVerticalDistance']
        #     my2 = moves['verticalDestination']
        #     cv2.imshow("Image", r)
        #     time.sleep(2)
        #     me.move_forward(150)
            
        
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        #time.sleep(1)

    
        


started_evt = Event()
y = threading.Thread(target=camera)
x = threading.Thread(target=rotation)


y.start()
time.sleep(6)
me.move_left(20)


   
#me.move_forward(20)



    

cv2.destroyAllWindows()



