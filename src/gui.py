#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter


def sikumim_page(window):
    widgets = window.pack_slaves()
    for widget in widgets:
        widget.destroy()
    window.mainloop()


def main():
    window = Tkinter.Tk()
    sikumim = u"סיכומים"
    sikumim_button = Tkinter.Button(window, text=sikumim[::-1], command=lambda: sikumim_page(window)).pack()
    window.mainloop()


if __name__ == "__main__":
    main()