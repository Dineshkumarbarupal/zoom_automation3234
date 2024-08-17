import customtkinter as ctk
import subprocess
import pyautogui
import time

# GUI theme and color theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Zoom Meeting")

def join_zoom_meeting():
    meeting_id = meeting_id_entry.get()
    password = password_entry.get()
    participants = int(participant_entry.get())

    meeting_info = {
        'meeting_id': meeting_id,
        'password': password
    }

    open_zoom_meeting(meeting_info, participants)

def open_zoom_meeting(meeting_info, participants):
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    user_data_dir = r'C:\Users\AdiiSunlay\AppData\Local\Google\Chrome\User Data'

    for i in range(1, participants + 1):
        profile_dir = f"Profile {i}"
        meeting_url = f"https://us02web.zoom.us/wc/{meeting_info['meeting_id']}/join?pwd={meeting_info['password']}"

        try:
            # Launch Chrome with the specified profile and Zoom meeting URL
            subprocess.Popen([chrome_path,
                              f'--user-data-dir={user_data_dir}',
                              f'--profile-directory={profile_dir}',
                              meeting_url])
            time.sleep(31)  # Increased wait time for the Zoom page to load completely

            # Define coordinates for the name input box (replace with accurate coordinates)
            name_input_x, name_input_y = 1351, 592  # Replace with actual coordinates from your screen

            # Click on the name input box
            pyautogui.click(x=name_input_x, y=name_input_y)

            # Type a space character
            pyautogui.write(' ')

        except FileNotFoundError:
            print(f"Error: Chrome executable not found at {chrome_path}.")
            return

# def on_entry_change(*args):
#     if meeting_id_entry.get() and password_entry.get() and participant_entry.get():
#         join_button.invoke()  # Automatically clicks the button when all fields are filled

label = ctk.CTkLabel(app, text="This is a page for joining a Zoom meeting")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Join a Zoom Meeting')
label.pack(pady=12, padx=10)

meeting_id_entry = ctk.CTkEntry(master=frame, placeholder_text="Meeting ID")
meeting_id_entry.pack(pady=12, padx=10)
#meeting_id_entry.bind("<KeyRelease>", on_entry_change)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entry.pack(pady=12, padx=10)
#password_entry.bind("<KeyRelease>", on_entry_change)

participant_entry = ctk.CTkEntry(master=frame, placeholder_text="Number of Participants")
participant_entry.pack(pady=12, padx=10)
#participant_entry.bind("<KeyRelease>", on_entry_change)

join_button = ctk.CTkButton(master=frame, text='Join Meeting', command=join_zoom_meeting)
join_button.pack(pady=12, padx=10)

app.mainloop()
