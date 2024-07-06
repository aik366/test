import customtkinter as ctk
import string
import random
from tkinter import messagebox


def pass_tkinter():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("339x197+700+300")
    root.resizable(False, False)
    root.title("Password Generator")

    def password(chars, number=1, letter=1, symbol=1):
        if not number and not letter and not symbol:
            return messagebox.showerror("Error", 'должен быть хотя бы один из: цифр, букв, знаков')
        number = string.digits if number else ''
        letter = string.ascii_letters if letter else ''
        symbol = string.punctuation if symbol else ''
        s = number + letter + symbol
        return ''.join(random.choices(s, k=chars))

    def generate():
        gen_password = password(int(myCombobox.get()), numbers_value.get(), letters_value.get(), symbols_value.get())
        if gen_password not in "ok":
            myEntry.delete(0, 'end')
            myEntry.insert(0, gen_password)

    def clear():
        myEntry.delete(0, 'end')

    myLabel = ctk.CTkLabel(root, text="Password Generator", font=("Arial", 20))
    myLabel.grid(row=0, column=0, pady=10, columnspan=3)

    myEntry = ctk.CTkEntry(root, placeholder_text="generate your password", width=230, font=("Arial", 14))
    myEntry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")

    myCombobox = ctk.CTkComboBox(root,
                                 values=["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", ],
                                 state="readonly", width=76, font=("Arial", 14))
    myCombobox.grid(row=1, column=2, pady=10, sticky="w")
    myCombobox.set("8")

    numbers_value = ctk.IntVar(value=1)
    numbersCheckBox = ctk.CTkCheckBox(root, text="Number", variable=numbers_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    numbersCheckBox.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    letters_value = ctk.IntVar(value=1)
    lettersCheckBox = ctk.CTkCheckBox(root, text="Letter", variable=letters_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    lettersCheckBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    symbols_value = ctk.IntVar(value=1)
    symbolsCheckBox = ctk.CTkCheckBox(root, text="Symbol", variable=symbols_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    symbolsCheckBox.grid(row=2, column=2, pady=10, sticky="w")

    runButton = ctk.CTkButton(root, text="Generate", command=generate, width=230, height=35, font=("Arial", 14))
    runButton.grid(row=3, column=0, padx=10, pady=10, sticky="w", columnspan=2)

    clearButton = ctk.CTkButton(root, text="Clear", command=clear, width=76, height=35, font=("Arial", 14))
    clearButton.grid(row=3, column=2, pady=10, sticky="w")

    root.mainloop()


if __name__ == '__main__':
    pass_tkinter()
