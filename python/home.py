from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import about
import login2
from face_register import App
import os.path
import tkinter as tk
import util
from  face_emotion import emotion
from PIL import Image, ImageTk



class FirstPage():
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Load the background image
        background_image = Image.open("python\\new\\home.png")
        background_image2 = Image.open("python\\new\\Guzel.png")

        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_photo2 = ImageTk.PhotoImage(background_image2)        
        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        

       

        

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#525561')

        # ====== MENU BAR ==========
        

        def faceId():
            dashboard_window.destroy()
            app = App()
            app.start() 
            page()
                #  pass  
        def delet_info():
            dashboard_window.withdraw()
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python\\Dashboard.py")
            os.system("python python/chat.py")
            dashboard_window.destroy()

      

        home_bgImg = Image.open('python\\new\\home.png')
        home_bgImg = home_bgImg.resize((1300, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        
        
        home_bgImg1 = Image.open('python\\new\\homentn.png')
        home_bgImg1= home_bgImg1.resize((130, 46))
        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, bg='#272A37')
        home_bg1.image = photo2
      
        home_bgImg2 = Image.open('python\\new\\chatbtn.png')
        home_bgImg2= home_bgImg2.resize((130, 46))
        photo3 = ImageTk.PhotoImage(home_bgImg2)
        home_bg2 = Label(homepage, image=photo3, bg='#272A37')
        home_bg2.image = photo3


        home_bgImg3 = Image.open('python\\new\\facid.png')
        home_bgImg2= home_bgImg2.resize((90,37))
        photo4 = ImageTk.PhotoImage(home_bgImg3)
        home_bg3 = Label(homepage, image=photo4, )
        home_bg3.image = photo4
      
        home_bgImg4 = Image.open('python\\new\\aboutbtn.png')
        home_bgImg2= home_bgImg2.resize((90,37))
        photo5 = ImageTk.PhotoImage(home_bgImg4)
        home_bg4 = Label(homepage, image=photo5, )
        home_bg4.image = photo5
       
        home_bgImg5 = Image.open('python\\new\\logout.png')
        home_bgImg2= home_bgImg2.resize((90, 37))
        photo6 = ImageTk.PhotoImage(home_bgImg5)
        home_bg5 = Label(homepage, image=photo6, )
        home_bg5.image = photo6


        
         
       
        
       

        # ========== HOME BUTTON =======
        home_button = Button(
            homepage, 
            image=photo2, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",)
        home_button.place(x=140, y=90)
        def about():
            dashboard_window.withdraw()
            os.system("python python\\about.py")
            dashboard_window.destroy()
        def chat():
            dashboard_window.withdraw()
            os.system("python python\\chat.py")
            dashboard_window.destroy()
                    
        
        # ========== chat BUTTON =======
        chat_button = Button(
            homepage, 
            image=photo3,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=chat
                    )
        chat_button.place(x=300, y=90)


         # ========== face  BUTTON =======
        face_button = Button(homepage,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=faceId)
        face_button.place(x=765, y=90)
        
        # ========== about  BUTTON =======
        about_button = Button(
            homepage, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,         
            command=about)
        about_button.place(x=460, y=90)
        





        def Dashboard():

            dashboard_window.withdraw()
            os.system("python python\\Dashboard.py")
            dashboard_window.destroy()
            
        # ========== LOG OUT =======
        logout_button = Button(homepage,  image=photo6,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" , command=delet_info
)
        logout_button.place(x=1000, y=90)
        self.Welcome()
               # ========== Welcome message =======
    def Welcome(self):
        file_path1 = 'most_emotion.txt'
        if os.path.exists(file_path1):
            with open(file_path1, 'r') as file:
                emotion = file.read()

            file_path2 = 'userinfo.txt'
            # Read the contents of the file
            with open(file_path2, 'r') as file:
                str_userinfo = file.read()
                userinfo=str_userinfo.split(",")
                name=userinfo[1]
                if emotion == "Neutral" :
                    self.pop(f"welcome {name} ,You are capable of amazing things. " )
                #     messagebox.showinfo("welcome", f"{name} ,You are capable of amazing things. "  ) 
                else :
                      self.pop(f"welcome, Hi {name}, why you are felling {emotion} , what happend with you today ?")
                #     messagebox.showinfo("welcome", f" Hi {name}, why you are felling {emotion} , what happend with you today ?" ) 

            os.remove(file_path1) 
    def chat2(self):
        self.register_new_user_window.destroy()
        os.system("python python\\chat.py")

        self.dashboard_window.destroy()
    def pop(self,text2):
        if hasattr(self, 'welcome') and self.register_new_user_window.winfo_exists():
            self.register_new_user_window.destroy()

        self.register_new_user_window = tk.Toplevel(self.dashboard_window)
        self.register_new_user_window.geometry("720x480")
        self.register_new_user_window.title("Register New User")

        # Use the existing background image label for the window
        self.background_label = tk.Label(self.register_new_user_window, image=self.background_photo2)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.accept_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'Chat', 'turquoise1', self.chat2
            
        )
        self.accept_button_register_new_user_window.place(x=160, y=120)

        self.try_again_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'close', 'navy', self.try_again_register_new_user
        )
        self.try_again_button_register_new_user_window.place(x=160, y=240)

        # Additional text
        self.additional_text_label = tk.Label(self.register_new_user_window, text=text2)
        self.additional_text_label.config(font=("Arial", 16))  # Increase font size to 16

        self.additional_text_label.place(x=160, y=20)

            # self.add_img_to_label(self.capture_label)
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()
def page():
    try:
        window = Tk()
        global mainPoag
        mainPoag=FirstPage(window)
        mainPoag
        mainPoag.Welcome()
        window.mainloop()
    except KeyboardInterrupt:
        FirstPage.delet_info()


if __name__ == '__main__':
    page()
