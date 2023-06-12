
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


def rotation():
        me.rotate_clockwise(90)
        time.sleep(2)



def camera():    
    n = 0
    temp = 0

    minLength = 125

    typesOpt = {
        "names" : {
            "LINES" : 0,
            "FILTERED_LINES" : 1,
            "LONG_LINES" : 2
        },
        "values" : [
            "lines",
            "filtered_lines",
            "long_lines"
        ],
        "criterias" : {
            "MIN_LENGTH" : 100,
            "MAX_VERTICAL_POSITION" : 200,
            "MAX_CENTER_DISTANCE" : 200,
            "MIN_ANGLE" : 1
        },
        "filters" : {
            "LENGTH" : 0,
            "FORWARD" : 1,
            "BOTTOM" : 2
        }
    }

    firstVerticalDistance = 0
    n = 0

    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Image", img)

        r, line, m = detect_line(img, typesOpt['filters']['FORWARD'], minLength)
        if line is not None :
            print(f"Tracking line : {line}")

            n += 1

            cv2.imshow("Image", r)
            
            mx1Cm, my1Cm, my2Cm = m
            if mx1Cm < 0 :
                # Move on the LEFT
                me.move_left(-mx1Cm)
            elif mx1Cm > 0 :
                # Move on the RIGHT
                me.move_right(mx1Cm)
            
            me.move_forward(my1Cm)
            me.move_forward(my2Cm)

            if minLength > 0 :
                if my2Cm == line['moves']['verticalDestination'] :
                    minLength -= 30
            
            print(f"Minimum length : {minLength}")
            time.sleep(1)  

        elif n != 0 :
            n = 0
            me.move_forward(80)                  

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    
        


started_evt = Event()
y = threading.Thread(target=camera)

y.start()
time.sleep(6)


   

cv2.destroyAllWindows()



