#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
def sikumim_page():
    pass

def main():
    window = Tkinter.Tk()
    sikumim = u"סיכומים"
    Tkinter.Button(window, text=sikumim[::-1], command = sikumim_page()).pack()
    window.mainloop()


if __name__ == "__main__":
    main()