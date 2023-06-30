from tkinter import *
import login2
from PIL import ImageTk, Image
from signup_page import signup

'''
Sajeda
Ibrahim
Bayan 
Aseel
'''

window = None
def destroy_signup_page():
     global window
     window.destroy()


def regestier():
    global window
    window = Tk()
    
    height = 690
    width = 1340
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")
   

    # ================Background Image ====================
    home_bgImg = Image.open('python\\assets\\regbg.png')
    home_bgImg = home_bgImg.resize((1340, 690))

    photo = ImageTk.PhotoImage(home_bgImg)
    home_bg = Label( image=photo, bg='#525561')
    home_bg.image = photo
    home_bg.place(x=0, y=0)


   


    

    # ================ GO TO LOGIN ====================
    login_img=PhotoImage(file="python\\assets\\rgbt.png")
    switchLogin = Button(
        home_bg,
        image=login_img,
        text="Login",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        
        command=lambda  : [destroy_signup_page(),login2.loginpage()]

        
        
        
    )
    
    switchLogin.place(x=250, y=133 )

    # ================ First Name Section ====================
    firstName_image = PhotoImage(file="python\\assets\\lable1.png")
    firstName_image_Label = Label(
        home_bg,
        image=firstName_image,
        bg="black"
    )
    firstName_image_Label.place(x=30, y=260,)


    firstName_entry = Entry(
        firstName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    firstName_entry.place(x=13, y=15, width=100, height=27 )


    # ================ Last Name Section ====================
    lastName_image = PhotoImage(file="python\\assets\\lable1.png")
    lastName_image_Label = Label(
        home_bg,
        image=lastName_image,
        bg="black"
    )
    lastName_image_Label.place(x=225, y=260)


    lastName_entry = Entry(
        lastName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    lastName_entry.place(x=13, y=15, width=100, height=27)

    # ================ Email Name Section ====================
    emailName_image = PhotoImage(file="python\\assets\\lable2.png")
    emailName_image_Label = Label(
        home_bg,
        image=emailName_image,
        borderwidth=0,
        bg="#272A37"
    )
    emailName_image_Label.place(x=50, y=390)


   

    emailName_entry = Entry(
        emailName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    emailName_entry.place(x=12, y=12, width=200, height=27)


    # ================ Password Name Section ====================
    passwordName_image = PhotoImage(file="python\\assets\\lable1.png")
    passwordName_image_Label = Label(
        home_bg,
        borderwidth=0,
        image=passwordName_image,
        bg="black"
    )
    passwordName_image_Label.place(x=30, y=490)

 

    passwordName_entry = Entry(
        passwordName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    passwordName_entry.place(x=13, y=15, width=120, height=27)


    # # ================ Confirm Password Name Section ====================
    confirm_passwordName_image = PhotoImage(file="python\\assets\\lable1.png")
    confirm_passwordName_image_Label = Label(
        home_bg,
        borderwidth=0,
        image=confirm_passwordName_image,
        bg="#272A37"
    )
    confirm_passwordName_image_Label.place(x=240, y=490)

   



    confirm_passwordName_entry = Entry(
        confirm_passwordName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    confirm_passwordName_entry.place(x=13, y=15, width=120, height=27)

    # =============== Submit Button ====================
    submit_buttonImage = PhotoImage(
        file="python\\assets\\signupbtn.png")
    submit_button = Button(
        home_bg,
        image=submit_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        bg='black',
        command=lambda:signup(firstName_entry,lastName_entry,emailName_entry,passwordName_entry)
    )
    submit_button .place(x=170, y=560)

   


    window.resizable(False, False)
    window.mainloop()

   
if __name__ == '__main__':
    regestier()