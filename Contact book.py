import json
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"

class ContactBookGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("400x300")

        self.contact_book = ContactBook()

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save Contacts", command=self.save_contacts)
        self.file_menu.add_command(label="Load Contacts", command=self.load_contacts)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.add_contact_button = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(pady=5)

        self.delete_contact_button = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(pady=5)

        self.display_contacts_button = tk.Button(self, text="Display Contacts", command=self.display_contacts)
        self.display_contacts_button.pack(pady=5)

    def add_contact(self):
        add_contact_window = tk.Toplevel(self)
        add_contact_window.title("Add Contact")
        add_contact_window.geometry("300x200")

        name_label = tk.Label(add_contact_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(add_contact_window)
        self.name_entry.pack()

        phone_label = tk.Label(add_contact_window, text="Phone Number:")
        phone_label.pack()
        self.phone_entry = tk.Entry(add_contact_window)
        self.phone_entry.pack()

        email_label = tk.Label(add_contact_window, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(add_contact_window)
        self.email_entry.pack()

        save_button = tk.Button(add_contact_window, text="Save", command=self.save_contact)
        save_button.pack()

    def save_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        contact = Contact(name, phone_number, email)
        self.contact_book.add_contact(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def delete_contact(self):
        delete_contact_window = tk.Toplevel(self)
        delete_contact_window.title("Delete Contact")
        delete_contact_window.geometry("300x100")

        delete_label = tk.Label(delete_contact_window, text="Enter name to delete:")
        delete_label.pack()
        self.delete_entry = tk.Entry(delete_contact_window)
        self.delete_entry.pack()

        delete_button = tk.Button(delete_contact_window, text="Delete", command=self.delete_contact_action)
        delete_button.pack()

    def delete_contact_action(self):
        name = self.delete_entry.get()
        self.contact_book.delete_contact(name)
        self.delete_entry.delete(0, tk.END)

    def display_contacts(self):
        display_contacts_window = tk.Toplevel(self)
        display_contacts_window.title("Display Contacts")
        display_contacts_window.geometry("400x300")

        contacts_text = tk.Text(display_contacts_window)
        contacts_text.pack()

        contacts_text.insert(tk.END, "Contacts:\n")
        for contact in self.contact_book.contacts.values():
            contacts_text.insert(tk.END, str(contact) + "\n")

    def save_contacts(self):
        file_name = tk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_name:
            self.contact_book.save_contacts(file_name)

    def load_contacts(self):
        file_name = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_name:
            self.contact_book.load_contacts(file_name)

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            messagebox.showerror("Error", f"{name} not found in contacts.")

    def save_contacts(self, file_name):
        with open(file_name, 'w') as f:
            json.dump([vars(contact) for contact in self.contacts.values()], f)
        messagebox.showinfo("Success", "Contacts saved successfully.")

    def load_contacts(self, file_name):
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
                self.contacts = {contact_data['name']: Contact(contact_data['name'], contact_data['phone_number'], contact_data['email']) for contact_data in data}
            messagebox.showinfo("Success", "Contacts loaded successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found. No contacts loaded.")

if __name__ == "__main__":
    app = ContactBookGUI()
    app.mainloop()
