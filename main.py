from tkinter import *
from tkinter.messagebox import showerror
from turtle import left
from tkcalendar import Calendar, DateEntry

# Close the application window
def quit():
    main_window.destroy()  

# Calculate deck materials needed based on user input
1

    # Here you would add the logic to calculate the materials needed based on the input
    # For example, you could calculate the total cost or the materials required for the hired items

# Set up the GUI interface
def main():
    Button(main_window, text="Quit", command=quit).grid(row=0, column=0, sticky=W)
    Button(main_window, text="Calculate", command=entry_print).grid(row=0, column=1, padx=10, pady=5, sticky=W)
    Label(main_window, text="First Name:").grid(row=1, column=0, sticky=W)
    Label(main_window, text="Last Name:").grid(row=2, column=0, sticky=W)
    Label(main_window, text="Receipt number:").grid(row=3, column=0, sticky=W)
    Label(main_window, text="Item Hired:").grid(row=4, column=0, sticky=W)
    Label(main_window, text="Number Hired:").grid(row=5, column=0, sticky=W)
    Label(main_window, text="Date Item is Hired From:").grid(row=6, column=0, sticky=W)
    Label(main_window, text="Date Item will be Returned:").grid(row=7, column=0, sticky=W)
    cal = DateEntry(main_window, width=12, background='darkblue', foreground='white', borderwidth=2)
    main_window.mainloop()

# Initialize main window and entry fields
main_window = Tk()
first_name = Entry(main_window)
last_name = Entry(main_window)
receipt_number = Entry(main_window)
item_hired = Entry(main_window)
number_hired = Entry(main_window)
day_hired_from = Entry(main_window)
month_hired_from = Entry(main_window)
year_hired_from = Entry(main_window)
calendar = DateEntry(main_window, width=12, background='darkblue', foreground='white', borderwidth=2)
calendar2 = DateEntry(main_window, width=12, background='darkblue', foreground='white', borderwidth=2)


date_returned = Entry(main_window)
first_name.grid(row=1, column=1, padx=10, pady=5)
last_name.grid(row=2, column=1, padx=10, pady=5)
receipt_number.grid(row=3, column=1, padx=10, pady=5)
item_hired.grid(row=4, column=1, padx=10, pady=5)
number_hired.grid(row=5, column=1, padx=10, pady=5)
calendar.grid(row=6, column=1, padx=10, pady=5, sticky=W)   
calendar2.grid(row=7, column=1, padx=10, pady=5, sticky=W)

if first_name.get() == "" or last_name.get() == "":
   showerror("Error", "Please enter both first and last name.")
main()