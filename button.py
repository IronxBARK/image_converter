import tkinter as tk


def on_enter(e):
    e.widget.configure(bg="#3a3f5a", relief="sunken")

def on_leave(e):
    e.widget.configure(bg="#2B3044", relief="flat")

# --- BUTTON STYLE FUNCTION ---
def create_modern_button(master, text, x , y, canvas, command=None):
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
        pady=12
    )
    btn_window = canvas.create_window(x, y, window=btn)

    # Simulate hover effects
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    if command:
        btn.config(command=command)

    return btn