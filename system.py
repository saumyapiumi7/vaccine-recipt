import tkinter as tk
from tkinter import ttk

def save_details():
    name = name_entry.get()
    age = age_entry.get()
    vaccine_type = vaccine_type_entry.get()
    date = date_entry.get()
    
    # Display the saved details
    info_label.config(text=f"Name: {name}\nAge: {age}\nVaccine Type: {vaccine_type}\nDate of Vaccination: {date}")

    # Clear the entry fields after saving
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    vaccine_type_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Person's Vaccine Management Receipt")
root.geometry("400x450")
root.configure(background="black")

# Load the wallpaper image
wallpaper = tk.PhotoImage(file="wallpaper.jpg")

# Create a Label widget to display the image
background_label = tk.Label(root, image=wallpaper)
background_label.place(relwidth=1, relheight=1)

# Create frame
frame = ttk.Frame(root, style="Custom.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# App Name Label
app_name_label = tk.Label(frame, text="Person's Vaccine Receipt", font=("Times New Roman", 14, "bold", "underline"), foreground="black", background="white")
app_name_label.grid(row=0, column=0, columnspan=2, pady=10)

# Line Separator
ttk.Separator(frame, orient=tk.HORIZONTAL).grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

# Label and Entry for Name
name_label = ttk.Label(frame, text="Name:", font=("Times New Roman", 12), foreground="black", background="white")
name_label.grid(row=2, column=0, padx=5, pady=5)
name_entry = ttk.Entry(frame, font=("Times New Roman", 12), foreground="black", width=20)
name_entry.grid(row=2, column=1, padx=5, pady=5)

# Label and Entry for Age
age_label = ttk.Label(frame, text="Age:", font=("Times New Roman", 12), foreground="black", background="white")
age_label.grid(row=3, column=0, padx=5, pady=5)
age_entry = ttk.Entry(frame, font=("Times New Roman", 12), foreground="black", width=20)
age_entry.grid(row=3, column=1, padx=5, pady=5)

# Label and Entry for Vaccine Type
vaccine_type_label = ttk.Label(frame, text="Vaccine Type:", font=("Times New Roman", 12), foreground="black", background="white")
vaccine_type_label.grid(row=4, column=0, padx=5, pady=5)
vaccine_type_entry = ttk.Entry(frame, font=("Times New Roman", 12), foreground="black", width=20)
vaccine_type_entry.grid(row=4, column=1, padx=5, pady=5)

# Label and Entry for Date of Vaccination
date_label = ttk.Label(frame, text="Date of Vaccination:", font=("Times New Roman", 12), foreground="black", background="white")
date_label.grid(row=5, column=0, padx=5, pady=5)
date_entry = ttk.Entry(frame, font=("Times New Roman", 12), foreground="black", width=20)
date_entry.grid(row=5, column=1, padx=5, pady=5)

# Save Button
style = ttk.Style()
style.configure("TButton", background="black", foreground="black")

save_button = ttk.Button(frame, text="Save", command=save_details, style="TButton")
save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Line Separator
ttk.Separator(frame, orient=tk.HORIZONTAL).grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)

# Information Label
info_label = ttk.Label(frame, text="", font=("Times New Roman", 12), foreground="white", background="gray")
info_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

root.mainloop()
