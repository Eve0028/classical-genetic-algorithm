from tkinter import *
from tkinter.ttk import Style

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

        self.__range_start = WidgetBuilder.create_entry(self.root, "Range start = a")
        self.__range_end = WidgetBuilder.create_entry(self.root, "Range end = b")
        self.__population_count = WidgetBuilder.create_entry(self.root, "Population count")
        self.__bits_count = WidgetBuilder.create_entry(self.root, "Bits per chromosome")
        self.__epoch_count = WidgetBuilder.create_entry(self.root, "Epochs number")
        self.__individuals_best = WidgetBuilder.create_entry(self.root, "Number of individuals (best / tournament)")
        self.__individuals_elite = WidgetBuilder.create_entry(self.root, "Number of individuals (elite)")

        self.__cross_prob = WidgetBuilder.create_entry(self.root, "Cross probability", float)
        self.__mutation_prob = WidgetBuilder.create_entry(self.root, "Mutation probability", float)
        self.__inversion_prob = WidgetBuilder.create_entry(self.root, "Inversion probability", float)

        self.__selection_strategy = WidgetBuilder.create_combobox(self.root, SELECTION_STRATEGY)
        self.__cross_method = WidgetBuilder.create_combobox(self.root, CROSS_STRATEGY)
        self.__mutation_method = WidgetBuilder.create_combobox(self.root, MUTATION_STRATEGY)

        self.__is_minimize = WidgetBuilder.create_checkbox(self.root, "Find mimimum of the function")

        self.__button_start = WidgetBuilder.create_button(self.root, "Start")
        self.__button_start.config(command=self.start_algorithm)

    def start(self) -> None:
        self.root.mainloop()

    def start_algorithm(self) -> None:
        # TODO: get values from controls
        #       start timer
        #       pass configuration to genetic algorithm
        #       calculate
        #       stop timer -> create popup window with result and time
        #       generate graphs / statistics
        pass


app = Application()
app.start()