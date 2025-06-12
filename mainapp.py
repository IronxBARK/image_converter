"""
mainapp.py

A modern Tkinter-based GUI application for image format conversion and background removal.

Features:
- Main menu with navigation buttons
- Convert image format with file dialog and format selection
- Remove image background with file dialog
- Modular widgets and code structure
"""

import tkinter as tk
from converter import convert_image
from widgets import create_modern_button, entry_button, browse_file
from tkinter import ttk, filedialog, messagebox


# -------------------- Main Landing Page --------------------
class MainPage(tk.Frame):
    """
    The main landing page of the application.
    Shows the app title and navigation buttons for conversion and background removal.
    """

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
        """
        Set up the main UI: background, title, and navigation buttons.
        """
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.canvas.create_text(
            (self.WIDTH // 2) - 18,
            62,
            text="PLASTIC SURGERY",
            font=("Georgia", 28, "bold"),
            fill="gray",
        )
        self.canvas.create_text(
            (self.WIDTH // 2) - 20,
            60,
            text="PLASTIC SURGERY",
            font=("Georgia", 28, "bold"),
            fill="black",
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


# -------------------- Convert Format Page --------------------
class ConvertFormatPage(tk.Frame):
    """
    Page for converting image formats.
    Allows user to select an image, choose output format, and save the result.
    """

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
        self.browse_file = controller.browse_file
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the UI for format conversion: file entry, browse, format dropdown, convert/back buttons, and key bindings.
        """
        self.canvas.create_text(
            (self.WIDTH // 3),
            (self.HEIGHT // 3) + 40,
            text="Enter File Path",
            font=("Georgia", 16, "bold"),
            fill="#333",
        )
        self.image_path_var = tk.StringVar()
        self.image_path, self.browse_btn, back_button = entry_button(self)
        self.canvas.create_window(
            self.WIDTH // 3, (self.HEIGHT // 3) + 80, window=self.image_path
        )
        self.canvas.create_window(
            (self.WIDTH // 6) + 40, (self.HEIGHT // 2) + 20, window=self.browse_btn
        )
        back_button.place(x=40, y=30)
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
        self.canvas.create_window(
            self.WIDTH - 400, (self.HEIGHT // 3) + 80, window=format_dropdown
        )
        self.canvas.create_text(
            650, 280, text="➡", font=("Arial", 24, "bold"), fill="#4a90e2"
        )
        convert_btn = create_modern_button(
            self,
            "Convert",
            self.WIDTH // 2,
            (self.HEIGHT // 2) + 80,
            canvas=self.canvas,
            command=self.convert_action,
        )

    def convert_action(self):
        """
        Convert the selected image to the chosen format and save it.
        Shows error/info dialogs as needed.
        """
        path = self.image_path.get()
        target_format = self.format_var.get()
        if not path:
            messagebox.showerror("Error", "Please enter a valid file path.")
            return
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
            messagebox.showinfo("Success", "Image converted and saved successfully!")
        else:
            messagebox.showinfo("Cancelled", "Conversion cancelled.")


# -------------------- Background Remover Page --------------------
class BackgroundRemoverPage(tk.Frame):
    """
    Page for removing the background from an image.
    Allows user to select an image and save the result with background removed.
    Keyboard shortcuts:
        - Escape: Go back to main page
        - Enter: Remove background
    """

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
        self.browse_file = controller.browse_file
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the UI for background removal: file entry, browse
        """
        # Center left: Show bgrem.png
        self.bgrem_img = tk.PhotoImage(file="assets/bgrem.png")
        self.canvas.create_image(350, 280, image=self.bgrem_img, anchor=tk.CENTER)
        # Center right: Path entry with label and browse button
        self.canvas.create_text(
            870, 240, text="Enter File Path", font=("Georgia", 16, "bold"), fill="#333"
        )
        self.image_path_var = tk.StringVar()
        self.image_path, self.browse_btn, back_button = entry_button(
            self
        )  # function called
        self.canvas.create_window(850, 280, window=self.image_path)
        self.canvas.create_window(1100, 280, window=self.browse_btn)
        back_button.place(x=40, y=30)
        convert_btn = create_modern_button(
            self, "Remove", 860, 350, canvas=self.canvas, command=self.remove_bg_action
        )

    def remove_bg_action(self):
        """
        Remove the background from the selected image and save it.
        Shows error/info dialogs as needed.
        """
        path = self.image_path.get()
        if not path:
            messagebox.showerror("Error", "Please enter a valid file path.")
            return
        filetypes = [("PNG files", "*.png"), ("All files", "*.*")]
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=filetypes,
            title="Save Image With Background Removed As...",
        )
        if save_path:
            messagebox.showinfo(
                "Processing", "Removing background may take time... Please wait."
            )
            from converter import remove_background

            remove_background(path, save_path)
            messagebox.showinfo("Success", "Background removed and saved successfully!")
        else:
            messagebox.showinfo("Cancelled", "Background removal cancelled.")


# -------------------- Main Application Controller --------------------
class PlasticSurgeryApp:
    """
    The main application controller.
    Manages window, navigation, and page switching.
    """

    def __init__(self, root):
        self.root = root
        self.WIDTH, self.HEIGHT = 1200, 600
        self.root.title("PLASTIC SURGERY")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.iconbitmap("assets\\icon.ico")
        self.image = tk.PhotoImage(file="assets\\bg2.png")
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.browse_file = browse_file
        self.frames = {}
        self.init_pages()
        self.show_frame("MainPage")

    def init_pages(self):
        """
        Create and store all pages (frames) for the app.
        """
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
        """Show the requested page"""
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlasticSurgeryApp(root)
    app.run()
