import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.togglebutton import ToggleButton

import time
from djitellopy import tello
import cv2
cv2.__version__

kivy.require('2.1.0')
kivy; print(kivy.__version__)

class CameraClick(BoxLayout):
    def capture(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.tello = tello.Tello()
        #self.image = Image()
        self.texture = None
        layout = BoxLayout()
        print("oui")
        while True:
            frame = self.tello.get_frame_read().frame
            
            self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = self.texture
            # self.ids.image_widget.texture = self.texture
            image_widget = Image(texture=self.texture)
            layout.add_widget(image_widget)
            return layout
            # layout.image_widget.texture = self.texture
            # #self.layout.clear_widgets()
            # self.add_widget(layout.image_widget)
            # self.ids.image_widget.texture = self.image_widget
            # return layout
            
    




class MainApp(App):
    def build(self):
        return CameraClick()
    

    def on_start(self):
        print("start")
        self.tello = tello.Tello()
        self.tello.connect()
        self.tello.streamon()

        

    def on_stop(self):
        self.tello.streamoff()
        self.tello.end()

    # def onoff(self, instance):
    #     self.tello = tello.Tello()
    #     if instance.text=='Start':
    #         self.tello.connect()
    #         self.tello.streamon()
    #         instance.text='Stop'
    #     else:
    #         self.tello.streamoff()
    #         self.tello.end()

if __name__ == '__main__':
    app = MainApp()
    app.run()
