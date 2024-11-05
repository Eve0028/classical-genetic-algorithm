from source.gui.common import (ENTRY_PADY, ENTRY_FONT_SIZE, FONT,
                               COMBOBOX_WIDTH, FG_COLOR, BLACK, BG_COLOR)
from source.gui.entry_ext import EntryExt
from tkinter import Misc, Button, StringVar, BooleanVar, Checkbutton
from tkinter import ttk


class WidgetBuilder:
    @staticmethod
    def create_entry(master : Misc, text : str, entry_type : type = int) -> EntryExt:
        return EntryExt(master, text, entry_type)

    @staticmethod
    def create_checkbox(master : Misc, text : str, checkbox_var : BooleanVar) -> Checkbutton:
        checkbox = Checkbutton(master,
                         text=text,
                         font=FONT(ENTRY_FONT_SIZE),
                         variable=checkbox_var,
                         onvalue=True, offvalue=False,
                         width=COMBOBOX_WIDTH)
        checkbox.pack(pady=ENTRY_PADY)
        checkbox.configure({
            "background": BG_COLOR,
            "foreground": FG_COLOR,
            "selectcolor": BG_COLOR,
            "activebackground": BG_COLOR,
            "activeforeground": FG_COLOR
        })
        return checkbox

    @staticmethod
    def create_combobox(master : Misc, values : list, value : StringVar) -> ttk.Combobox:
        combobox = ttk.Combobox(master,
                         width=COMBOBOX_WIDTH,
                         textvariable=value,
                         font=FONT(ENTRY_FONT_SIZE))
        combobox.configure({"background": FG_COLOR, "foreground": BLACK})
        combobox['values'] = values
        combobox['state'] = "readonly"
        combobox.current(0)
        combobox.pack(pady=ENTRY_PADY, ipady=3)
        return combobox

    @staticmethod
    def create_button(master : Misc, text : str) -> Button:
        button = Button(master, text=text,
                        font=FONT(ENTRY_FONT_SIZE),
                        width=COMBOBOX_WIDTH)
        button.pack(pady=ENTRY_PADY)
        return button