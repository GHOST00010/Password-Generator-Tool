# import random
# print("This program is used to generate strong passwords to save your account from attackers. ")

# user = input(str("Enter your USER name:"))
# print(f"Welcome, {user}.")


# #Password length
# def length():
#     while True:
#         try:
#             length = int(input("Length of password : "))

#             if length <= 0:
#                 print("Please enter a positive numeber.")
#                 continue
#             return length
#         except ValueError:
#             print("Please enter only numeric values.")
#     return length()

# password_length = length()
# print(f"{user} want's {password_length} length of password.")

# #Upper, Lower, Numbers and Special Char ?
# print("answer in y or n (yes --> y and no --> n) default is 'y'")

# print("Do you want.....")


# while True:

#     upper_case = str(input("Upper characters in password? ")).lower() or 'y'
#     lower_case = str(input("Lower characters in password? ")).lower() or 'y'
#     numbers   = str(input("Numbers in password? ")).lower() or 'y'
#     special_char = str(input("Special characters in password?" )).lower() or 'y'

#     if upper_case != 'y' and  upper_case != 'n':
#         print("Please enter y or n")
#     elif lower_case != 'y' and lower_case != 'n':
#         print("Please enter y or n")
#     elif numbers != 'y' and numbers!= 'n':
#         print("Please enter y or n")
#     elif special_char != 'y' and special_char != 'n':
#         print("Please enter y or n")
#     elif upper_case == 'n' and lower_case == 'n' and numbers == 'n' and special_char == 'n':
#         print("Please Select Atleat on character type.")
#     else:
#         print("Thanks....")
#         break

# print("Legth of Password :",password_length)
# print("Is upper case     :",upper_case)
# print("Is lower case     :",lower_case)
# print("Is numbers        :",numbers)
# print("Is special chars  :",special_char)

# #Character Pool

# upper_char_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lower_char_pool = "abcdefghijklmnopqrstuvwxyz"
# nums            = "0123456789"
# special_characaters    = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# #Creation of character pool

# character_pool = [""]

# if upper_case == "y":
#     character_pool += upper_char_pool
# if lower_case == "y":
#     character_pool  += lower_char_pool
# if numbers       == "y":
#     character_pool += nums
# if special_char == "y":
#     character_pool += special_characaters


# #Password Generation
# password = []
# for i in range(password_length):
#     password.append(str(random.choice(character_pool)))
# password = "".join(password)
    
# print(
#     f'''The password for the {user}  is "{password}".'''
#     )




import math
import secrets
import tkinter as tk
from tkinter import ttk, messagebox

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SPECIAL = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


class App(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=12)
        self.grid(sticky="nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.user = tk.StringVar()
        self.length = tk.IntVar(value=16)
        self.upper = tk.BooleanVar(value=True)
        self.lower = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.special = tk.BooleanVar(value=True)
        self.password = tk.StringVar()
        self.show = tk.BooleanVar(value=True)
        self.strength_text = tk.StringVar(value="Strength: -")
        self.status = tk.StringVar(value="Ready")

        self.build()

    def build(self):
        ttk.Label(self, text="User name:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=self.user).grid(row=0, column=1, columnspan=2, sticky="ew", pady=4)

        ttk.Label(self, text="Password length:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Spinbox(self, from_=1, to=128, textvariable=self.length, width=6).grid(
            row=1, column=1, sticky="w", pady=4)

        box = ttk.LabelFrame(self, text="Include", padding=8)
        box.grid(row=2, column=0, columnspan=3, sticky="ew", pady=8)
        ttk.Checkbutton(box, text="Uppercase letters (A-Z)", variable=self.upper).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(box, text="Lowercase letters (a-z)", variable=self.lower).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(box, text="Numbers (0-9)", variable=self.numbers).grid(row=0, column=1, sticky="w", padx=20)
        ttk.Checkbutton(box, text="Special characters (!@#$...)", variable=self.special).grid(
            row=1, column=1, sticky="w", padx=20)

        ttk.Button(self, text="Generate", command=self.generate).grid(row=3, column=0, sticky="w", pady=4)

        ttk.Label(self, text="Password:").grid(row=4, column=0, sticky="w", pady=4)
        self.entry = ttk.Entry(self, textvariable=self.password, state="readonly", font=("Consolas", 11))
        self.entry.grid(row=4, column=1, sticky="ew", pady=4)
        ttk.Button(self, text="Copy", command=self.copy).grid(row=4, column=2, padx=(6, 0), pady=4)

        ttk.Checkbutton(self, text="Show password", variable=self.show, command=self.toggle).grid(
            row=5, column=1, sticky="w")

        ttk.Label(self, textvariable=self.strength_text).grid(row=6, column=0, columnspan=2, sticky="w", pady=(10, 2))
        self.bar = ttk.Progressbar(self, maximum=100)
        self.bar.grid(row=7, column=0, columnspan=3, sticky="ew")

        ttk.Separator(self).grid(row=8, column=0, columnspan=3, sticky="ew", pady=(12, 4))
        ttk.Label(self, textvariable=self.status).grid(row=9, column=0, columnspan=3, sticky="w")

    def generate(self):
        try:
            n = int(self.length.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Invalid length", "Please enter only numeric values.")
            return
        if n <= 0:
            messagebox.showerror("Invalid length", "Please enter a positive number.")
            return

        sets = []
        if self.upper.get():
            sets.append(UPPER)
        if self.lower.get():
            sets.append(LOWER)
        if self.numbers.get():
            sets.append(DIGITS)
        if self.special.get():
            sets.append(SPECIAL)
        if not sets:
            messagebox.showwarning("No character type", "Please select at least one character type.")
            return
        if n < len(sets):
            messagebox.showwarning("Length too short",
                                   f"Length must be at least {len(sets)} to include every selected type.")
            return

        pool = "".join(sets)
        chars = [secrets.choice(s) for s in sets]            # one of each selected type
        chars += [secrets.choice(pool) for _ in range(n - len(chars))]
        secrets.SystemRandom().shuffle(chars)

        self.password.set("".join(chars))
        self.update_strength(n * math.log2(len(pool)))
        name = self.user.get().strip()
        self.status.set(f"Password generated for {name}." if name else "Password generated.")

    def update_strength(self, bits):
        if bits < 40:
            label = "Weak"
        elif bits < 60:
            label = "Fair"
        elif bits < 80:
            label = "Strong"
        else:
            label = "Very strong"
        self.strength_text.set(f"Strength: {label} ({round(bits)} bits)")
        self.bar["value"] = min(100, bits / 1.2)

    def toggle(self):
        self.entry.config(show="" if self.show.get() else "*")

    def copy(self):
        if not self.password.get():
            self.status.set("Nothing to copy. Generate a password first.")
            return
        self.clipboard_clear()
        self.clipboard_append(self.password.get())
        self.status.set("Password copied to clipboard.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    root.minsize(460, 330)
    App(root)
    root.mainloop()