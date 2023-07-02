from tkinter import *
import register_page
import os 
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox
import psycopg2
import hashlib
import reset_page
import Dashboard

'''
Sajeda
Ibrahim
Bayan 
Aseel
'''

def show_custom_error(title, message):
    global win
    win = Toplevel()
    
    window_width = 350
    window_height = 150
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    win.title(title)
    win.configure(background="#272A37")
    win.resizable(False, False)

    label = Label(win, text=message, fg="white", bg="#272A37")
    label.pack(pady=20)

    ok_button = Button(win, text="OK", command=win.destroy)
    ok_button.pack(pady=10)
def login():
    # Implement the login functionality here
    email = Login_emailName_entry.get()
    password = Login_passwordName_entry.get()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
    cursor = conn.cursor()

    # Check if the email exists in the database
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user:
            # Hash the entered password
            entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Compare the hashed passwords
            if entered_password_hash == user[3]:  # Assuming the password hash is stored in column index 4
       
                file_path = 'userinfo.txt'

                # Save the JSON data to a file
                with open(file_path, 'w+') as json_file:
                    json_file.write(f"{user[0]},{user[1]},{user[2]}")                                
                destroy_login()
                os.system("python python\\home.py")
                
            else:
                invalid_password_message = "Invalid Password"
                show_custom_error("Login Failed", invalid_password_message)
    else:
        # messagebox.showerror("Login Failed", "Invalid Email")
        invalid_password_message = "Invalid Email"
        show_custom_error("Login Failed", invalid_password_message)

        # Close the connection
        conn.close()

window = None

def destroy_login():
    global window
    window.destroy()

def loginpage ():
    global window
    window = Tk()

    # window.state('zoomed')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    screen_width = window.winfo_screenwidth()
    screen_height =window.winfo_height()
    app_width = 1340
    app_height = 690
    x = (screen_width/2)-(app_width/2)
    y = (screen_height/160)-(app_height/160)
    window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")



    # ================Background Image ====================
     
    home_bgImg = Image.open('python\\assets\\loginbg.png')
    home_bgImg = home_bgImg.resize((1340, 690))

    photo = ImageTk.PhotoImage(home_bgImg)
    bg_imageLogin = Label( image=photo, )
    bg_imageLogin.image = photo
    bg_imageLogin.place(x=0, y=0)

   
   

    # ================ GO TO SIGN UP ====================
    signup_img= PhotoImage(file="python\\assets\\signupbtn.png")

    switchSignup = Button(
        bg_imageLogin,
        image=signup_img,
        text="Sign Up",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        command=lambda  : [destroy_login(),register_page.regestier()]

    )
    switchSignup.place(x=230, y=140,)
# ================ GO TO Back ====================
    signup_img2= PhotoImage(file="python\\assets\\signupbtn.png")


      
    switchSignup = Button(
        bg_imageLogin,
        image=signup_img2,
        text="Back",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        command=lambda  : [destroy_login(),Dashboard.page()]

    )
    switchSignup.place(x=350, y=140,)
    


    # ================ Email Name Section ====================
    Login_emailName_image = PhotoImage(file="python\\assets\\lable.png")
    Login_emailName_image_Label = Label(
        bg_imageLogin,
        image=Login_emailName_image,
        borderwidth=0,
        bg="#272A37"
    )
    Login_emailName_image_Label.place(x=76, y=270)


    
    global Login_emailName_entry
    Login_emailName_entry = Entry(
        Login_emailName_image_Label,
        bd=0,
       bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    Login_emailName_entry.place(x=9, y=10,width=300)


    # ================ Password Name Section ====================
    Login_passwordName_image = PhotoImage(file="python\\assets\\lable.png")
    Login_passwordName_image_Label = Label(
        bg_imageLogin,
        image=Login_passwordName_image,
      
        borderwidth=0
    )
    Login_passwordName_image_Label.place(x=80, y=380)

    global Login_passwordName_entry
    Login_passwordName_entry = Entry(
        Login_passwordName_image_Label,
        bd=0,
        bg="#245c62",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
        show="*"
    )
    Login_passwordName_entry.place(x=10, y=17, )

    # login_password_entry = tk.Entry(Login_passwordName_entry, show="*")
    # login_password_entry.pack()
    # def login():
    #         login.withdraw()
    #         os.system("python Dashboard.py")
    #         login.destroy()
    # =============== Submit Button ====================
    Login_button_image_1 = PhotoImage(
        file="python\\assets\\loginbtn.png")
    Login_button_1 = Button(
        bg_imageLogin,
        image=Login_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda:login,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        bg='#272A37',
        command=lambda:login()
        
    )
    
    Login_button_1.place(x=190, y=480)

    forgot_password_image= PhotoImage(file="python\\assets\\forgt.png")
    forgotPassword = Button(
        bg_imageLogin,
        image=forgot_password_image,
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: forgot_password(),
    )
    forgotPassword.place(x=150, y=443, )


    def forgot_password():

        win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('Forgot Password')
        # win.iconbitmap('images\\aa.ico')
        win.configure(background='#272A37')
        win.resizable(False, False)

        # ====== Email ====================
        email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                            bd=0)
        email_entry3.place(x=40, y=80, width=256, height=50)
        email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                            font=("yu gothic ui", 11, 'bold'))
        email_label3.place(x=40, y=50)

        update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#ff6c38', font=("yu gothic ui", 12, "bold"),
                            cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                            command=lambda:destroy_resset(email_entry3))
        update_pass.place(x=40, y=260, width=256, height=45)
        # window.destroy()

        def destroy_resset(email_entrey):
            reset_page.reset_password(email_entrey)
            win.destroy()


    
    


    window.mainloop()
    

if __name__ == '__main__':
    loginpage()