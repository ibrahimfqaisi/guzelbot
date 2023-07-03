import os.path
import datetime
import pickle
import tkinter as tk
import cv2
import face_recognition
import util
from  face_emotion import emotion
from PIL import Image, ImageTk

from PIL import Image, ImageTk
class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1340x690")


        self.register_new_user_button_main_window = util.get_button(self.main_window, 'add face id', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=800, y=300)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=60, width=700, height=500)

        self.add_webcam(self.webcam_label)
        self.email =    None
        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()
    def gitInfo(self):
        file_path = 'userinfo.txt'
        # Read the contents of the file
        with open(file_path, 'r') as file:
            str_userinfo = file.read()
            userinfo=str_userinfo.split(",")
            self.email=userinfo[2]


    def process_webcam(self):
        global ret, frame
        
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
   
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)


    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1340x690")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=60, width=700, height=500)

        self.add_img_to_label(self.capture_label)




    def des(self):
        self.cap.release()  # Release the webcam capture
        cv2.destroyAllWindows()
        self.main_window.destroy()

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        self.gitInfo()
        name = self.email

        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        # Specify the name and path of the file
        filename = '{}.pickle'.format(name)
        file_path = os.path.join(self.db_dir, filename)
        # Check if the file exists
        if os.path.exists(file_path):
            # Remove the existing file
            os.remove(file_path)

        # Open a new file and dump the data
        file = open(file_path, 'wb')
        pickle.dump(embeddings, file)
        file.close()

        util.msg_box('Success!', 'User was registered successfully !')

        self.register_new_user_window.destroy()
        self.des()

if __name__ == "__main__":
    app = App()
    app.start()