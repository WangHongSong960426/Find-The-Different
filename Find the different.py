from tkinter import *
def button_clicked1():
    a4.config(text="You are right!")
def button_clicked2():
    a4.config(text="You are wrong!")

window = Tk()
window.title("Find the different")
window.geometry("600x600")
a0 = Label(text="find the different one", bg="yellow")
a1 = Label(text="101010101010101010101010101010101010101010101010", bg="gray")
a2 = Label(text="101010101010101010101110101010101010101010101010", bg="red")
a3 = Label(text="101010101010101010101010101010101010101010101010", bg="green")
a4 = Label(text="")
a0.pack(side=TOP)
a1.pack(side=TOP)
a2.pack(side=TOP)
a3.pack(side=TOP)
a4.pack(side=TOP)


button1 = Button(text="It's Red", font=("Arial", 18, "bold"), padx=5, pady=5, bg="blue", fg="black", command=button_clicked1)
button1.pack()

button2 = Button(text="It's Gray", font=("Arial", 18, "bold"), padx=5, pady=5, bg="blue", fg="black", command=button_clicked2)
button2.pack()

button3 = Button(text="It's Green", font=("Arial", 18, "bold"), padx=5, pady=5, bg="blue", fg="black", command=button_clicked2)
button3.pack()

window.mainloop()