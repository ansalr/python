import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BusBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Booking System")
        self.root.config(bg="gray")

        ttk.Label(root, text="From:").grid(row=0,column=0, padx=5, pady=5)
        ttk.Label(root, text="To:").grid(row=1,column=0, padx=5, pady=5)
        ttk.Label(root, text="Name:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(root, text="Gender:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(root, text="Age:").grid(row=4, column=0, padx=5, pady=5)
        ttk.Label(root, text="Date:").grid(row=5, column=0, padx=5, pady=5)
        ttk.Label(root, text="Time:").grid(row=6, column=0, padx=5, pady=5)
        ttk.Label(root, text="seat:").grid(row=7, column=0, padx=5, pady=5)

        # Creating entry widgets
        self.from_entry = ttk.Entry(root, width=30)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.to_entry = ttk.Entry(root, width=30)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.name_entry = ttk.Entry(root, width=30)
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.gender_var = tk.StringVar()
        self.gender_dropdown = ttk.Combobox(root, width=27, textvariable=self.gender_var, state='readonly')
        self.gender_dropdown['values'] = ('','Male', 'Female', 'Other')
        self.gender_dropdown.current(0)
        self.gender_dropdown.grid(row=3, column=1, padx=5, pady=5)

        self.from_var = tk.StringVar()
        self.from_dropdown = ttk.Combobox(root, width=27, textvariable=self.from_var, state='readonly')
        self.from_dropdown['values'] = ('','lucknow', 'Varanasi', 'Agra')
        self.from_dropdown.current(0)
        self.from_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.to_var = tk.StringVar()
        self.to_dropdown = ttk.Combobox(root, width=27, textvariable=self.to_var, state='readonly')
        self.to_dropdown['values'] = ('','Noida', 'Ayaodha', 'Azamgarh')
        self.to_dropdown.current(0)
        self.to_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.seat_var = tk.StringVar()
        self.seat_dropdown = ttk.Combobox(root, width=27, textvariable=self.seat_var, state='readonly')
        self.seat_dropdown['values'] = ('','UPPER', 'LOWER', 'BERTH')
        self.seat_dropdown.current(0)
        self.seat_dropdown.grid(row=7, column=1, padx=5, pady=5)
        
        self.age_entry = ttk.Entry(root, width=30)
        self.age_entry.grid(row=4, column=1, padx=5, pady=5)
        
        self.date_entry = ttk.Entry(root, width=30)
        self.date_entry.grid(row=5, column=1, padx=5, pady=5)

        self.time_entry = ttk.Entry(root, width=30)
        self.time_entry.grid(row=6, column=1, padx=5, pady=5)
 
        # Creating submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.book_ticket)
        self.submit_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def book_ticket(self):
        # Get values from entry widgets
        from_place = self.from_var.get()
        to_place = self.to_var.get()
        name = self.name_entry.get()
        gender = self.gender_var.get()
        age = self.age_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        seat =self.seat_var.get()


        # Check if any field is empty
        if from_place == '' or to_place == '' or name == '' or age == '' or date == '' or time == '' or seat =='':
            messagebox.showerror("Error", "Please fill in all fields.")
        
            
        else:
        # Display booking details
            messagebox.showinfo("Booking Details", f"Booking Confirmed!\n\nFrom: {from_place}\nTo: {to_place}\nName: {name}\nGender: {gender}\nAge: {age}\nDate: {date}\nTime: {time}\nseat:{seat}")
        return

# Create main window
root = tk.Tk()
app = BusBookingApp(root)
root.mainloop()