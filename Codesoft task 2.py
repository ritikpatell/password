import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.name_label = tk.Label(root, text="Name:", font=("Helvetica", 12))
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.name_entry.pack()

        self.generated_password = tk.StringVar()
        self.generated_password_label = tk.Label(root, textvariable=self.generated_password, font=("Courier", 16))
        self.generated_password_label.pack()

        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.accept_button = tk.Button(root, text="Accept Password", command=self.accept_password)
        self.accept_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

        self.accepted_password = ""

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            password = self.generate_random_password(length)
            self.generated_password.set(password)
            self.accepted_password = ""
        except ValueError:
            self.generated_password.set("Invalid length")

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def accept_password(self):
        self.accepted_password = self.generated_password.get()

    def reset(self):
        self.name_entry.delete(0, tk.END)
        self.generated_password.set("")
        self.length_entry.delete(0, tk.END)
        self.accepted_password = ""

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()