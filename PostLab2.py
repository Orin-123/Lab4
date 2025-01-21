import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title("File Dialog Example")
root.geometry("300x200")

# Function to open a file dialog and get the file name
def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        label.config(text=f"Selected File: {file_path}")
    else:
        label.config(text="No file selected")

# Add a button to trigger the file dialog
button = tk.Button(root, text="Open File", command=open_file)
button.pack(pady=20)

# Add a label to display the selected file
label = tk.Label(root, text="No file selected")
label.pack()

# Run the application
root.mainloop()
