from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os 


def toggle_microphone():
    # Add your code here to handle microphone control
    # For example, you can start/stop recording audio or enable/disable voice input
    # This part depends on the specific implementation and requirements
    pass

def exit_application():
    # Add your code here to exit the application
    # This can include closing any open resources or windows
    window.destroy()

def send_message():
    message = entry.get()
    display.insert(tk.END, message + "\n", "right")
    entry.delete(0, tk.END)

# Create the main window
window = Tk()
window.title("GUZEL BOT")
window_width = 1340
window_height = 690
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#525561")
window.geometry('1340x690')

background_image = Image.open("python\\new\\Guzel (10).png")
background_image = background_image.resize((1340, 690))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0)


home_bgImg1 = Image.open('python\\new\\homentn.png')
home_bgImg1= home_bgImg1.resize((130, 46))
photo2 = ImageTk.PhotoImage(home_bgImg1)
home_bg1 = Label(window, image=photo2, bg='#272A37')
home_bg1.image = photo2
      
home_bgImg2 = Image.open('python\\new\\chatbtn.png')
home_bgImg2= home_bgImg2.resize((130, 46))
photo3 = ImageTk.PhotoImage(home_bgImg2)
home_bg2 = Label(window, image=photo3, bg='#272A37')
home_bg2.image = photo3


home_bgImg3 = Image.open('python\\new\\facid.png')
home_bgImg2= home_bgImg2.resize((90,37))
photo4 = ImageTk.PhotoImage(home_bgImg3)
home_bg3 = Label(window, image=photo4, )
home_bg3.image = photo4
      
home_bgImg4 = Image.open('python\\new\\aboutbtn.png')
home_bgImg2= home_bgImg2.resize((90,37))
photo5 = ImageTk.PhotoImage(home_bgImg4)
home_bg4 = Label(window, image=photo5, )
home_bg4.image = photo5
       
home_bgImg5 = Image.open('python\\new\\logout.png')
home_bgImg2= home_bgImg2.resize((90, 37))
photo6 = ImageTk.PhotoImage(home_bgImg5)
home_bg5 = Label(window, image=photo6, )
home_bg5.image = photo6


        
         
       
        
       

        # ========== HOME BUTTON =======
home_button = Button(
         window, 
            image=photo2, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",)
home_button.place(x=140, y=40)

def about():
            pass

def chat():
            pass

        # ========== chat BUTTON =======
chat_button = Button(
            window, 
            image=photo3,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=chat
                    )
chat_button.place(x=300, y=40)



         # ========== face  BUTTON =======
face_button = Button(window,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,command=about)
face_button.place(x=765, y=40)

        # ========== about  BUTTON =======
about_button = Button(
            window, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,         
            command=about)
about_button.place(x=460, y=40)
        
     

def Dashboard():
            window.withdraw()
            os.system("python python\\Dashboard.py")
            window.destroy()
            
        # ========== LOG OUT =======
logout_button = Button(window,  image=photo6,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" , command=Dashboard)
logout_button.place(x=1000, y=40)









display = tk.Text(window, height=20, width=63,bg='#40508a', fg="black", wrap=tk.WORD,font=("yu gothic ui SemiBold", 12))
display.place(x=640, y=110)

# Create a frame to hold the image and entry widget
enter_img1=Image.open("python\\new\\label.png")
enter_img1=enter_img1.resize((430,60))
enter_photo1=ImageTk.PhotoImage(enter_img1)
image_label1 = tk.Label(window, image=enter_photo1,bg='#40508a')
image_label1.place(x=660, y=540)

# entry_frame =tk.Frame(image_label1,bg="#A28DCF")
# entry_frame.place(x=643, y=470)

# enter_img = Image.open("python\\new\\user.png")
# enter_img = enter_img.resize((50, 50))
# enter_photo = ImageTk.PhotoImage(enter_img)

# Create an image label and entry widget within the frame
# image_label = tk.Label(entry_frame, image=enter_photo,)
# image_label.pack(side=tk.LEFT, padx=6)

entry = Entry(image_label1,width=35, font=("yu gothic ui SemiBold", 15),bg=("#6f6caa"))
entry.place(x=20, y=15)

image = Image.open("python\\new\\send.png")
image = image.resize((40, 40))
photo = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\exit.png")
image = image.resize((40, 40))
photo1 = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\mic.png")
image = image.resize((40, 40))
photo2 = ImageTk.PhotoImage(image)

# Create a send button to trigger the send_message function
send_button = tk.Button(window, image=photo, text="Send", command=send_message, height=40, width=40, bg='#40508a')
send_button.place(x=1100, y=550)

# Create a microphone button to trigger the toggle_microphone function
mic_button = tk.Button(window, image=photo2, text="Microphone", command=toggle_microphone, height=40, width=40, bg='#40508a')
mic_button.place(x=1150, y=550)

# Create an exit button to trigger the exit_application function
# exit_button = tk.Button(window, image=photo1, text="Exit", command=exit_application, height=40, width=40, bg='#424E83')
# exit_button.place(x=1050, y=550)

display.tag_configure("left", justify="left")
display.tag_configure("right", justify="right")

def receive_message(message):
    box_color = "white"
    display.insert(tk.END, message + "\n")
    display.tag_add("box", "end-2l", "end")
    display.tag_config("box", background=box_color)

    # Scroll to the end of the display
    display.see(tk.END)

# Simulate receiving a message from the bot
receive_message("Hello, how can I assist you?")

# Run the main loop
window.mainloop()