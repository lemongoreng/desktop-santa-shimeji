import tkinter as tk
from santa import DesktopSanta

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopSanta(root)
    root.mainloop()