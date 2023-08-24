import tkinter as tk
import random
import string 


class PasswordGenerator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Password Generator")
        self.geometry("400x400")
        
        self.password_generator = tk.Label(self, text="Password Generator", font=("Arial", 20, "bold"), fg="darkblue")
        self.password_generator.pack(pady=10)
        
        self.name_label = tk.Label(self, text="Enter user name:", font=("Arial", 10, "bold"))
        self.name_label.pack(pady=5)
        
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        self.length_label = tk.Label(self, text="Enter password length:", font=("Arial", 10, "bold"))
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(self)
        self.length_entry.pack()
        
        self.password_label = tk.Label(self, text="Generated password:", font=("Arial", 10, "bold"))
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        self.generate_button = tk.Button(self, text="GENERATE PASSWORD", command=self.generate_password, font=("Arial", 10, "bold"),bg="darkblue", fg="white")
        self.generate_button.pack(pady=20)

        self.generate_button = tk.Button(self, text="ACCEPT", command=self.generate_password, font=("Arial", 10, "bold"),bg="darkblue", fg="white")
        self.generate_button.pack(pady=8)

        self.generate_button = tk.Button(self, text="RESET", command=self.generate_password, font=("Arial", 10, "bold"),bg="darkblue", fg="white")
        self.generate_button.pack(pady=8)



    

        

    def generate_password(self):
        password_length = int(self.length_entry.get())
        
        character_set = ""

        if character_set:
            password = "".join(random.choice(character_set) for _ in range(password_length))
        else:
            password = "S*<2~j\A@k"

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.mainloop()