import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageDraw, ImageTk

# Variable to store the hotkey
current_hotkey = "F2"  # Default hotkey

# Function to create a rounded rectangle image
def create_rounded_rectangle(width, height, radius, color):
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
    return ImageTk.PhotoImage(image)

# Function to center the window on any screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to open the hotkey popup
def open_hotkey_popup():
    hotkey_popup = Toplevel(window)
    hotkey_popup.title("Change Hotkey")
    hotkey_popup.configure(bg="#f8f8f8")
    hotkey_popup.geometry("300x150")
    center_window(hotkey_popup)

    label = tk.Label(hotkey_popup, text="Enter new hotkey:", font=("Arial", 12), fg="black", bg="#f8f8f8")
    label.pack(pady=(15, 5))

    hotkey_entry = tk.Entry(hotkey_popup, font=("Arial", 10), width=20)
    hotkey_entry.pack(pady=5)
    hotkey_entry.focus()

    def save_hotkey():
        global current_hotkey
        new_hotkey = hotkey_entry.get().upper()
        if new_hotkey:
            current_hotkey = new_hotkey
            hotkey_label.config(text=f"Current Hotkey: {current_hotkey}")
            print(f"New hotkey saved: {current_hotkey}")
        hotkey_popup.destroy()

    save_button = tk.Button(hotkey_popup, text="Save", command=save_hotkey, bg="#1230AE", fg="white", font=("Arial", 10, "bold"))
    save_button.pack(pady=(10, 5))
    close_button = tk.Button(hotkey_popup, text="Close", command=hotkey_popup.destroy, bg="#f8f8f8", fg="black", font=("Arial", 10))
    close_button.pack()

# Function to open info popup window
def open_info_popup():
    info_popup = Toplevel(window)
    info_popup.title("About AS Auto Clicker")
    info_popup.configure(bg="#f8f8f8")
    info_popup.geometry("350x250")
    center_window(info_popup)

    title = tk.Label(info_popup, text="AS Auto Clicker", font=("Arial", 16, "bold"), fg="black", bg="#f8f8f8")
    title.pack(pady=(15, 5))

    info_text = (
        "Features:\n\n"
        "- Set custom click intervals\n"
        "- Choose click types (single or double)\n"
        "- Pick mouse button (left, middle, right)\n"
        "- Random intervals support\n"
        "- Configurable hotkeys for start/stop"
    )
    info_label = tk.Label(info_popup, text=info_text, font=("Arial", 10, "bold"), fg="black", bg="#f8f8f8", justify="center")
    info_label.pack(pady=10, padx=20)

    close_button = tk.Button(info_popup, text="Close", command=info_popup.destroy, bg="#1230AE", fg="white", font=("Arial", 10, "bold"))
    close_button.pack(pady=(10, 10))

# Function to minimize the main window
def minimize_window():
    window.iconify()

# Function to close the main window
def close_window():
    window.destroy()

# Function to open record and playback popup window
def open_record_playback_popup():
    record_playback_popup = Toplevel(window)
    record_playback_popup.title("Record & Playback")
    record_playback_popup.configure(bg="#f8f8f8")
    record_playback_popup.geometry("300x200")
    center_window(record_playback_popup)

    title = tk.Label(record_playback_popup, text="Record & Playback", font=("Arial", 14, "bold"), fg="black", bg="#f8f8f8")
    title.pack(pady=(15, 10))

    def play_action():
        print("Play action triggered")
        record_playback_popup.destroy()

    def record_action():
        print("Record action triggered")
        record_playback_popup.destroy()

    def load_action():
        print("Load action triggered")
        record_playback_popup.destroy()

    play_button = tk.Button(record_playback_popup, text="Play", command=play_action, bg="#1230AE", fg="white", font=("Arial", 10, "bold"), width=15)
    play_button.pack(pady=5)
    record_button = tk.Button(record_playback_popup, text="Record", command=record_action, bg="#1230AE", fg="white", font=("Arial", 10, "bold"), width=15)
    record_button.pack(pady=5)
    load_button = tk.Button(record_playback_popup, text="Load", command=load_action, bg="#1230AE", fg="white", font=("Arial", 10, "bold"), width=15)
    load_button.pack(pady=5)

    close_button = tk.Button(record_playback_popup, text="Close", command=record_playback_popup.destroy, bg="#f8f8f8", fg="black", font=("Arial", 10))
    close_button.pack(pady=(10, 5))

# Function to make the window draggable
def start_move(event):
    window.x = event.x
    window.y = event.y

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    x = window.winfo_pointerx() - window.x
    y = window.winfo_pointery() - window.y
    window.geometry(f"+{x}+{y}")

# Create the main window with increased width
window = tk.Tk()
window.title("AS Auto Clicker")
window.configure(bg="#f8f8f8")
window.geometry("600x700")  # Increased width to ensure all elements fit
window.overrideredirect(True)  # Removes the default window decorations
center_window(window)

# Bind mouse events for dragging
window.bind("<Button-1>", start_move)
window.bind("<ButtonRelease-1>", stop_move)
window.bind("<B1-Motion>", do_move)

# Load and resize images (replace with paths)
icon_image = Image.open("logoauto-removebg-preview.png").resize((50, 50), Image.LANCZOS)
icon_photo = ImageTk.PhotoImage(icon_image)
sun_icon_image = Image.open("sun (1).png").resize((25, 25), Image.LANCZOS)
sun_icon_photo = ImageTk.PhotoImage(sun_icon_image)
minimize_icon_image = Image.open("icons8-minimize-48 (1).png").resize((25, 25), Image.LANCZOS)
minimize_icon_photo = ImageTk.PhotoImage(minimize_icon_image)
close_icon_image = Image.open("icons8-x-50.png").resize((22, 22), Image.LANCZOS)
close_icon_photo = ImageTk.PhotoImage(close_icon_image)

# Header section
header_frame = tk.Frame(window, bg="#f8f8f8")
header_frame.pack(pady=5, fill=tk.X, padx=5)
icon_label = tk.Label(header_frame, image=icon_photo, bg="#f8f8f8")
icon_label.pack(side=tk.LEFT, padx=(2, 2))
header_label = tk.Label(header_frame, text="AS Auto Clicker", fg="#1230AE", bg="#f8f8f8", font=("Arial", 18, "bold"))
header_label.pack(side=tk.LEFT, padx=(2, 5))

# Right icons
close_icons_frame = tk.Frame(header_frame, bg="#f8f8f8")
close_icons_frame.pack(side=tk.RIGHT)
info_label = tk.Label(close_icons_frame, text="ℹ", fg="#1230AE", bg="#f8f8f8", font=("Arial", 16))
info_label.pack(side=tk.LEFT, padx=5)
info_label.bind("<Button-1>", lambda e: open_info_popup())
theme_label = tk.Label(close_icons_frame, image=sun_icon_photo, bg="#f8f8f8")
theme_label.pack(side=tk.LEFT, padx=5)
minimize_label = tk.Label(close_icons_frame, image=minimize_icon_photo, bg="#f8f8f8")
minimize_label.pack(side=tk.LEFT, padx=5)
minimize_label.bind("<Button-1>", lambda e: minimize_window())
close_label = tk.Label(close_icons_frame, image=close_icon_photo, bg="#f8f8f8")
close_label.pack(side=tk.LEFT, padx=5)
close_label.bind("<Button-1>", lambda e: close_window())

# Function to create labeled frames with a precise blue border
def create_label_frame(window, title):
    outer_frame = tk.Frame(window, bg="#1230AE", padx=1, pady=1)  # Reduced padding for better fit
    outer_frame.pack(pady=10, fill=tk.X, padx=20)
    label_frame = tk.LabelFrame(outer_frame, text=title, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold"), padx=10, pady=10)
    label_frame.pack(fill=tk.BOTH, expand=True)  # Expand to fit exactly within the border
    return label_frame

# Click Interval section
interval_frame = create_label_frame(window, "Click Interval")

# Set Time section
set_time_label = tk.Label(interval_frame, text="Set Time (Hours:Min:Sec:Ms)", fg="black", bg="#f8f8f8", font=("Arial", 10, "bold"))
set_time_label.grid(row=0, column=0, columnspan=4, pady=2)

tk.Label(interval_frame, text="Hrs", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=0, padx=5)
tk.Label(interval_frame, text="Min", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=1, padx=5)
tk.Label(interval_frame, text="Sec", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=2, padx=5)
tk.Label(interval_frame, text="Ms", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=3, padx=5)

hours = tk.Spinbox(interval_frame, from_=0, to=23, width=5, fg="#1230AE")
minutes = tk.Spinbox(interval_frame, from_=0, to=59, width=5, fg="#1230AE")
seconds = tk.Spinbox(interval_frame, from_=0, to=59, width=5, fg="#1230AE")
milliseconds = tk.Spinbox(interval_frame, from_=0, to=990, increment=10, width=5, fg="#1230AE")

hours.grid(row=2, column=0, padx=5)
minutes.grid(row=2, column=1, padx=5)
seconds.grid(row=2, column=2, padx=5)
milliseconds.grid(row=2, column=3, padx=5)

# Random Interval section
rand_interval_label = tk.Label(interval_frame, text="Random Interval (Sec:Ms)", fg="black", bg="#f8f8f8", font=("Arial", 10, "bold"))
rand_interval_label.grid(row=0, column=5, columnspan=2, pady=2)

tk.Label(interval_frame, text="Sec", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=5, padx=5)
tk.Label(interval_frame, text="Ms", fg="black", bg="#f8f8f8", font=("Arial", 9)).grid(row=1, column=6, padx=5)

rand_seconds = tk.Spinbox(interval_frame, from_=0, to=59, width=5, fg="#1230AE")
rand_milliseconds = tk.Spinbox(interval_frame, from_=0, to=990, increment=10, width=5, fg="#1230AE")

rand_seconds.grid(row=2, column=5, padx=5)
rand_milliseconds.grid(row=2, column=6, padx=5)

# Click Options section with increased font size and boldness
options_frame = create_label_frame(window, "Click Options")

# Mouse Buttons column
mouse_buttons_frame = tk.Frame(options_frame, bg="#f8f8f8")
mouse_buttons_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
tk.Label(mouse_buttons_frame, text="Mouse Buttons", fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(mouse_buttons_frame, text="Left", value=1, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(mouse_buttons_frame, text="Middle", value=2, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(mouse_buttons_frame, text="Right", value=3, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")

# Click Type column
click_type_frame = tk.Frame(options_frame, bg="#f8f8f8")
click_type_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nw")
tk.Label(click_type_frame, text="Click Type", fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(click_type_frame, text="Single Click", value=1, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(click_type_frame, text="Double Click", value=2, fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold")).pack(anchor="w")

# Click Repeat section
repeat_frame = create_label_frame(window, "Click Repeat")
tk.Radiobutton(repeat_frame, text="Repeat", value=1, fg="#1230AE", bg="#f8f8f8", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
repeat_spinbox = tk.Spinbox(repeat_frame, from_=1, to=100, width=5, fg="#1230AE", font=("Arial", 10, "bold"))
repeat_spinbox.grid(row=0, column=1, padx=5)
tk.Radiobutton(repeat_frame, text="Until Stopped", value=2, fg="#1230AE", bg="#f8f8f8", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w")

# Cursor Position section
cursor_container = tk.Frame(window, bg="#f8f8f8")
cursor_container.pack(fill=tk.X, padx=20, pady=10)
cursor_outer_frame = tk.Frame(cursor_container, bg="#1230AE", padx=1, pady=1)
cursor_outer_frame.pack(side=tk.LEFT, fill=tk.BOTH)
cursor_frame = tk.LabelFrame(cursor_outer_frame, text="Cursor Position", fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold"), padx=10, pady=10)
cursor_frame.pack(fill=tk.BOTH)
cursor_options_frame = tk.Frame(cursor_frame, bg="#f8f8f8")
cursor_options_frame.pack(anchor="w")
tk.Radiobutton(cursor_options_frame, text="Use Current Location", value=1, fg="#1230AE", bg="#f8f8f8", font=("Arial", 10, "bold")).pack(anchor="w")
pick_location_frame = tk.Frame(cursor_options_frame, bg="#f8f8f8")
pick_location_frame.pack(anchor="w")
tk.Radiobutton(pick_location_frame, text="Pick a Location", value=2, fg="#1230AE", bg="#f8f8f8", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
pick_button = tk.Button(pick_location_frame, text="Pick", fg="#1230AE", font=("Arial", 10, "bold"))
pick_button.pack(side=tk.LEFT, padx=5)

# Hotkey display
hotkey_label = tk.Label(window, text=f"Current Hotkey: {current_hotkey}", fg="#1230AE", bg="#f8f8f8", font=("Arial", 12, "bold"))
hotkey_label.pack(pady=(10, 0))

# Four main action buttons in a 2x2 grid layout
buttons_frame = tk.Frame(cursor_container, bg="#f8f8f8")
buttons_frame.pack(side=tk.RIGHT, padx=(20, 0), fill=tk.Y, pady=2)
rounded_start = create_rounded_rectangle(130, 35, 15, "#1230AE")
rounded_stop = create_rounded_rectangle(130, 35, 15, "#1230AE")
rounded_hotkey = create_rounded_rectangle(130, 35, 15, "#1230AE")
rounded_playback = create_rounded_rectangle(130, 35, 15, "#1230AE")

# Buttons with new arrangement
change_hotkey_button = tk.Button(buttons_frame, text="Change HOTKEY", image=rounded_hotkey, compound="center", fg="white", font=("Arial", 10, "bold"), borderwidth=0, command=open_hotkey_popup)
start_button = tk.Button(buttons_frame, text="START", image=rounded_start, compound="center", fg="white", font=("Arial", 10, "bold"), borderwidth=0)
stop_button = tk.Button(buttons_frame, text="STOP", image=rounded_stop, compound="center", fg="white", font=("Arial", 10, "bold"), borderwidth=0)
playback_button = tk.Button(buttons_frame, text="Record & Playback", image=rounded_playback, compound="center", fg="white", font=("Arial", 10, "bold"), borderwidth=0, command=open_record_playback_popup)

# Arrange buttons in a 2x2 grid layout
change_hotkey_button.grid(row=0, column=0, padx=10, pady=5)
start_button.grid(row=0, column=1, padx=10, pady=5)
stop_button.grid(row=1, column=0, padx=10, pady=5)
playback_button.grid(row=1, column=1, padx=10, pady=5)

# Run the Tkinter event loop
window.mainloop()
