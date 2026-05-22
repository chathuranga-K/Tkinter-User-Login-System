# User Login Page - tkinter

# import all packages from tkinter module
from tkinter import*

# ---------- functions ----------

# delete last character of username
def backspace_function():
    username.delete(len(username.get())-1, "end")

# check user login validation
def login_function():
    user_password = password.get() # initialize variables
    if username.get() != "@username" :
        message:str="Login successful"
        login_label.configure(text=message)
        login_label.grid(row=4, column=0)
    else:
        message:str="Login failed!"
        login_label.configure(text=message)
        login_label.grid(row=4, column=0)

# ---------------- Tkinter GUI Window ----------------
window = Tk()
window.title("User Login") # window Title
window.geometry("550x260") # window size dimensions

# organize grid column for better arrangements
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=0)
window.grid_columnconfigure(3, weight=0)
window.grid_columnconfigure(4, weight=0)
window.grid_anchor("center")

# Label - username
Label_username = Label(
    window,
    text="Username",
    font=("Arial", 12),
    foreground="Black",
)
Label_username.grid(row=0, column=0)

# Entry - Username
username = Entry(
    window,
    width=22,
    font=("Arial", 18),
    background="light gray",
    foreground="black",
)
username.grid(row=0,column=1 ,columnspan=3 , pady=20)

# Label - Password
Label_password = Label(
    window,
    text="Password",
    font=("Arial", 12),
    foreground="Black",
)
Label_password.grid(row=1, column=0)

# Entry - Password
password = Entry(
    window,
    width=22,
    font=("Arial", 18),
    background="light gray",
    foreground="black",
    show="*", # hide user input visibility
)
password.grid(row=1,column=1 ,columnspan=3 , pady=20)

# Label - login notification
login_label = Label(
    text='',
    font=("Arial", 12),
    foreground="red"
)

# Button - Login
login_button = Button(
    window,
    width=10,
    text="Login",
    font=('Arial', 12),
    command=login_function
)
login_button.grid(row=3, column=0)

window.mainloop() # output