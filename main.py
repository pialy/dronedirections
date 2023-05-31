#/usr/bin/python
from djitellopy import tello
import time
import cv2
import threading
from threading import Thread, Event
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_adress = ('192.168.10.1', 8889)
sock.bind(('',9000))

while True:
    try:
        msg = input('')
        if not msg:
            break
        if 'end' in msg:
            sock.close()
            break
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_adress)
    except Exception as err:
        print(err)
        sock.close()
        break



# me = tello.Tello()
# me.connect()
# print(me.get_battery())
# me.streamoff()
# me.streamon()
# me.takeoff()
# me.move_up(20)

# def rotation():
#         me.rotate_clockwise(90)
#         time.sleep(2)



# def camera():    
#     while True:
#         img = me.get_frame_read().frame
#         img = cv2.resize(img, (640, 480))
#         cv2.imshow("Image", img)
        
#         if cv2.waitKey(5) & 0xFF == ord('q'):
#             break


# started_evt = Event()
# y = threading.Thread(target=camera)
# x = threading.Thread(target=rotation)


# y.start()
# time.sleep(4)


# for i in range(8):
#     me.rotate_clockwise(45)
#     time.sleep(1)
    

# cv2.destroyAllWindows()



