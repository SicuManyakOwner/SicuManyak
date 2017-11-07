#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter


WINDOW = Tkinter.Tk()


def clean_page(window, location):
    widgets = window.pack_slaves()
    for widget in widgets:
        widget.destroy()
    if location == "sikumim":
        sikumim_page(WINDOW)
    elif location == "premium":
        premium_page(WINDOW)
    elif location == "main":
        main()


def sikumim_page(window):
    label1 = Tkinter.Label(window, text=u"סיכומים"[::-1]).pack()
    return_button = Tkinter.Button(WINDOW, text=u"חזרה למסך הראשי"[::-1], command=lambda: clean_page(WINDOW, "main")).pack()
    window.mainloop()


def premium_page(window):
    label1 = Tkinter.Label(window, text=u"קנה פרמיום"[::-1]).pack()
    return_button = Tkinter.Button(WINDOW, text=u"חזרה למסך הראשי"[::-1], command=lambda: clean_page(WINDOW, "main")).pack()
    window.mainloop()


def main():
    sikumim = u"סיכומים"
    premium = u"קנה פרמיום"
    sikumim_button = Tkinter.Button(WINDOW, text=sikumim[::-1], command=lambda: clean_page(WINDOW, "sikumim")).pack()
    premium_button = Tkinter.Button(WINDOW, text=premium[::-1], command=lambda: clean_page(WINDOW, "premium")).pack()
    WINDOW.mainloop()


if __name__ == "__main__":
    main()