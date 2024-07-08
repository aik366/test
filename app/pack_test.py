import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("+600+350")


def pack_forget():
    frame3.pack_forget()


def pack():
    frame3.pack(side="left", padx=10, pady=10, fill="both", expand=True)


frame1 = ctk.CTkFrame(app, fg_color="red", width=400, height=400)
frame1.pack(side="left", padx=10, pady=10, fill="both", expand=True)
button1 = ctk.CTkButton(frame1, command=pack_forget)
button1.pack(padx=20, pady=20)

frame2 = ctk.CTkFrame(app, fg_color="green", width=400, height=400)
frame2.pack(side="left", padx=10, pady=10, fill="both", expand=True)
button2 = ctk.CTkButton(frame2, command=pack)
button2.pack(padx=20, pady=20)

frame3 = ctk.CTkFrame(app, fg_color="blue", width=400, height=400)
frame3.pack(side="left", padx=10, pady=10, fill="both", expand=True)
button3 = ctk.CTkButton(frame3)
button3.pack(padx=20, pady=20)

if __name__ == '__main__':
    app.mainloop()
