import customtkinter as ctk

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

app = ctk.CTk(fg_color="blue")
app.geometry("300x200")

try:
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x00FF0000

    windll.dwmapi.DwmSetWindowAttribute(
        HWND, 
        20, 
        byref(c_int(title_bar_color)), 
        sizeof(c_int))

except:
    pass

app.mainloop()