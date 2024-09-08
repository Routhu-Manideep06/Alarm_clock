from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from time import sleep
from PIL import ImageTk, Image
from pygame import mixer

# Colors
bg_color = '#ffffff'  # white
colr1 = '#566fc6'  # Blue color
colr2 = '#000000'  # Black color

# Initialize the mixer
mixer.init()

# Window setup
window = Tk()
window.title("Levu bro Levu....")
window.geometry('350x200')
window.resizable(False, False)
window.configure(bg=bg_color)

# Frames
frame_line = Frame(window, width=400, height=5, bg=colr1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=300, bg=bg_color)
frame_body.grid(row=1, column=0)

# Configuring the body
img = Image.open('alarm_pic.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_img = Label(frame_body, height=100, image=img, bg=bg_color)
app_img.place(x=10, y=30)

name = Label(frame_body, text='Alarm', height=1, font="Ivy 18 bold", bg=bg_color)
name.place(x=125, y=30)

# Hour combobox
hour = Label(frame_body, text='Hour', font='Ivy 10 bold ', bg=bg_color, fg=colr1)
hour.place(x=125, y=60)
c_hour = Combobox(frame_body, font='arial 15', width=2, state="readonly")
c_hour['values'] = [f"{i:02}" for i in range(24)]
c_hour.current(0)
c_hour.place(x=125, y=80)

# Minute combobox
minute = Label(frame_body, text='Minute', font='Ivy 10 bold', bg=bg_color, fg=colr1)
minute.place(x=175, y=60)
c_min = Combobox(frame_body, font='arial 15', width=2, state="readonly")
c_min['values'] = [f"{i:02}" for i in range(60)]
c_min.current(0)
c_min.place(x=175, y=80)

# Second combobox
sec = Label(frame_body, text='Second', font='Ivy 10 bold', bg=bg_color, fg=colr1)
sec.place(x=225, y=60)
c_sec = Combobox(frame_body, width=2, font='arial 15', state="readonly")
c_sec['values'] = [f"{i:02}" for i in range(60)]
c_sec.current(0)
c_sec.place(x=225, y=80)

# Activate Alarm function
def activate_alarm():
    check_alarm()

# Deactivate Alarm function
def deactivate_alarm():
    print("Deactivated alarm", selected.get())
    mixer.music.stop()
    selected.set(0)

# Radiobutton for activating the alarm
selected = IntVar()
rad1 = Radiobutton(frame_body, font='arial 10 bold', value=1, text='Activate', bg=bg_color,
                   command=activate_alarm, variable=selected)
rad1.place(x=125, y=120)

# Radiobutton for deactivating the alarm
rad2 = Radiobutton(frame_body, text='Deactivate', value=2, font="arial 10 bold", bg=bg_color,
                   command=deactivate_alarm, variable=selected)
rad2.place(x=225, y=120)

# Sound Alarm function
def sound_alarm():
    mixer.music.load('alarm_song.mp3')
    mixer.music.play()

# Check Alarm function using after() method
def check_alarm():
    control = selected.get()
    alarm_hour = c_hour.get()
    alarm_min = c_min.get()
    alarm_sec = c_sec.get()

    # Getting the current time in 24-hour format
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")

    if control == 1:
        if alarm_hour == current_hour and alarm_min == current_minute and alarm_sec == current_second:
            print("Time to wake up!")
            sound_alarm()
            selected.set(0)  # Reset the activation state

    # Re-check every 1000 milliseconds (1 second)
    window.after(1000, check_alarm)

# Main loop
window.mainloop()
