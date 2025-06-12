import tkinter as tk
from converter import convert_image
from button import create_modern_button
from tkinter import ttk
from tkinter import filedialog


# Main landing page
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.WIDTH = controller.WIDTH
        self.HEIGHT = controller.HEIGHT
        self.image = tk.PhotoImage(file="assets/bg.png")
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.setup_ui()

    def setup_ui(self):
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.canvas.create_text(
            582, 62, text="PLASTIC SURGERY", font=("Georgia", 28, "bold"), fill="gray"
        )
        self.canvas.create_text(
            580, 60, text="PLASTIC SURGERY", font=("Georgia", 28, "bold"), fill="black"
        )
        create_modern_button(
            self,
            "Convert Format",
            self.WIDTH // 2,
            self.HEIGHT // 2 - 40,
            canvas=self.canvas,
            command=lambda: self.controller.show_frame("ConvertFormatPage"),
        )
        create_modern_button(
            self,
            "Remove Background",
            self.WIDTH // 2,
            self.HEIGHT // 2 + 40,
            canvas=self.canvas,
            command=lambda: self.controller.show_frame("BackgroundRemoverPage"),
        )


# Convert Format Page
class ConvertFormatPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.WIDTH = controller.WIDTH
        self.HEIGHT = controller.HEIGHT
        self.image = controller.image
        self.canvas = tk.Canvas(
            self, width=self.WIDTH, height=self.HEIGHT, highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.setup_ui()

    def setup_ui(self):
        self.canvas.create_text(
            400, 240, text="Enter File Path", font=("Georgia", 16, "bold"), fill="#333"
        )
        self.image_path_var = tk.StringVar()
        self.image_path = tk.Entry(
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
        )
        self.canvas.create_window(400, 280, window=self.image_path)
        browse_btn = tk.Button(
            self,
            text="Browse",
            font=("Arial", 12),
            command=self.browse_file,
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        )
        self.canvas.create_window(240, 320, window=browse_btn)
        self.format_var = tk.StringVar(value="PNG")
        formats = ["JPEG", "PNG", "WEBP", "BMP", "TIFF", "GIF", "ICO"]
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.TMenubutton",
            font=("Arial", 14, "bold"),
            background="#e0e7ef",
            foreground="#333",
            borderwidth=2,
            relief="groove",
        )
        format_dropdown = ttk.OptionMenu(self, self.format_var, formats[0], *formats)
        format_dropdown.config(style="Custom.TMenubutton")
        format_dropdown["menu"].config(font=("Arial", 12), bg="#f0f4f8", fg="#333")
        self.canvas.create_window(800, 280, window=format_dropdown)
        self.canvas.create_text(
            650, 280, text="➡", font=("Arial", 24, "bold"), fill="#4a90e2"
        )
        create_modern_button(
            self, "Convert", self.WIDTH // 2, 380, canvas=self.canvas, command=self.convert_action
        )
        # Back button to return to main page
        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.controller.show_frame("MainPage"),
            font=("Arial", 14, "bold"),
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        )
        back_button.place(x=40, y=30)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.tiff;*.gif;*.ico"),
                ("All Files", "*.*"),
            ],
            title="Select Image File",
        )
        if file_path:
            self.image_path_var.set(file_path)

    def convert_action(self):
        path = self.image_path.get()
        target_format = self.format_var.get()
        # Ask user where to save the converted file
        filetypes = [
            (f"{target_format} files", f"*.{target_format.lower()}"),
            ("All files", "*.*"),
        ]
        save_path = filedialog.asksaveasfilename(
            defaultextension=f".{target_format.lower()}",
            filetypes=filetypes,
            title="Save Converted Image As...",
        )
        if save_path:
            convert_image(path, target_format, save_path)
        else:
            print("Save cancelled.")


# Background Remover Page
class BackgroundRemoverPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.WIDTH = controller.WIDTH
        self.HEIGHT = controller.HEIGHT
        self.image = controller.image
        self.canvas = tk.Canvas(
            self, width=self.WIDTH, height=self.HEIGHT, highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.setup_ui()

    def setup_ui(self):
        # Center left: Show bgrem.png
        self.bgrem_img = tk.PhotoImage(file="assets/bgrem.png")
        self.canvas.create_image(350, 280, image=self.bgrem_img, anchor=tk.CENTER)
        # Center right: Path entry with label and browse button
        self.canvas.create_text(
            870, 240, text="Enter File Path", font=("Georgia", 16, "bold"), fill="#333"
        )
        self.image_path_var = tk.StringVar()
        self.image_path = tk.Entry(
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
        )
        self.canvas.create_window(850, 280, window=self.image_path)
        browse_btn = tk.Button(
            self,
            text="Browse",
            font=("Arial", 12),
            command=self.browse_file,
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        )
        self.canvas.create_window(1100, 280, window=browse_btn)
        # Convert button below
        create_modern_button(
            self, "Remove", 860, 350, canvas=self.canvas, command=self.remove_bg_action
        )
        # Back button (same as ConvertFormatPage)
        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.controller.show_frame("MainPage"),
            font=("Arial", 14, "bold"),
            bg="#e0e7ef",
            fg="#333",
            bd=2,
            relief="groove",
        )
        back_button.place(x=40, y=30)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.tiff;*.gif;*.ico"),
                ("All Files", "*.*"),
            ],
            title="Select Image File",
        )
        if file_path:
            self.image_path_var.set(file_path)

    def remove_bg_action(self):
        path = self.image_path.get()
        # Ask user where to save the output file
        filetypes = [("PNG files", "*.png"), ("All files", "*.*")]
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=filetypes,
            title="Save Image With Background Removed As...",
        )
        if save_path:
            # You should implement/remove_background in converter.py
            from converter import remove_background

            remove_background(path, save_path)
        else:
            print("Save cancelled.")


# main app.py
class PlasticSurgeryApp:
    def __init__(self, root):
        self.root = root
        self.WIDTH, self.HEIGHT = 1200, 600
        self.root.title("PLASTIC SURGERY")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.iconbitmap("assets\\icon.ico")
        self.image = tk.PhotoImage(file="assets\\bg2.png")
        # Create a container frame to hold all pages
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        # Dictionary to hold page frames
        self.frames = {}
        self.init_pages()
        self.show_frame("MainPage")

    def init_pages(self):
        # Create and store all pages
        self.frames["MainPage"] = MainPage(parent=self.container, controller=self)
        self.frames["ConvertFormatPage"] = ConvertFormatPage(
            parent=self.container, controller=self
        )
        self.frames["BackgroundRemoverPage"] = BackgroundRemoverPage(
            parent=self.container, controller=self
        )
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        # Bring the selected page to the front
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlasticSurgeryApp(root)
    app.run()
