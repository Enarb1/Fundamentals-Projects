import re
import tkinter as tk
from tkinter import messagebox


def main_window():
    root = tk.Tk()
    root.geometry('600x600')
    root.title("Validator")

    name = tk.Label(root, text='Validate Your Data', font=('Arial', 20), )
    name.pack()
    input_field = tk.Text(root, height=3)
    input_field.pack(padx=10, pady=20)

    def validate_email():

        email = input_field.get("1.0", "end-1c").strip()
        email_pattern = r'^[a-zA-Z0-9._-]+@[a-z0-9]+[.][a-z.]{2,6}$'
        if re.match(email_pattern, email):
            messagebox.showinfo("Info", 'Email is Valid')
        else:
            messagebox.showerror('Info', 'Invalid Email')

    def validate_phone():
        phone = input_field.get("1.0", "end-1c").strip()
        phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
        if re.match(phone_pattern, phone):
            messagebox.showinfo("Info", 'Valid Phone number')
        else:
            messagebox.showerror('Info', 'Invalid Phone number')

    def validate_postal_code():
        postal_code = input_field.get("1.0", "end-1c").strip()
        postal_code_pattern = r'^\d{5}$|^\d{5}-\d{4}$'
        if re.match(postal_code_pattern, postal_code):
            messagebox.showinfo("Info", 'Valid Postcode')
        else:
            messagebox.showerror('Info', 'Invalid Postcode')

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    email_button = tk.Button(buttonframe, text='Validate Email', font=('Arial', 15), command=validate_email)
    email_button.grid(row=0, column=0, sticky=tk.W + tk.E)

    phone_button = tk.Button(buttonframe, text='Validate Phone', font=('Arial', 15), command=validate_phone)
    phone_button.grid(row=0, column=1, sticky=tk.W + tk.E)

    postcode_button = tk.Button(buttonframe, text='Validate Postcode', font=('Arial', 15), command=validate_postal_code)
    postcode_button.grid(row=0, column=2, sticky=tk.W + tk.E)

    buttonframe.pack()

    root.mainloop()


main_window()
