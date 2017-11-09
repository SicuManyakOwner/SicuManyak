# -*- coding: utf-8 -*-

from Tkinter import *
import contact_server

WINDOW = Tk()


def clean_page(location):
    """Cleans the window of modules to prepare for a new page"""
    widgets = WINDOW.grid_slaves()
    for widget in widgets:
        widget.destroy()
    if location == "sikumim":
        sikumim_page()
    elif location == "premium":
        premium_page()
    elif location == "login":
        login_page()
    elif location == "main":
        main()


def login_page():
    """Opens the login page"""
    WINDOW.title(u"התחבר")
    username = StringVar()
    Entry(WINDOW, text=u"שם משתמש"[::-1], textvariable=username, width=26).grid(row=1, column=1, columnspan=2)
    Button(WINDOW, text=u"שלח נתונים"[::-1], command=lambda: contact_server.create_socket(0)).grid(row=2, column=2)
    Button(WINDOW, text=u"חזרה למסך הראשי"[::-1],
           command=lambda: clean_page("main")).grid(row=2, column=1)


def sikumim_page():
    """Opens the sikumim page"""
    WINDOW.title(u"סיכומים")
    Label(WINDOW, text=u"סיכומים"[::-1]).grid(row=1, column=1)
    Button(WINDOW, text=u"חזרה למסך הראשי"[::-1],
           command=lambda: clean_page("main")).grid(row=2, column=1)
    WINDOW.mainloop()


def premium_page():
    """Open the "Buy Premium" page"""
    WINDOW.title(u"קנה פרמיום")
    Label(WINDOW, text=u"קנה פרמיום"[::-1]).grid(row=1, column=1)
    Button(WINDOW, text=u"חזרה למסך הראשי"[::-1],
           command=lambda: clean_page("main")).grid(row=2, column=1)
    WINDOW.mainloop()


def main():
    WINDOW.geometry('225x200')
    WINDOW.title(u"ברוכים הבאים לסיכומניאק!")
    login = u"התחבר"
    sikumim = u"סיכומים"
    premium = u"קנה פרמיום"
    Button(WINDOW, text=login[::-1],
           command=lambda : clean_page("login")).grid(row=1,column=1)
    Button(WINDOW, text=sikumim[::-1],
           command=lambda: clean_page("sikumim")).grid(row=1, column=2)
    Button(WINDOW, text=premium[::-1], fg="#ff0000",
           command=lambda: clean_page("premium")).grid(row=1, column=3)
    WINDOW.mainloop()


if __name__ == "__main__":
    main()