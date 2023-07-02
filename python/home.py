from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import about
import login2
# from face_register import App


class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

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
            # dashboard_window.destroy()
            # app = App()
            # app.start() 
            # page()
                 pass  
        def delet_info():
            dashboard_window.withdraw()
            dashboard_window.destroy()            
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python/chat.py")

      

        home_bgImg = Image.open('python\\assets\\home.png')
        home_bgImg = home_bgImg.resize((1340, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        
        
        home_bgImg1 = Image.open('python\\assets\\homebtn.png')
        home_bgImg1= home_bgImg1.resize((140, 40))
        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, bg='#272A37')
        home_bg1.image = photo2
      
        home_bgImg2 = Image.open('python\\assets\\chat.png')
        home_bgImg2= home_bgImg2.resize((150, 50))
        photo3 = ImageTk.PhotoImage(home_bgImg2)
        home_bg2 = Label(homepage, image=photo3, bg='#272A37')
        home_bg2.image = photo3


        home_bgImg3 = Image.open('python\\assets\\face.png')
        home_bgImg2= home_bgImg2.resize((100, 40))
        photo4 = ImageTk.PhotoImage(home_bgImg3)
        home_bg3 = Label(homepage, image=photo4, )
        home_bg3.image = photo4
      
        home_bgImg4 = Image.open('python\\assets\\about.png')
        home_bgImg2= home_bgImg2.resize((130, 40))
        photo5 = ImageTk.PhotoImage(home_bgImg4)
        home_bg4 = Label(homepage, image=photo5, )
        home_bg4.image = photo5
       
        home_bgImg5 = Image.open('python\\assets\\logout.png')
        home_bgImg2= home_bgImg2.resize((110, 40))
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
        home_button.place(x=130, y=90)

        def about():
            pass

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
        chat_button.place(x=140, y=180)



         # ========== face  BUTTON =======
        face_button = Button(homepage,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=faceId)
        face_button.place(x=115, y=290)

        # ========== about  BUTTON =======
        about_button = Button(
            homepage, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,         
            command=about)
        about_button.place(x=90, y=400)
        





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
        logout_button.place(x=110, y=530)
        
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
                    messagebox.showinfo("welcome", f"{name} ,You are capable of amazing things. "  ) 
                else :

                    messagebox.showinfo("welcome", f" Hi {name}, why you are felling {emotion} , what happend with you today ?" ) 

            os.remove(file_path1)


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
