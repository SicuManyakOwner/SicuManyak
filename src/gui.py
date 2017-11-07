#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter


WINDOW = Tkinter.Tk()


def clean_page(window, location):
    """Cleans the window of modules to prepare for a new page"""
    widgets = window.grid_slaves()
    for widget in widgets:
        widget.destroy()
    if location == "sikumim":
        sikumim_page(window)
    elif location == "premium":
        premium_page(window)
    elif location == "main":
        main(window)


def sikumim_page(window):
    """Opens the sikumim page"""
    window.title(u"סיכומים")
    Tkinter.Label(window, text=u"סיכומים"[::-1]).grid(row=1, column=1)
    Tkinter.Button(WINDOW, text=u"חזרה למסך הראשי"[::-1],
                   command=lambda: clean_page(WINDOW, "main")).grid(row=2, column=1)
    window.mainloop()


def premium_page(window):
    """Open the "Buy Premium" page"""
    window.title(u"קנה פרמיום")
    Tkinter.Label(window, text=u"קנה פרמיום"[::-1]).grid(row=1, column=1)
    Tkinter.Button(WINDOW, text=u"חזרה למסך הראשי"[::-1],
                   command=lambda: clean_page(WINDOW, "main")).grid(row=2, column=1)
    window.mainloop()


def main(window):
    window.title(u"ברוכים הבאים לסיכומניאק!")
    sikumim = u"סיכומים"
    premium = u"קנה פרמיום"
    Tkinter.Button(window, text=sikumim[::-1],
                   command=lambda: clean_page(window, "sikumim")).grid(row=1, column=1)
    Tkinter.Button(window, text=premium[::-1], fg="#ff0000",
                   command=lambda: clean_page(window, "premium")).grid(row=2, column=1)
    WINDOW.mainloop()


if __name__ == "__main__":
    main(WINDOW)