from numpy import ndarray
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime


class GraphCreator:
    generated_data_folder = "generated_data"

    def create_graphs(self, fitness_values: ndarray, search_minimum: bool):
        generations = np.arange(1, fitness_values.shape[0] + 1)
        self.create_fitness_values_graph(generations, fitness_values, search_minimum)
        self.create_standard_deviation_graph(generations, fitness_values)

    def create_fitness_values_graph(self, generations: ndarray, fitness_values: ndarray, search_minimum: bool) -> None:
        if search_minimum:
            best_solutions = np.min(fitness_values, axis=1)
        else:
            best_solutions = np.max(fitness_values, axis=1)
        self.save_data(generations, best_solutions, "funkcja_celu_w_kolejnej_iteracji.txt")
        self.plot_data(generations, np.array([best_solutions]).reshape(-1, 1),
                       "Wykres zależności wartości funkcji celu od kolejnej iteracji",
                       "generacja",
                       ["wartość funkcji celu"],
                       "wykres_funkcji_celu_w_kolejnej_iteracji.png")

    def create_standard_deviation_graph(self, generations: ndarray, fitness_values: ndarray) -> None:
        std_fitness_values = np.std(fitness_values, axis=1)
        means = np.mean(fitness_values, axis=1)
        self.save_data(generations, std_fitness_values, "funkcja_odchylenia_standardowego.txt")
        self.save_data(generations, means, "średnie.txt")
        self.plot_data(generations, np.column_stack((std_fitness_values, means)),
                       "Wykres odchylenia standardowego i średniej w poszczególnych epokach",
                       "generacja",
                       ["odchylenie standardowe", "średnia"],
                       "wykres_funkcji_średniej_odchylenia.png")

    def save_data(self, x: ndarray, y: ndarray, filename: str) -> None:
        data = np.column_stack((x, y))
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'{current_time}_{filename}'
        np.savetxt(self.generated_data_folder+"/"+file_name, data, fmt='%d', header='x y', comments='')

    def plot_data(self, x: ndarray, y: ndarray, title: str, xlabel: str, ylabel: str, filename: str) -> None:
        plt.figure()
        for i in range(len(y[0])):
            plt.plot(x, y[:, i], label=ylabel[i])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(", ".join(ylabel))
        plt.legend()
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        plt.savefig(self.generated_data_folder+"/"+current_time+"_"+filename)
