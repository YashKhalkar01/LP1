from tkinter import *
from tkinter import messagebox
a = ""
b = ""
c = ""
gen = ""
g = 0
window = Tk()
window.title("Login Page")
window.geometry("350x300+10+20")
def show_msg():
    messagebox.showinfo("Thank You!")
    a = txtfld1.get()
    b = txtfld2.get()
    c = txtfld3.get()
    gender = "Male" if v0.get() == 1 else "Female" if v0.get() == 2 else "Not Selected"
    if a == "" or b == "" or c == "" or gender == "Not Selected":
        messagebox.showerror("Error", "Please fill in all fields and select a gender.")
        return
    print(f"Name: {a}")
    print(f"Email: {b}")
    print(f"Mob No: {c}")
    print(f"Gender: {gender}")
    txtfld1.delete(0, END)
    txtfld2.delete(0, END)
    txtfld3.delete(0, END)
    v0.set(0)
lbl1=Label(window, text="Name:", fg='red', font=("Helvetica", 16))
lbl1.place(x=60, y=50)
txtfld1=Entry(window, text="Enter Name", bd=5)
txtfld1.place(x=130, y=50)
lbl2=Label(window, text="Email:", fg='red', font=("Helvetica", 16))
lbl2.place(x=60, y=100)
txtfld2=Entry(window, text="Enter email", bd=5)
txtfld2.place(x=130, y=100)
lbl3=Label(window, text="Mob:", fg='red', font=("Helvetica", 16))
lbl3.place(x=60, y=150)
txtfld3=Entry(window, text="Enter mobile no", bd=5)
txtfld3.place(x=130, y=150)
lbl4=Label(window, text="Gender:", fg='red', font=("Helvetica", 16))
lbl4.place(x=60, y=200)
v0=IntVar()
v0.set(0)
r1=Radiobutton(window, text="Male", variable=v0,value=1)
r2=Radiobutton(window, text="Female", variable=v0,value=2)
r1.place(x=130,y=200)
r2.place(x=190, y=200)
submitbutton = Button(window, text = "Submit", command=show_msg , fg = "black")  
submitbutton.place(x=130, y = 250)
window.mainloop()