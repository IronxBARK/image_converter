import tkinter as tk
from tkinter import filedialog


def on_enter(e):
    e.widget.configure(bg="#3a3f5a", relief="sunken")


def on_leave(e):
    e.widget.configure(bg="#2B3044", relief="flat")


# --- BUTTON STYLE FUNCTION ---
def create_modern_button(master, text, x, y, canvas, command=None):
    btn = tk.Button(
        master,
        text=text,
        font=("Helvetica", 16, "bold"),
        fg="#ff7576",
        bg="#2B3044",
        activebackground="#3a3f5a",
        activeforeground="#ff7576",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=24,
        pady=12,
    )
    btn_window = canvas.create_window(x, y, window=btn)

    # Simulate hover effects
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    if command:
        btn.config(command=command)

    return btn


# path image creator
def entry_button(self):
    """( Entry path , browse button , back button ) is same for both pages. DRY"""
    return (
        tk.Entry(
            self,
            textvariable=self.image_path_var,
            font=("Arial", 16, "bold"),
            width=32,
            bd=2,
            relief="groove",
            fg="#333",
            bg="#f0f4f8",
            insertbackground="#333",
            highlightthickness=2,
            highlightcolor="#4a90e2",
        ),
        tk.Button(
            self,
            text="Browse",
            font=("Arial", 12),
            command=lambda: self.browse_file(self),
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        ),
        tk.Button(
            self,
            text="Back",
            command=lambda: self.controller.show_frame("MainPage"),
            font=("Arial", 14, "bold"),
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        ),
    )


def browse_file(self):
    '''Open a file dialog to select an image file and set the path in the entry widget.'''
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.tiff;*.gif;*.ico"),
            ("All Files", "*.*"),
        ],
        title="Select Image File",
    )
    if file_path:
        self.image_path_var.set(file_path)
