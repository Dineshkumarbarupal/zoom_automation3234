import customtkinter as ctk
from tkinter import messagebox as tkmb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
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
    # Path to Chrome profile directory
    profile_directory = r"C:\Users\pc\AppData\Local\Google\Chrome\User Data\Profile"

    # List to store Chrome WebDriver instances
    chrome_drivers = []

    # Loop through each participant and create a Chrome WebDriver instance
    for i in range(1, participants + 1):
        profile_dir = f"{profile_directory} {i}"
        # Create ChromeOptions with specified profile directory
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={profile_dir}")

        # Create Chrome WebDriver with ChromeOptions
        chrome_driver = webdriver.Chrome(options=chrome_options)
        chrome_drivers.append(chrome_driver)
        time.sleep(1)  # Add a delay to ensure profiles are loaded properly

    # Example: Open the Zoom meeting URL with meeting ID and password
    for driver in chrome_drivers:
        meeting_url = f"https://us02web.zoom.us/wc/{meeting_info['meeting_id']}/join?pwd={meeting_info['password']}"
        driver.get(meeting_url)
        driver.maximize_window()
        time.sleep(1)  # Adjust the delay as needed

        # Wait for the name field and fill it with your name using Selenium's send_keys method
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-for-name"]'))).send_keys('dinesh')
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="preview-audio-control-button"]'))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="preview-video-control-button"]'))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/button'))).click()
            time.sleep(5)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Close the profiles after 360 seconds (6 minutes)
    time.sleep(3600)
    for driver in chrome_drivers:
        driver.quit()  # Quit the WebDriver

label = ctk.CTkLabel(app, text="This is a page for joining a Zoom meeting")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Join a Zoom Meeting')
label.pack(pady=12, padx=10)

meeting_id_entry = ctk.CTkEntry(master=frame, placeholder_text="Meeting ID")
meeting_id_entry.pack(pady=12, padx=10)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entry.pack(pady=12, padx=10)

participant_entry = ctk.CTkEntry(master=frame, placeholder_text="Number of Participants")
participant_entry.pack(pady=12, padx=10)

join_button = ctk.CTkButton(master=frame, text='Join Meeting', command=join_zoom_meeting)
join_button.pack(pady=12, padx=10)

app.mainloop()
