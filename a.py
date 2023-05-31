# import kivy
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# import time
# from djitellopy import Tello

# kivy.require('2.1.0')

# class CameraClick(BoxLayout):
#     def __init__(self, **kwargs):
#         super(CameraClick, self).__init__(**kwargs)
#         self.tello = Tello()
#         self.tello.connect()
#         self.tello.streamon()

#     def capture(self):
#         camera = self.ids['camera']
#         timestr = time.strftime("%Y%m%d_%H%M%S")

# class atest(App):
#     def build(self):
#         camera_click = CameraClick(drone=self.tello)
#         return camera_click

# testApp = atest()
# testApp.run()