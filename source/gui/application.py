from tkinter import *
from tkinter.ttk import Style

import numpy as np

from source.gui.widget_builder import WidgetBuilder
from source.gui.common import *

class Application:
    def __init__(self) -> None:
        root = Tk()

        style = Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=GREY, background=GREY)

        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        ws = (ws / 2) - (WIDTH / 2)
        hs = (hs / 2) - (HEIGHT / 2)

        root.configure(background=BG_COLOR)
        root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, ws, hs))
        root.title("Classical genetic algorithm")
        root.bind("<Escape>", lambda e: e.widget.quit())
        root.focus_set()
        root.resizable(False, False)
        self.root = root

        label = Label(self.root, text="Configuration", font=FONT(LABEL_FONT_SIZE))
        label.configure({"background": BG_COLOR, "foreground": FG_COLOR})
        label.pack(pady=LABEL_PADY)

        self.__range_start = WidgetBuilder.create_entry(self.root, "Interval start = a", float)
        self.__range_end = WidgetBuilder.create_entry(self.root, "Interval end = b", float)
        self.__population_count = WidgetBuilder.create_entry(self.root, "Population size")
        self.__number_of_variables = WidgetBuilder.create_entry(self.root, "Number of variables")
        self.__bits_count = WidgetBuilder.create_entry(self.root, "Bits per chromosome (precision)")
        self.__epoch_count = WidgetBuilder.create_entry(self.root, "Number of generations")
        self.__individuals_best = WidgetBuilder.create_entry(self.root, "Number of individuals (best / tournament)")
        self.__individuals_elite = WidgetBuilder.create_entry(self.root, "Number of individuals (elite)")

        self.__cross_prob = WidgetBuilder.create_entry(self.root, "Cross probability", float)
        self.__mutation_prob = WidgetBuilder.create_entry(self.root, "Mutation probability", float)
        self.__inversion_prob = WidgetBuilder.create_entry(self.root, "Inversion probability", float)

        self.__selection_var = StringVar()
        self.__cross_var = StringVar()
        self.__mutation_var = StringVar()
        self.__selection_strategy = WidgetBuilder.create_combobox(self.root, SELECTION_STRATEGY, self.__selection_var)
        self.__cross_method = WidgetBuilder.create_combobox(self.root, CROSS_STRATEGY, self.__cross_var)
        self.__mutation_method = WidgetBuilder.create_combobox(self.root, MUTATION_STRATEGY, self.__mutation_var)

        self.__is_minimize_var = BooleanVar()
        self.__is_minimize = WidgetBuilder.create_checkbox(self.root, "Find mimimum of the function", self.__is_minimize_var)

        self.button_start = WidgetBuilder.create_button(self.root, "Start")

    def start(self) -> None:
        self.root.mainloop()

    def get_algorithm_config(self) -> dict:
        res = dict()
        res['start_interval'] = self.__range_start.get_value
        res['end_interval'] = self.__range_end.get_value
        res['population_size'] = self.__population_count.get_value
        res['number_of_variables'] = self.__number_of_variables.get_value
        res['bits_count'] = self.__bits_count.get_value
        res['generations'] = self.__epoch_count.get_value
        res['individuals_best'] = self.__individuals_best.get_value
        res['individuals_elite'] = self.__individuals_elite.get_value
        res['cross_prob'] = self.__cross_prob.get_value
        res['mutation_prob'] = self.__mutation_prob.get_value
        res['inversion_prob'] = self.__inversion_prob.get_value
        res['selection_strategy'] = STRATEGY(self.__selection_var.get())
        res['cross_strategy'] = STRATEGY(self.__cross_var.get())
        res['mutation_strategy'] = STRATEGY(self.__mutation_var.get())
        res['search_minimum'] = self.__is_minimize_var.get()
        return res

    def popup(self, time_elapsed : float, value : float, representation : np.ndarray) -> None:
        popup = Toplevel(self.root)
        popup.configure(background=FG_COLOR)
        h = HEIGHT // 2
        ws = (self.root.winfo_screenwidth() / 2) - (WIDTH / 2)
        hs = (self.root.winfo_screenheight() / 2) - (h / 2)
        popup.geometry("%dx%d+%d+%d" % (WIDTH, h, ws, hs))
        popup.title("Result")
        popup.resizable(False, False)

        Label(popup, text=f"f(x) = {value}", font=FONT(LABEL_FONT_SIZE)).pack(pady=5)
        Label(popup, text=f"time = {time_elapsed:.2f} sec", font=FONT(LABEL_FONT_SIZE)).pack(pady=5)
        Label(popup, text=f"Best ind values = {representation}", font=FONT(LABEL_FONT_SIZE)).pack(pady=5)
        button = WidgetBuilder.create_button(popup, "OK")
        button.config(command=popup.destroy)
        button.focus_set()