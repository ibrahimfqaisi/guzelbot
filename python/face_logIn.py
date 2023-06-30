import os.path
import datetime
import tkinter as tk
import cv2
import util
from  face_emotion import emotion
import hashlib
import psycopg2


from PIL import Image, ImageTk
class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")


        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()
    def des(self):
        cv2.destroyAllWindows()
        self.main_window.destroy()        
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
    def saveData(self,get_email):
    # Implement the login functionality here
        email = get_email

        # Connect to the PostgreSQL database
        conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
        cursor = conn.cursor()

        # Check if the email exists in the database
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
                    file_path = 'userinfo.txt'
                    # Save the JSON data to a file
                    with open(file_path, 'w+') as json_file:
                        json_file.write(f"{user[0]},{user[1]},{user[2]}")                                   
 
   
    def login(self):

            emotion(self.cap )

            
            name = util.recognize(self.most_recent_capture_arr, self.db_dir)

            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
            else:
                get_email=name
                self.saveData(get_email)
                print('Welcome back !', 'Welcome, {}.'.format(name))
            self.des()

    def des(self):
        self.cap.release()  # Release the webcam capture
        cv2.destroyAllWindows()
        self.main_window.destroy()

    def start(self):
        self.main_window.mainloop()

  

if __name__ == "__main__":
    app = App()
    app.start()