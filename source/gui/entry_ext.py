from tkinter import *
from source.gui.common import *

class EntryExt(Entry):
    def __init__(self, master : Misc, text : str, entry_type : type = int) -> None:
        super().__init__(master,
                         bd=0,
                         relief="flat",
                         font=FONT(ENTRY_FONT_SIZE))
        self.__type = entry_type
        self.configure({
            "background": FG_COLOR,
            "foreground": BLACK,
            "highlightbackground": HL_BG_COLOR,
            "highlightthickness": "2",
            "highlightcolor": HL_COLOR,
        })
        self.insert(0, text)
        self.modified = False
        self.bind("<Key>", self.__first_time_entry)
        self.pack(padx=ENTRY_PADX, pady=ENTRY_PADY, ipady=ENTRY_IPADY)
        self.configure(width=ENTRY_WIDTH)

    def __first_time_entry(self, event : Event) -> None:
        if event.keysym == "Tab":
            return
        if event.widget == self and not self.modified:
            self.delete(0, END)
            self.modified = True

    @property
    def get_value(self) -> float | int | None:
        value = 0
        try:
            value = self.__type(self.get())
        except ValueError:
            self.focus()
            value = None
        finally:
            return value