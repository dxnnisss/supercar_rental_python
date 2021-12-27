import tkinter as tk
from tkinter import ttk

largefont = ("Verdana", 30)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartMenu, LoginRegister):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Super Car Rental Services", font=largefont)
        label.grid(row=0, column=7, padx=10, pady=10)

        button1 = ttk.Button(self, text="Login/Register", command=lambda: controller.show_frame(LoginRegister))
        button1.grid(row=2, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Quit", command=parent.quit)
        button2.grid(row=3, column=1, padx=10, pady=10)


class LoginRegister(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="StartPage", font=largefont)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Register", command=lambda: controller(Login))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(StartMenu))
        button3.grid(row=4, column=1, padx=10, pady=10)




class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page 2', font=largefont)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Login as Member", command=lambda: controller.show_frame(LoginRegister))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Login as Admin", command=lambda: controller.show_frame(Admin))
        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(LoginRegister))
        button3.grid(row=1, column=1, padx=10, pady=10)


class Admin(tk.Frame):
    pass

app = tkinterApp()
app.title("Super Car Rental Services")
app.geometry("700x720")
app.mainloop()

