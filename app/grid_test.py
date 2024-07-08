import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("500x500+600+350")

app.grid_columnconfigure((0, 1), weight=1, uniform='a')
app.grid_rowconfigure((0, 1), weight=1, uniform='a')


def color_button(button, fg_color, hover_color):
    button.configure(fg_color=fg_color, hover_color=hover_color)


def func():
    if entry3.get() == "5":
        frame1.grid_forget()
        frame2.grid_forget()
        frame3.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="NSEW")
        frame4.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="NSEW")
    elif entry3.get() == "4":
        frame1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="NSEW")
        frame2.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="NSEW")
        frame3.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="NSEW")
        frame4.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="NSEW")


frame1 = ctk.CTkFrame(app, fg_color="#473363")
frame1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="NSEW")
label1 = ctk.CTkLabel(frame1, text="frame1 label", font=("Arial", 30))
label1.pack(pady=10)
entry1 = ctk.CTkEntry(frame1, placeholder_text="frame1 entry", height=40)
entry1.pack(pady=10)
button1 = ctk.CTkButton(frame1, text="frame1 button", height=40)
button1.pack(pady=10)

frame2 = ctk.CTkFrame(app, fg_color="#6C0D49")
frame2.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="NSEW")
label2 = ctk.CTkLabel(frame2, text="frame2 label", font=("Arial", 30))
label2.pack(pady=10)
entry2 = ctk.CTkEntry(frame2, placeholder_text="frame2 entry", height=40)
entry2.pack(pady=10)
button2 = ctk.CTkButton(frame2, text="frame2 button", height=40)
button2.pack(pady=10)

frame3 = ctk.CTkFrame(app, fg_color="#525BD2")
frame3.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="NSEW")
label3 = ctk.CTkLabel(frame3, text="frame3 label", font=("Arial", 30))
label3.pack(pady=10)
entry3 = ctk.CTkEntry(frame3, placeholder_text="frame3 entry", height=40)
entry3.pack(pady=10)
button3 = ctk.CTkButton(frame3, text="frame3 button", height=40, command=func)
button3.pack(pady=10)

frame4 = ctk.CTkFrame(app, fg_color="#D56C2C")
frame4.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="NSEW")
label4 = ctk.CTkLabel(frame4, text="frame4 label", font=("Arial", 30))
label4.pack(pady=10)
entry4 = ctk.CTkEntry(frame4, placeholder_text="frame4 entry", height=40)
entry4.pack(pady=10)
button4 = ctk.CTkButton(frame4, text="frame4 button", height=40)
button4.pack(pady=10)

color_button(button1, "#56743D", "#718C35")
color_button(button4, "#D4126B", "#C10BAB")

if __name__ == '__main__':
    app.mainloop()
