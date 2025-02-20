import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql
import ttkbootstrap as tb
import datetime
import random

class LoginApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Barkel Hotel")
        self.root.geometry("800x600")  # Increase width

        # Center window on the screen
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Make window non-resizable
        self.root.resizable(False, False)

        # Logo
        self.logo = tk.PhotoImage(file="l2.png")  # Path to your logo file
        self.logo_label = tk.Label(root, image=self.logo)
        self.logo_label.place(x=50, y=50)  # Adjust the position according to your layout

        # Buttons
        btn_width = 15
        btn_height = 2
        self.btn_guest = tk.Button(root, text="Guest Login", command=self.guest_login, width=btn_width, height=btn_height)
        self.btn_guest.place(relx=0.8, rely=0.3, anchor="center")  # Center the button

        self.btn_admin = tk.Button(root, text="Admin Login", command=self.admin_login, width=btn_width, height=btn_height)
        self.btn_admin.place(relx=0.8, rely=0.5, anchor="center")  # Center the button

        self.btn_exit = tk.Button(root, text="Exit", command=self.root.destroy, width=btn_width, height=btn_height)
        self.btn_exit.place(relx=0.8, rely=0.7, anchor="center")  # Center the button

        # Room Costs
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
        self.nb2 = ttk.Notebook(self.admin_window)
        self.nb2.place(x=0, y=50, relwidth=1, relheight=1)

        self.tab_frames1 = {}
        # Define pages for the tabbed interface
        pages = ["View Reservations", "View Events","View Services", "Clear Reservations", "Clear Events", "Clear Services", "Employees"]

        for page in pages:
            frame = ttk.Frame(self.nb2)
            self.tab_frames1[page] = frame
            self.nb2.add(frame, text=page)

        self.nb2.bind("<<NotebookTabChanged>>", self.switch_page_admin)

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

        page = self.nb2.tab(self.nb2.select(), "text")

        if page == "View Reservations":
            self.go_to_pa1()
        elif page == "View Events":
            self.go_to_pa2()
        elif page == "View Services":
            self.go_to_pa3()
        elif page == "Clear Reservations":
            self.go_to_pa4()
        elif page == "Clear Events":
            self.go_to_pa5()
        elif page == "Clear Services":
            self.go_to_pa6()
        elif page == "Employees":
            self.go_to_pa7()

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
        # Get the frame associated with the "View Reservations" tab
        tab_frame = self.tab_frames1["View Reservations"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()

            # Create a scrollable text widget with a specific size
        text_widget = tk.Text(tab_frame, wrap="none", width=100, height=20)
        text_widget.pack(expand=True, fill="both")

        # Create a scrollbar and link it to the text widget
        scrollbar = tk.Scrollbar(tab_frame, command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)

        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="Bangtan07$",
            database="hotel_database"
        )
        cursor = connection.cursor()

        try:
            # Fetch data from the reservation table joined with the guest table
            cursor.execute("SELECT guest.user_id, guest.name, reservation.roomno, reservation.paymentid, reservation.date_from, reservation.date_To FROM reservation INNER JOIN guest ON reservation.user_id = guest.user_id")
            reservations = cursor.fetchall()

            text_widget.insert("end", "{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}\n".format("Name", "User ID", "Room No", "Payment ID", "Check-in Date", "Check-out Date"))
            text_widget.insert("end", "="*100 + "\n")  # Add a separator line

            for reservation in reservations:
                # Check if the reservation tuple has enough elements
                if len(reservation) >= 6:
                    # Format dates properly
                    check_in_date = reservation[4].strftime("%d-%m-%Y")
                    check_out_date = reservation[5].strftime("%d-%m-%Y")

                    text_widget.insert("end", "{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(reservation[1], reservation[0], reservation[2], reservation[3], check_in_date, check_out_date))
                else:
                    # Handle the case where the reservation tuple does not have enough elements
                    messagebox.showwarning("Data Error", "Incomplete data for reservation: {}".format(reservation))

        except pymysql.Error as err:
            messagebox.showerror("Error", f"Failed to fetch reservations: {err}")
        finally:
            cursor.close()
            connection.close()

        # Disable editing of the text widget
        text_widget.config(state="disabled")

    def go_to_pa2(self):
        # Get the frame associated with the "View Events" tab
        tab_frame = self.tab_frames1["View Events"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Create a text widget to display the events
        text_widget = tk.Text(tab_frame, wrap="none")
        text_widget.pack(expand=True, fill="both")

        try:
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            # Execute SQL query to select specific attributes from the event table
            cursor.execute("SELECT user_id, Payment_ID, Event_type, event_date, total_ppl FROM event")
            events = cursor.fetchall()

            # Display the events in the text widget
            for event in events:
                text_widget.insert("end", f"User ID: {event[0]}\n")
                text_widget.insert("end", f"Payment ID: {event[1]}\n")
                text_widget.insert("end", f"Event Type: {event[2]}\n")
                text_widget.insert("end", f"Event Date: {event[3]}\n")
                text_widget.insert("end", f"Total People: {event[4]}\n")
                text_widget.insert("end", "="*50 + "\n")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to fetch events: {e}")
        finally:
            # Close cursor and database connection
            cursor.close()
            connection.close()

    def go_to_pa3(self):
        # Get the frame associated with the "View Services" tab
        tab_frame = self.tab_frames1["View Services"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Create a text widget to display the services
        text_widget = tk.Text(tab_frame, wrap="none")
        text_widget.pack(expand=True, fill="both")

        try:
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            # Execute SQL query to select all rows from the services table
            cursor.execute("SELECT * FROM services")
            services = cursor.fetchall()

            # Display the services in the text widget
            for service in services:
                text_widget.insert("end", f"User ID: {service[0]}\n")
                text_widget.insert("end", f"Payment ID: {service[1]}\n")
                text_widget.insert("end", f"Service: {service[2]}\n")
                text_widget.insert("end", f"Service Date: {service[3]}\n")
                text_widget.insert("end", "="*50 + "\n")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to fetch services: {e}")
        finally:
            # Close cursor and database connection
            cursor.close()
            connection.close()

    def go_to_pa4(self):
        # Get the frame associated with the "Clear Reservations" tab
        tab_frame = self.tab_frames1["Clear Reservations"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="lime",
            password="Bangtan07$",
            database="hotel_database"
        )
        cursor = connection.cursor()
        
        # Add input fields for Name, room number, and check-in date
        name_label = tk.Label(tab_frame, text="User ID:")
        name_label.place(x=10, y=10)

        name_entry = tk.Entry(tab_frame)
        name_entry.place(x=150, y=10)

        room_label = tk.Label(tab_frame, text="Room Number:")
        room_label.place(x=10, y=40)

        room_entry = tk.Entry(tab_frame)
        room_entry.place(x=150, y=40)

        checkin_label = tk.Label(tab_frame, text="Check-in Date:")
        checkin_label.place(x=10, y=70)

        checkin_entry = tk.Entry(tab_frame)
        checkin_entry.insert(0, "dd-mm-yyyy")  
        checkin_entry.place(x=150, y=70)

        def search_reservation():
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            try:
                # Get input values
                id = name_entry.get()
                room_number = room_entry.get()
                checkin_date = datetime.datetime.strptime(checkin_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")

                # Execute SQL query to find the reservation record
                cursor.execute("SELECT user_id, RoomNo, date_from, date_to, paymentid FROM reservation  WHERE user_id = %s AND RoomNo = %s AND date_from = %s",(id, room_number, checkin_date))
                reservation = cursor.fetchone()

                # Display the reservation record
                if reservation:
                    y_position = 150
                    # Create labels to display the reservation attributes
                    reservation_labels = [
                        ("User ID", reservation[0]),
                        ("Room No:", reservation[1]),
                        ("Check-in Date:", reservation[2]),
                        ("Check-out Date:", reservation[3]),
                        ("Payment ID:", reservation[4])
                    ]

                    # Add labels to the tab frame
                    for label_text, value in reservation_labels:
                        label = tk.Label(tab_frame, text=label_text)
                        label.place(x=10, y=y_position)
                        value_label = tk.Label(tab_frame, text=value)
                        value_label.place(x=150, y=y_position)
                        y_position += 30

                    # Add a checkout button
                    checkout_button = tk.Button(tab_frame, text="Checkout", command=checkout_reservation)
                    checkout_button.place(x=400, y=y_position)
                else:
                    messagebox.showinfo("No Reservation", "No reservation found matching the provided details.")
            finally:
                cursor.close()
                connection.close()

        def checkout_reservation():
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            try:
                # Get input values
                id = name_entry.get()
                room_number = room_entry.get()
                checkin_date = datetime.datetime.strptime(checkin_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")

                # Execute SQL query to delete the reservation record
                cursor.execute("DELETE FROM reservation WHERE user_id = %s AND RoomNo = %s AND date_from = %s",
                            (id, room_number, checkin_date))

                # Check if any rows were affected
                if cursor.rowcount > 0:
                    # Commit the transaction
                    connection.commit()

                    messagebox.showinfo("Checkout Successful", "Reservation successfully checked out.")
                else:
                    messagebox.showerror("Checkout Failed", "Failed to check out reservation.")
            finally:
                cursor.close()
                connection.close()


        # Add a search button to trigger the search
        search_button = tk.Button(tab_frame, text="Search Reservation", command=search_reservation)
        search_button.place(x=400, y=100)

    def go_to_pa5(self):

            # Get the frame associated with the "Clear Events" tab
        tab_frame = self.tab_frames1["Clear Events"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Add input fields for User ID, Hall Type, and Date
        user_id_label = tk.Label(tab_frame, text="User ID:")
        user_id_label.place(x=10, y=10)
        user_id_entry = tk.Entry(tab_frame)
        user_id_entry.place(x=150, y=10)
        
        hall_type_label = tk.Label(tab_frame, text="Hall Type:")
        hall_type_label.place(x=10, y=40)
        hall_type_var = tk.StringVar()
        hall_type_dropdown = ttk.Combobox(tab_frame, textvariable=hall_type_var, values=["Banquet Hall", "Board Room"])
        hall_type_dropdown.place(x=150, y=40)
        
        date_label = tk.Label(tab_frame, text="Date (dd-mm-yyyy):")
        date_label.place(x=10, y=90)
        date_entry = tk.Entry(tab_frame)
        date_entry.place(x=150, y=90)
        
        def search_event():
            try:
                # Connect to the database
                connection = pymysql.connect(
                    host="localhost",
                    user="lime",
                    password="Bangtan07$",
                    database="hotel_database"
                )
                cursor = connection.cursor()

                # Get input values
                user_id = user_id_entry.get()
                hall_type = hall_type_dropdown.get()
                date = datetime.datetime.strptime(date_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")


                # Execute SQL query to find the event record
                cursor.execute("SELECT user_id, Payment_ID, Event_type, event_date, total_ppl FROM event WHERE user_id = %s AND Event_type = %s AND event_date = %s", (user_id, hall_type, date))
                event = cursor.fetchone()

                # Display the event record
                if event:
                    # Create labels to display the event attributes
                    event_labels = [
                        ("User ID:", event[0]),
                        ("Payment ID:", event[1]),
                        ("Hall Type:", event[2]),
                        ("Date:", event[3]),
                        ("Total People:", event[4])
                    ]
                    
                    # Add labels to the tab frame
                    y_position = 150
                    for label_text, value in event_labels:
                        label = tk.Label(tab_frame, text=label_text)
                        label.place(x=10, y=y_position)
                        value_label = tk.Label(tab_frame, text=value)
                        value_label.place(x=150, y=y_position)
                        y_position += 30
                    
                    # Add a delete button
                    delete_button = tk.Button(tab_frame, text="Delete", command=delete_event)
                    delete_button.place(x=10, y=y_position)
                else:
                    messagebox.showinfo("No Event", "No event found matching the provided details.")        
            except pymysql.Error as err:
                messagebox.showerror("Database Error", f"Failed to fetch event: {err}")
            finally:
                # Close cursor and connection
                cursor.close()
                connection.close()

        def delete_event():
            try:
                # Connect to the database
                connection = pymysql.connect(
                    host="localhost",
                    user="lime",
                    password="Bangtan07$",
                    database="hotel_database"
                )
                cursor = connection.cursor()

                user_id = user_id_entry.get()
                hall_type = hall_type_dropdown.get()
                date = datetime.datetime.strptime(date_entry.get(), "%d-%m-%Y").strftime("%Y-%m-%d")


                # Delete the event record from the database
                cursor.execute("DELETE FROM event WHERE user_id = %s AND Event_type = %s AND event_date = %s", (user_id, hall_type, date))
                connection.commit()
                messagebox.showinfo("Event Deletion", "Event successfully deleted.")
            except pymysql.Error as err:
                messagebox.showerror("Database Error", f"Failed to delete event: {err}")
            finally:
                # Close cursor and connection
                cursor.close()
                connection.close()
        search_button = tk.Button(tab_frame, text="Search Event", command=search_event)
        search_button.place(x=400, y=100)

    def go_to_pa6(self):
        # Get the frame associated with the "Clear Services" tab
        tab_frame = self.tab_frames1["Clear Services"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Add input fields for User ID and Service Name
        user_id_label = tk.Label(tab_frame, text="User ID:")
        user_id_label.place(x=10, y=10)
        user_id_entry = tk.Entry(tab_frame)
        user_id_entry.place(x=150, y=10)
        
        service_label = tk.Label(tab_frame, text="Service:")
        service_label.place(x=10, y=40)
        service_var = tk.StringVar()
        service_dropdown = ttk.Combobox(tab_frame, textvariable=service_var, values=["Massage", "Sauna", "Gym Trainer", "Laundry"])
        service_dropdown.place(x=150, y=40)
        
        def search_service():
            try:
                # Connect to the database
                connection = pymysql.connect(
                    host="localhost",
                    user="lime",
                    password="Bangtan07$",
                    database="hotel_database"
                )
                cursor = connection.cursor()

                # Get input values
                user_id = user_id_entry.get()
                service_name = service_dropdown.get()

                # Execute SQL query to find the service record
                cursor.execute("SELECT user_id, PaymentID, Service, Service_date FROM services WHERE user_id = %s AND Service = %s", (user_id, service_name))
                service = cursor.fetchone()

                # Display the service record
                if service:
                    # Create labels to display the service attributes
                    service_labels = [
                        ("User ID:", service[0]),
                        ("Payment ID:", service[1]),
                        ("Service:", service[2]),
                        ("Service Date:", service[3])
                    ]
                    
                    # Add labels to the tab frame
                    y_position = 90
                    for label_text, value in service_labels:
                        label = tk.Label(tab_frame, text=label_text)
                        label.place(x=10, y=y_position)
                        value_label = tk.Label(tab_frame, text=value)
                        value_label.place(x=150, y=y_position)
                        y_position += 30
                    
                    # Add a delete button
                    delete_button = tk.Button(tab_frame, text="Delete", command=delete_service)
                    delete_button.place(x=10, y=y_position)
                else:
                    messagebox.showinfo("No Service", "No service found matching the provided details.")        
            except pymysql.Error as err:
                messagebox.showerror("Database Error", f"Failed to fetch service: {err}")
            finally:
                # Close cursor and connection
                cursor.close()
                connection.close()

        def delete_service():
            try:
                # Connect to the database
                connection = pymysql.connect(
                    host="localhost",
                    user="lime",
                    password="Bangtan07$",
                    database="hotel_database"
                )
                cursor = connection.cursor()

                user_id = user_id_entry.get()
                service_name = service_dropdown.get()

                # Delete the service record from the database
                cursor.execute("DELETE FROM services WHERE user_id = %s AND Service = %s", (user_id, service_name))
                connection.commit()
                messagebox.showinfo("Service Deletion", "Service successfully deleted.")
            except pymysql.Error as err:
                messagebox.showerror("Database Error", f"Failed to delete service: {err}")
            finally:
                # Close cursor and connection
                cursor.close()
                connection.close()
        
        search_button = tk.Button(tab_frame, text="Search Service", command=search_service)
        search_button.place(x=400, y=40)

    def go_to_pa7(self):
        # Get the frame associated with the "View Employees" tab
        tab_frame = self.tab_frames1["Employees"]
        
        # Clear any existing widgets
        for widget in tab_frame.winfo_children():
            widget.destroy()
        
        # Create a text widget to display the employees
        text_widget = tk.Text(tab_frame, wrap="none")
        text_widget.pack(expand=True, fill="both")

        # Create a scrollbar
        scrollbar = tk.Scrollbar(tab_frame, command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)

        try:
            # Connect to the database
            connection = pymysql.connect(
                host="localhost",
                user="lime",
                password="Bangtan07$",
                database="hotel_database"
            )
            cursor = connection.cursor()

            # Execute SQL query to select all rows from the employee table
            cursor.execute("SELECT empID, emp_name, dept, salary, position FROM employee")
            employees = cursor.fetchall()

            # Display the employees in the text widget
            for employee in employees:
                text_widget.insert("end", f"Employee ID: {employee[0]}\n")
                text_widget.insert("end", f"Employee Name: {employee[1]}\n")
                text_widget.insert("end", f"Department: {employee[2]}\n")
                text_widget.insert("end", f"Salary: {employee[3]}\n")
                text_widget.insert("end", f"Position: {employee[4]}\n")
                text_widget.insert("end", "="*50 + "\n")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to fetch employees: {e}")
        finally:
            # Close cursor and database connection
            cursor.close()
            connection.close()

    def logout_guest(self):
        self.guest_window.destroy()
        self.root.deiconify()

    def logout_admin(self):
        self.admin_window.destroy()
        self.root.deiconify()


if __name__ == "__main__":
    root=tb.Window(themename='superhero')
    app = LoginApp(root)
    root.mainloop()
