from tkinter import *
import random
from passwords_data import account_details



account_details2 = {
   'sample01@gmail.com': ('gmail', 'OkNv.ePe$]!IWY'), 
   'sample02@yahoo.com': ('gmail.com', 'yY%vOpO%lWjTE'), 
   'sample03@mail.ru': ('mail', 'rCeBNrgH')
}


# with open("password manager/passwords_data.py", "a") as file:
#     file.write("account_details2")

CHARACTERS_FOR_PASSWORD = "!@#$%^&*.wertyuiop][;laskdfjhgxz/cvm,nZXCMVBNA'SLDFKJGHQWERPOTIYU"


list_of_websites = []


try:
    for key in account_details:
        list_of_websites.append(account_details[key][0])
except:
    pass
print(list_of_websites)

# account_details = "Account_details"




def passwordgen():
    parol = ""
    darozii_parol = random.randint(8,16)
    for i in range(darozii_parol):
        harf = random.choice(CHARACTERS_FOR_PASSWORD)
        parol += harf
    return parol


def new_password():
    ekrani_generate_password = Password_entry.get()
    Password_entry.delete(0, END)
    new_password = passwordgen()
    Password_entry.insert(0, new_password)
    print(account_details)    


index_of_login_password = 0
def find():
    ekrani_nomi_website = website_entry.get()
    if ekrani_nomi_website.lower() in list_of_websites:
        logins_in_this_website = {}
        emptydict = {}
        for login in account_details:
            nomi_sait = account_details[login][0]
            if nomi_sait == ekrani_nomi_website:
                paroli_account = account_details[login][1]
                logins_in_this_website[login] = paroli_account

        global index_of_login_password
        if logins_in_this_website!= emptydict and index_of_login_password <= len(logins_in_this_website):
            print(index_of_login_password)
            print(logins_in_this_website)

            Login_entry.delete(0, END)
            Password_entry.delete(0, END)
            try:
                Login_entry.insert(0, list(logins_in_this_website.keys())[index_of_login_password])
                Password_entry.insert(0, list(logins_in_this_website.values())[index_of_login_password])
                index_of_login_password += 1
            except IndexError:
                pass
                # index_of_login_password = 0 
        if index_of_login_password > (len(logins_in_this_website) - 1):
            index_of_login_password = 0



def save_edit():
    current_website = website_entry.get()
    current_login = Login_entry.get()
    current_password = Password_entry.get()
    if len(current_website) != 0 and len(current_login) != 0 and len(current_password) != 0:
        account_details[current_login] = (current_website, current_password)
        with open("password manager/passwords_data.py", "w") as data:
            data.write(f"account_details = {account_details}")

    if current_login in list_of_websites:
        pass
    else:
        list_of_websites.append(current_website)
    print(account_details)       


# with open("account_details.py", "w") as data:
#     data.write("""account_details = {
# "login": ("website", "password"),
# "sample@gmail.com": ("gmail", "123"),
# } """)


def clear_all():
    Login_entry.delete(0, END)
    Password_entry.delete(0, END)
    website_entry.delete(0, END)
    print(account_details)    




# -----------||  Front End  || --------
main = Tk()
main.title("Password Manager")
main.config(width=700, height=500, padx=20, pady=20)


# photo
canvas = Canvas(width=160, height=180)
background_img = PhotoImage(file="logo.png")
# background_img = PhotoImage(file="password manager/logo.png")
# background_img = PhotoImage(file="tkinter/password manager/logo.png")

canvas.create_image(70,80, image=background_img)
canvas.grid(column=0,row=0, rowspan=5)


# website
website = Label(main, text="Website", font=(16))
website.grid(row=0, column=1, padx=20)

website_entry = Entry(width=50) 
website_entry.grid(row=0, column=2, columnspan=3)


# login
Login = Label(main, text="Login", font=(16))
Login.grid(row=1, column=1, padx=20)

Login_entry = Entry(width=50) 
Login_entry.grid(row=1, column=2, columnspan=3)


# Password
Password = Label(main, text="Password", font=(16))
Password.grid(row=2, column=1, padx=20)

Password_entry = Entry(width=50) 
Password_entry.grid(row=2, column=2, columnspan=3)


# buttons
Find = Button(main, text="Find", width=13, command=find).grid(row=3, column=1)
Generate_password = Button(main, text="Generate", width=13, command=new_password).grid(row=3, column=2)
add_edit = Button(main, text="Add/Edit", width=13, command=save_edit).grid(row=3, column=3)
Clear = Button(main, text="Clear", width=13, command=clear_all).grid(row=3, column=4)


main.mainloop()


print(account_details)

