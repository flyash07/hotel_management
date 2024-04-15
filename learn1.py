import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql
import ttkbootstrap as tb

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("600x600")

        self.btn_guest = tk.Button(root, text="Guest Login", command=self.guest_login)
        self.btn_guest.pack(pady=20)

        self.btn_admin = tk.Button(root, text="Admin Login", command=self.admin_login)
        self.btn_admin.pack(pady=20)

        self.btn_exit = tk.Button(root, text="Exit", command=self.root.destroy)
        self.btn_exit.pack(pady=20)

    def guest_login(self):
        self.root.withdraw()  # Hide the main window
        self.create_guest_login_window()

    def admin_login(self):
        self.root.withdraw()  # Hide the main window
        self.create_admin_login_window()

    def create_admin_login_window(self):
        self.admin_login_window = tk.Toplevel(self.root)
        self.admin_login_window.title("Admin Login")
        self.admin_login_window.geometry("600x400")

        self.lbl_username = tk.Label(self.admin_login_window, text="Username:")
        self.lbl_username.pack()

        self.entry_username = tk.Entry(self.admin_login_window)
        self.entry_username.pack()

        self.lbl_password = tk.Label(self.admin_login_window, text="Password:")
        self.lbl_password.pack()

        self.entry_password = tk.Entry(self.admin_login_window, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(self.admin_login_window, text="Login", command=self.admin_login_check)
        self.btn_login.pack(pady=5)

        self.btn_back = tk.Button(self.admin_login_window, text="Back", command=self.go_back_fromadmin)
        self.btn_back.place(x=10, y=10)

    def create_guest_login_window(self,):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Guest Login")
        self.login_window.geometry("600x600")

        self.lbl_username = tk.Label(self.login_window, text="Username:")
        self.lbl_username.pack()

        self.entry_username = tk.Entry(self.login_window)
        self.entry_username.pack()

        self.lbl_password = tk.Label(self.login_window, text="Password:")
        self.lbl_password.pack()

        self.entry_password = tk.Entry(self.login_window, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(self.login_window, text="Login", command=self.guest_login_check)
        self.btn_login.pack(pady=5)

        self.lbl_create_account = tk.Label(self.login_window, text="First time logging in? Create account")
        self.lbl_create_account.pack()

        self.btn_create_account = tk.Button(self.login_window, text="Create Account", command=self.create_account_window)
        self.btn_create_account.pack(pady=5)

        self.btn_back = tk.Button(self.login_window, text="Back", command=self.go_back_fromguest)
        self.btn_back.place(x=10, y=10)

    def guest_login_check(self):
        self.username = self.entry_username.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="pass",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Execute a SELECT query to check if the username and password match any entry in the users table
            sql = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
            cursor.execute(sql, (self.username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "Login successful")
                # If login is successful, create a new window
                self.login_window.destroy()
                self.create_guest_window()
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except pymysql.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")
        finally:
            cursor.close()
            connection.close()
    
    def admin_login_check(self):
        self.username = self.entry_username.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="pass",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Execute a SELECT query to check if the username and password match any entry in the users table
            sql = "SELECT * FROM admin WHERE username = %s AND password_hash = %s "
            cursor.execute(sql, (self.username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "Admin Login successful")
                # If login is successful, create a new window
                self.admin_login_window.destroy()
                self.create_admin_window()
            else:
                messagebox.showerror("Error", "Invalid admin username or password")
        except pymysql.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")
        finally:
            cursor.close()
            connection.close()




    def go_back_fromguest(self):
        self.login_window.destroy()
        self.root.deiconify()

    def go_back_fromadmin(self):
        self.admin_login_window.destroy()
        self.root.deiconify()

    def create_account_window(self):
        self.account_window = tk.Toplevel(self.root)
        self.account_window.title("Create Account")
        self.account_window.geometry("300x200")

        self.lbl_username = tk.Label(self.account_window, text="Username:")
        self.lbl_username.pack()

        self.entry_username = tk.Entry(self.account_window)
        self.entry_username.pack()

        self.lbl_password = tk.Label(self.account_window, text="Password:")
        self.lbl_password.pack()

        self.entry_password = tk.Entry(self.account_window, show="*")
        self.entry_password.pack()

        self.btn_create_account = tk.Button(self.account_window, text="Create Account", command=self.create_account)
        self.btn_create_account.pack(pady=5)

    def create_account(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="lime",
            password="pass",
            database="hotel_database"
        )
        cursor = connection.cursor()

        # Insert the user account details into the users table
        try:
            sql = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
            connection.commit()
            messagebox.showinfo("Success", "Account created successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to create account: {err}")
        finally:
            cursor.close()
            connection.close()
            self.account_window.destroy()  # Close the account creation window after creating the account


    def create_guest_window(self):
        self.guest_window = tk.Toplevel(self.root)
        self.guest_window.title("Guest Window")
        self.guest_window.geometry("800x600")

        # Welcome Label
        welcome_label = tk.Label(self.guest_window, text="Welcome, Guest!", font=("Arial", 16))
        welcome_label.place(x=10, y=10)

        # Logout Button
        logout_button = tk.Button(self.guest_window, text="Logout", command=self.logout_guest)
        logout_button.place(x=700, y=10)

        # Notebook
        nb = ttk.Notebook(self.guest_window)
        nb.place(x=10, y=50, relwidth=0.95, relheight=0.9)  # Adjust the placement and size as needed

        pages = ["Make a Reservation", "Order Room Service", "Page 3", "Book an Event", "Checkout"]
        for page in pages:
            tab = tk.Frame(nb)
            nb.add(tab, text=page)
        nb.bind("<<NotebookTabChanged>>", lambda event: self.switch_page_guest(nb.tab(nb.select(), "text")))






    def create_admin_window(self):
        self.admin_window = tk.Toplevel(self.root)
        self.admin_window.title("Admin Window")
        self.admin_window.geometry("800x600")

        # Welcome Label
        welcome_label = tk.Label(self.admin_window, text="Welcome, Admin!", font=("Arial", 16))
        welcome_label.place(x=10, y=10)

        # Logout Button
        logout_button = tk.Button(self.admin_window, text="Logout", command=self.logout_admin)
        logout_button.place(x=700, y=10)

        # Tabbed Interface
        nb = ttk.Notebook(self.admin_window)
        nb.place(x=0, y=50, relwidth=1, relheight=1)

        # Define pages for the tabbed interface
        pages = ["View reservations", "View Events", "View payments", "View Employee shifts"]

        for page_name in pages:
            page = ttk.Frame(nb)
            nb.add(page, text=page_name)

    def check_guest_existence(self):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="pass",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Execute a SELECT query to check if the user exists in the guest table
            sql = "SELECT * FROM guest WHERE user_ID = %s"
            cursor.execute(sql, (self.username,))
            user = cursor.fetchone()

            if user:
                return True
            else:
                return False
        except pymysql.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")
        finally:
            cursor.close()
            connection.close()

    def switch_page_guest(self, page):
        # Logic to switch to the selected page
        if page == "Make a Reservation":
            self.go_to_pg1()
        elif page == "Order Room Service":
            self.go_to_pg2()
        elif page == "Page 3":
            self.go_to_pg3()
        elif page == "Book an Event":
            self.go_to_pg4()
        elif page == "Checkout":
            self.go_to_pg5()
        pass

    def switch_page_admin(self,page):
        pass

    def go_to_pg1(self):
        if self.check_guest_existence():
            messagebox.showinfo("Info", "User exists in the guest table.")
        else:
            messagebox.showinfo("Info", "User does not exist in the guest table.")

    def go_to_pg2(self):
        # Logic to display page 2
        pass

    def go_to_pg3(self):
        # Logic to display page 3
        pass

    def go_to_pg4(self):
        # Logic to display page 4
        pass
    def go_to_pg5(self):
        # Logic to display page 4
        pass

    def logout_guest(self):
        self.guest_window.destroy()
        self.root.deiconify()

    def logout_admin(self):
        self.admin_window.destroy()
        self.root.deiconify()



if __name__ == "__main__":
    root=tb.Window(themename='superhero')
    #root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
