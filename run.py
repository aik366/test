from app import pass_tkinter, password, grid_test


# print(password(12, symbol=False))
# pass_tkinter()
def func():
    if ignor.entry3.get() == "5":
        ignor.frame1.forget()
    elif ignor.entry3.get() == "4":
        ignor.frame1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="NSEW")



ignor.button3.configure(fg_color=ignor.button1.cget("fg_color"))
ignor.button3.configure(command=func)

ignor.app.mainloop()
