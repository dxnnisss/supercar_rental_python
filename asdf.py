import tkinter as tk
from tkinter import ttk

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartMenu, LoginRegister, Login, ViewCar, Register):
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

        label = ttk.Label(self, text="SuperCar Rental Services", font=("Verdana", 25))
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Login/Register", command=lambda: controller.show_frame(LoginRegister))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="View Cars", command=lambda: controller.show_frame(ViewCar))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Quit", command=parent.quit)
        button3.grid(row=3, column=1, padx=10, pady=10)



class ViewCar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Cars Available for Rent", font=("Verdana", 25))
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(LoginRegister))
        button1.grid(row=1, column=1, padx=10, pady=10)

    def viewcar(self):
        i = 1
        while i != 0:
            with open("cardetails.txt") as car_details:
                car_details = car_details.readlines()
                for line in car_details:
                    line = line.split("|")

                    car_name = line[1]
                    car_engine = line[2]
                    car_segment = line[3]
                    car_type = line[4]
                    car_colour = line[5]

                    print("\n--------------- CAR", i, "---------------")
                    print("Car Name\t\t: ", car_name)
                    print("Engine Capacity\t: ", car_engine)
                    print("Car Segment\t\t: ", car_segment)
                    print("Car Type\t\t: ", car_type)
                    print("Colour\t\t\t: ", car_colour)

                    print("\n\t1 View Next Record")
                    print("\t0 Return to menu\n")
                    viewcar_status = input("Please enter a response: ")

                    if viewcar_status == "1":
                        i += 1

                    else:
                        return False

                print("\n---------------No more available record---------------")
                print("\n\t1 Return to Main Menu.\n")
                miniStatus = input("Please enter a response: ")

                if miniStatus == "1":
                    print("You will be redirected to menu...\n")

                    return False

                else:
                    print("You will be redirected to menu...\n")

                    return False


class LoginRegister(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="To Login/Register", font=("Verdana", 25))
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
        button1.grid(row=1, column=2, padx=10, pady=10)

        button2 = ttk.Button(self, text="Register", command=lambda: controller.show_frame(Register))
        button2.grid(row=2, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(StartMenu))
        button3.grid(row=3, column=2, padx=10, pady=10)


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="To Login", font=("Verdana", 25))
        label.grid(row=0, column=4, padx=10, pady=10)

        # button1 = ttk.Button(self, text="Login as Member", command=lambda: controller.show_frame(-))
        # button1.grid(row=1, column=1, padx=10, pady=10)

        # button2 = ttk.Button(self, text="Login as Admin", command=lambda:controller.show_frame(-)

        button3 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(LoginRegister))
        button3.grid(row=3, column=1, padx=10, pady=10)

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="To Register", font=("Verdana", 25))
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(LoginRegister))
        button1.grid(row=1, column=1, padx=10, pady=10)


app= tkinterApp()
app.mainloop()