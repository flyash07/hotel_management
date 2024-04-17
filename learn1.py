import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql
import ttkbootstrap as tb
import datetime
import random

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

        self.room_costs = {
            "Suite": 8000,
            "Double": 4000,
            "Single": 2000
        }


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
        self.user_id = self.entry_username.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="Bangtan07$",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Execute a SELECT query to check if the username and password match any entry in the users table
            sql = "SELECT * FROM users WHERE user_id = %s AND password_hash = %s"
            cursor.execute(sql, (self.user_id, password))
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
            password="Bangtan07$",
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
        self.user_id = self.entry_username.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="lime",
            password="Bangtan07$",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            sql = "INSERT INTO users (user_id, password_hash) VALUES (%s, %s)"
            cursor.execute(sql, (self.user_id, password))
            connection.commit()
            messagebox.showinfo("Success", "Account created successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to create account: {err}")
        finally:
            cursor.close()
            connection.close()
            self.account_window.destroy()  # Close the account creation window after creating the account
            self.login_window.destroy()  # Destroy the guest login window
            self.create_guest_login_window()  # Recreate the guest login window


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

        # Create a notebook to hold the tabs
        self.nb1 = ttk.Notebook(self.guest_window)
        self.nb1.place(x=10, y=50, relwidth=0.95, relheight=0.9)

        self.tab_frames = {}
        pages = ["Make a Reservation", "Book a Service", "Order Food", "Book an Event"]
        for page in pages:
            frame = tk.Frame(self.nb1)
            self.tab_frames[page] = frame
            self.nb1.add(frame, text=page)

        # Bind the tab change event
        self.nb1.bind("<<NotebookTabChanged>>", self.switch_page_guest)

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
        pages = ["View reservations", "Clear Service", "Clear reservations", "View Events"]

        for page_name in pages:
            page = ttk.Frame(nb)
            nb.add(page, text=page_name)
        nb.bind("<<NotebookTabChanged>>", lambda event: self.switch_page_admin(nb.tab(nb.select(), "text")))

    def check_guest_existence(self):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="Bangtan07$",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Execute a SELECT query to check if the user exists in the guest table
            sql = "SELECT * FROM guest WHERE user_ID = %s"
            cursor.execute(sql, (self.user_id,))
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

    def switch_page_guest(self, event=None):
        # Logic to switch to the selected page
        selected_tab_text = self.nb1.tab(self.nb1.select(), "text")

        if selected_tab_text == "Make a Reservation":
            self.go_to_pg1()
        elif selected_tab_text == "Book a Service":
            self.go_to_pg2()
        elif selected_tab_text == "Order Food":
            self.go_to_pg3()
        elif selected_tab_text == "Book an Event":
            self.go_to_pg4()
        pass

    def switch_page_admin(self,page):
        if page == "View reservations":
            self.go_to_pa1()
        elif page == "Clear Service":
            self.go_to_pa2()
        elif page == "Clear reservations":
            self.go_to_pa3()
        elif page == "View Events":
            self.go_to_pa4()
        elif page == "Checkout":
            self.go_to_pa5()
        pass

    def go_to_pg1(self):
        if not self.check_guest_existence():
            # Pop up a window to collect additional details
            additional_details_window = tk.Toplevel(self.guest_window)
            additional_details_window.title("Additional Details")
            additional_details_window.geometry("300x200")

            # Label and Entry for Name
            name_label = tk.Label(additional_details_window, text="Name:")
            name_label.pack()

            name_entry = tk.Entry(additional_details_window)
            name_entry.pack()

            # Label and Entry for Aadhar Number
            aadhar_label = tk.Label(additional_details_window, text="Aadhar Number:")
            aadhar_label.pack()

            aadhar_entry = tk.Entry(additional_details_window)
            aadhar_entry.pack()

            additional_details_window.lift()
            def insert_into_guest():
                name = name_entry.get()
                aadhar = aadhar_entry.get()

                try:
                    connection = pymysql.connect(
                        host="localhost",
                        user="lime",
                        password="Bangtan07$",
                        database="hotel_database"
                    )
                    cursor = connection.cursor()

                    sql = "INSERT INTO guest (user_ID, Name, Aadhaar) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (self.user_id, name, aadhar))
                    connection.commit()

                    messagebox.showinfo("Info", "Data inserted into guest table.")
                except pymysql.Error as err:
                    messagebox.showerror("Error", f"Failed to insert data into guest table: {err}")
                finally:
                    cursor.close()
                    connection.close()
                    additional_details_window.destroy()


            # Button to confirm and insert data
            confirm_button = tk.Button(additional_details_window, text="Confirm", command=insert_into_guest)
            confirm_button.pack()
            # Get the frame associated with the "Make a Reservation" tab
        
        tab_frame = self.tab_frames["Make a Reservation"]

        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()

        # Add widgets to the tab frame
        room_type_label = tk.Label(tab_frame, text="Room Type:")
        room_type_label.place(x=10, y=20)

        self.room_type_dropdown = ttk.Combobox(tab_frame, values=["Suite", "Double", "Single"])
        self.room_type_dropdown.place(x=130, y=20)

        check_in_label = tk.Label(tab_frame, text="Check-In Date:")
        check_in_label.place(x=10, y=60)

        self.check_in_entry = tk.Entry(tab_frame)
        self.check_in_entry.insert(0, "dd-mm-yyyy")
        self.check_in_entry.place(x=130, y=60)

        checkout_label = tk.Label(tab_frame, text="Check-Out Date:")
        checkout_label.place(x=10, y=90)

        self.checkout_entry = tk.Entry(tab_frame)
        self.checkout_entry.insert(0, "dd-mm-yyyy")  
        self.checkout_entry.place(x=130, y=90)

        # Add the cost label
        cost_label = tk.Label(tab_frame, text="Cost:")
        cost_label.place(x=10, y=120)

         # Add a button
        submit_button = tk.Button(tab_frame, text="Submit Reservation", command=self.submit_reservation)
        submit_button.place(x=100, y=200)  # Adjust the coordinates as needed


        # Calculate and display the reservation cost when dates or room type changes
        def calculate_cost(event=None):
            room_type = self.room_type_dropdown.get()
            check_in_date = self.check_in_entry.get()
            checkout_date = self.checkout_entry.get()

            # Call the calc_reservation_cost method with the provided inputs
            cost = self.calc_reservation_cost(room_type, check_in_date, checkout_date)

            # Update the cost label with the calculated cost
            self.cost_value_label.config(text=str(cost))

        # Bind the calculate_cost function to events that might trigger a cost update
        self.room_type_dropdown.bind("<<ComboboxSelected>>", calculate_cost)
        self.check_in_entry.bind("<FocusOut>", calculate_cost)
        self.checkout_entry.bind("<FocusOut>", calculate_cost)

        # Initialize the cost value label
        self.cost_value_label = tk.Label(tab_frame, text="")
        self.cost_value_label.place(x=100, y=120)  # Adjust the coordinates as needed

        # Initial calculation of the cost
        calculate_cost()

       
  
    def submit_reservation(self):
        try:
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            # Get the cost from the cost value label
            cost = float(self.cost_value_label.cget("text"))

            # Get the selected room type from the UI
            room_type = self.room_type_dropdown.get()

            # Get the check-in and check-out dates from the UI

            # Convert date strings to MySQL-compatible format
            date_from = datetime.datetime.strptime(self.check_in_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")
            date_to = datetime.datetime.strptime(self.checkout_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")


            # Check room availability
            sql_check_availability = "SELECT COUNT(*) FROM rooms WHERE Type = %s AND RoomNo NOT IN (SELECT RoomNo FROM reservation WHERE (%s BETWEEN date_from AND date_to OR %s BETWEEN date_from AND date_to) AND Type = %s)"
            cursor.execute(sql_check_availability, (room_type, date_from, date_to, room_type))
            available_rooms_count = cursor.fetchone()[0]

            if available_rooms_count == 0:
                messagebox.showinfo("Info", "Rooms fully booked.")
                return

            # Insert into payment table
            sql_payment = "INSERT INTO payment (user_id, Dateofpayment, amount) VALUES (%s, CURDATE(), %s)"
            cursor.execute(sql_payment, (self.user_id, cost))
            connection.commit()

            # Get the payment ID
            payment_id = cursor.lastrowid

            # Get the room number of the first available room
            sql_get_room_number = "SELECT RoomNo FROM rooms WHERE Type = %s AND RoomNo NOT IN (SELECT RoomNo FROM reservation WHERE (%s BETWEEN date_from AND date_to OR %s BETWEEN date_from AND date_to) AND Type = %s) LIMIT 1"
            cursor.execute(sql_get_room_number, (room_type, date_from, date_to, room_type))
            room_no = cursor.fetchone()[0]

            # Insert into reservation table
            sql_reservation = "INSERT INTO reservation (user_id, RoomNo, PaymentID, date_from, date_to) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_reservation, (self.user_id, room_no, payment_id, date_from, date_to))
            connection.commit()

            messagebox.showinfo("Info", "Reservation made successfully.")
        except pymysql.Error as err:
            messagebox.showerror("Error", f"Failed to make reservation: {err}")
        finally:
            cursor.close()
            connection.close()


    def calc_reservation_cost(self, room_type, check_in_date, checkout_date):

        # Get the cost based on room type and floor number
        room_cost = self.room_costs.get(room_type, 0)

        # Convert check-in and check-out dates to datetime objects
        check_in = datetime.datetime.strptime(check_in_date, "%d-%m-%Y")
        checkout = datetime.datetime.strptime(checkout_date, "%d-%m-%Y")

        # Calculate the number of days between check-in and check-out dates
        num_days = (checkout - check_in).days

        # Calculate the total cost by multiplying room cost with the number of days
        total_cost = room_cost * num_days

        return total_cost


    def go_to_pg2(self):
        # Get the frame associated with the "Book a Service" tab
        tab_frame = self.tab_frames["Book a Service"]

        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()

        # Add widgets to the tab frame
        service_label = tk.Label(tab_frame, text="Select Service:")
        service_label.place(x=10, y=10)  # Adjust the coordinates as needed

        service_dropdown = ttk.Combobox(tab_frame, values=["Massage", "Sauna", "Gym Trainer", "Laundry"])
        service_dropdown.place(x=120, y=10)  # Adjust the coordinates as needed

        # Define the book_service function

        def book_service():

            selected_service = service_dropdown.get()
            
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            try:
                # Insert a payment record with an amount of 1000 and retrieve the payment ID
                cursor.execute("INSERT INTO payment (user_id, Dateofpayment, amount) VALUES (%s, CURDATE(), %s)", (self.user_id, 1000))
                connection.commit()
                payment_id = cursor.lastrowid

                # Insert a record into the services table using the retrieved payment ID
                cursor.execute("INSERT INTO services (user_id, PaymentID, Service, Service_date) VALUES (%s, %s, %s, CURDATE())", (self.user_id, payment_id, selected_service))
                connection.commit()

                messagebox.showinfo("Booking", f"Service '{selected_service}' booked successfully!")
            except pymysql.Error as err:
                messagebox.showerror("Error", f"Failed to book service: {err}")
            finally:
                cursor.close()
                connection.close()

        book_button = tk.Button(tab_frame, text="Book", command=book_service)
        book_button.place(x=10, y=50)  # Adjust the coordinates as needed

    def go_to_pg3(self):
        # Get the frame associated with the "Order Food" tab
        tab_frame = self.tab_frames["Order Food"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Add widgets to the tab frame
        buffet_label = tk.Label(tab_frame, text="Select Buffet:")
        buffet_label.place(x=10, y=10)

        # Define the options for the buffet combobox
        buffet_options = ["Breakfast Buffet", "Lunch Buffet", "Dinner Buffet"]
        selected_buffet = tk.StringVar()
        buffet_combobox = ttk.Combobox(tab_frame, textvariable=selected_buffet, values=buffet_options)
        buffet_combobox.place(x=120, y=10)

        # Define a function to handle the booking of the selected buffet
        def book_buffet():
            selected_food = selected_buffet.get()
    
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            try:
                # Insert a payment record with an amount of 1000 and retrieve the payment ID
                cursor.execute("INSERT INTO payment (user_id, Dateofpayment, amount) VALUES (%s, CURDATE(), %s)", (self.user_id, 1000))
                connection.commit()
                payment_id = cursor.lastrowid

                # Insert a record into the services table using the retrieved payment ID
                cursor.execute("INSERT INTO services (user_id, PaymentID, Service, Service_date) VALUES (%s, %s, %s, CURDATE())", (self.user_id, payment_id, selected_food))
                connection.commit()

                messagebox.showinfo("Booking Confirmation", f"Booked {selected_food} successfully!")
            except pymysql.Error as err:
                messagebox.showerror("Error", f"Failed to book buffet: {err}")
            finally:
                cursor.close()
                connection.close()

        # Add a button to allow the user to book the selected buffet
        book_button = tk.Button(tab_frame, text="Book", command=book_buffet)
        book_button.place(x=10, y=50)


    def go_to_pg4(self):
        # Get the frame associated with the "Book an Event" tab
        tab_frame = self.tab_frames["Book an Event"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Add widgets to the tab frame
        # 1. Radio buttons for event type selection
        event_type_label = tk.Label(tab_frame, text="Select Event Type:")
        event_type_label.place(x=10, y=10)

        selected_event_type = tk.StringVar()
        event_type_frame = tk.Frame(tab_frame)
        event_type_frame.place(x=150, y=10)

        board_room_radio = tk.Radiobutton(event_type_frame, text="Board Room", variable=selected_event_type, value="Board Room")
        board_room_radio.pack(side="left")

        banquet_hall_radio = tk.Radiobutton(event_type_frame, text="Banquet Hall", variable=selected_event_type, value="Banquet Hall")
        banquet_hall_radio.pack(side="left")

        # 2. Date input
        date_label = tk.Label(tab_frame, text="Select Date:")
        date_label.place(x=10, y=50)

        date_entry = tk.Entry(tab_frame)
        date_entry.insert(0, "dd-mm-yyyy")
        date_entry.place(x=150, y=50)

        # 3. Number of people input
        num_people_label = tk.Label(tab_frame, text="Number of People:")
        num_people_label.place(x=10, y=90)

        num_people_entry = tk.Entry(tab_frame)
        num_people_entry.place(x=150, y=90)

        # 4. Book button
        def book_event():
            event_type = selected_event_type.get()
            event_date = date_entry.get()
            num_people = num_people_entry.get()

            event_date = datetime.datetime.strptime(date_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")

            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            try:
                              
                cursor.execute("SELECT COUNT(*) FROM event WHERE event_date = %s AND event_type = %s", (event_date, event_type))
                count = cursor.fetchone()[0]
                
                if count > 0:
                    messagebox.showwarning("Booking Error", f"{event_type} event is already booked for {event_date}. Please select another date or event type.")
                else:
                    # Proceed with the booking
                    cursor.execute("INSERT INTO payment (user_id, Dateofpayment, amount) VALUES (%s, CURDATE(), %s)", (self.user_id, 50000))
                    connection.commit()
                    payment_id = cursor.lastrowid

                    cursor.execute("INSERT INTO event (user_id, Payment_ID, event_type, event_date, total_ppl) VALUES (%s, %s, %s, %s, %s)", (self.user_id, payment_id, event_type, event_date, num_people))
                    connection.commit()

                    messagebox.showinfo("Event Booking", f"Booked {event_type} for {num_people} people on {event_date} successfully!")

            except pymysql.Error as err:
                messagebox.showerror("Database Error", f"Failed to book event: {err}")
            finally:
                cursor.close()
                connection.close()    

        book_button = tk.Button(tab_frame, text="Book", command=book_event)
        book_button.place(x=10, y=130)


    def go_to_pa1(self):
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
