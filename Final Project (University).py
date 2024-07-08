import json
import tkinter as Tk
islogin=False


def submit():
    user = input_new_user.get()
    passw = input_new_passw.get()

    with open("info.json") as f:
        users_dct = json.load(f)
    if (user in users_dct):
        output_sub.configure(text="Username exists, already!!", fg="red")
    elif (len(passw) < 5 or passw.isalpha()):
        output_sub.configure(text="Please correct password", fg="red")
    else:
        users_dct[user] = passw
        with open("info.json", "w") as f:
            json.dump(users_dct, f)
        output_sub.configure(text="Submit done!", fg="green")



def login():
    global islogin
    user = input_user.get()
    passw = input_passw.get()
    if (islogin):
        output.configure(text="You're logged in, already!", fg="red")
        return
    else:
        with open("info.json") as f:
            users_dct = json.load(f)
        if (user in users_dct and users_dct[user] == passw):
            output.configure(text="Welcome to your account!", fg="green")
            islogin = user
            logincount()
        else:
            output.configure(text="Either wrong username or password!!", fg="red")


def logout():
    global islogin
    if (not islogin):
        output_logout.configure(text="You're logged out, already!", fg="red")
    else:
        confirm = input("Are you sure you that want to logout from your account? Yes/No")
        if (confirm == "Yes"):
            islogin = False
            output_logout.configure(text="Logged out successfully!", fg="green")
        else:
            output_logout.configure(text="Logout canceled by user.", fg="red")


def delete():
    global islogin
    if (not islogin):
        output_dlt.configure(text="You need to login first.", fg="red")
    else:
        with open("info.json") as f:
            users_dct = json.load(f)
        confirm = input("Are you sure you that want to delete your account? Yes/No")
        if (confirm == "Yes"):
            users_dct.pop(islogin)
            with open("info.json", "w") as f:
                json.dump(users_dct, f)
            output_dlt.configure(text="Your account has been deleted succesfully!", fg="green")
        else:
            output_dlt.configure(text="Account deletion was canceled by user.", fg="red")


def logincount():
    global islogin
    with open("logincount.json") as f:
        logincount = json.load(f)
    if (islogin in logincount):
        logincount[islogin] += 1
    else:
        logincount[islogin] = 1
    with open("logincount.json", "w") as f:
        json.dump(logincount, f)



def showlogincount():
    global islogin
    if (islogin != "admin"):
        output_count.configure(text="You don't have enough permission to reach this information!", fg="red")
        return
    else:
        with open("logincount.json") as f:
            logincount = json.load(f)
        output_count.configure(text=logincount)



def userslist():
    global islogin
    if (islogin != "admin"):
        output_userslist.configure(text="You don't have enough permissions to reach this information!", fg="red")
        return
    else:
        with open("info.json") as f:
            userslist = json.load(f)
        usrs_lst = str(list(userslist.keys()))
        lst_box.insert("end", usrs_lst)





#######       Tkinter main window       #########
win=Tk.Tk()
win.title("Mid term project")
win.geometry("950x900")


########     Tkinter (Submit)    #########
lbl_submit = Tk.Label(win, text="Submit")
lbl_submit.pack()

lbl_new_user = Tk.Label(win, text="New username:")
lbl_new_user.pack()
input_new_user = Tk.Entry(win, width=40)
input_new_user.pack()

lbl_new_passw = Tk.Label(win, text="New password:")
lbl_new_passw.pack()
input_new_passw = Tk.Entry(win, width=40)
input_new_passw.pack()

output_sub = Tk.Label(win, text="")
output_sub.pack()

Tk.Button(win, text="Submit", command=submit).pack()




########   Tkinter (Login)    #########
lbl_login = Tk.Label(win, text="Login")
lbl_login.pack()

lbl_user = Tk.Label(win, text="Username:")
lbl_user.pack()

input_user = Tk.Entry(win, width=40)
input_user.pack()

lbl_passw = Tk.Label(win, text="Password:")
lbl_passw.pack()
input_passw = Tk.Entry(win, width=40)
input_passw.pack()

output = Tk.Label(win, text="")
output.pack()

Tk.Button(win, text="Login", command=login).pack()



###########      Tkinter (Login count - Delete - Logout)     ############
output_count = Tk.Label(win, text="")
output_count.pack()

Tk.Button(win, text="Login count", command=showlogincount).pack()



output_dlt = Tk.Label(win, text="")
output_dlt.pack()

Tk.Button(win, text="Delete", command=delete).pack()



output_logout = Tk.Label(win, text="")
output_logout.pack()

Tk.Button(win, text="Logout", command=logout).pack()



############      Tkinter (Users list)     #############

output_userslist = Tk.Label(win, text="")
output_userslist.pack()

Tk.Button(win, text="Users list", command=userslist).pack()

lst_box = Tk.Listbox(win, height=20)
lst_box.pack()


###########        Tkinter mainloop     ###########
win.mainloop()


























