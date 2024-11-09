# classical-genetic-algorithm
Implementation of the classical genetic algorithm

### Install dependencies
```bash
pip3 install -r requirements.txt
```

### Run the genetic algorithm GUI
```bash
python main.py
```
After running the command, a window will pop up where you can set the hyperparameters of the genetic algorithm and run it. 
The GUI will display the solution found in the last generation and the time it took to find it.
After the algorithm finishes, the data and plots of the: 
- target function value from the best individual in each generation, 
- average target function value in each generation,
- standard deviation of the target function value in each generation.

You can find in the `generated_data` folder.

### Run hyperparameter search
Choose the function which hyperparameters you want to search and define the search space in the `source/config/functions/[function].yaml` file (or add your own function). 
Then run the following command:
```bash
python search.py functions=[function]
```
Or run for multiple functions at once:
```bash
python search.py -m functions=[function1],[function2],...
```
Optuna will search for the best hyperparameters for the genetic algorithm and save the results in the database located in `db/functions.db` file.


### Used benchmarks
- https://gitlab.com/luca.baronti/python_benchmark_functions
- https://github.com/thieu1995/opfunu/tree/master <br>
Van Thieu, N. (2024). Opfunu: An Open-source Python Library for Optimization Benchmark Functions. Journal of Open Research Software, 12(1), 8. https://doi.org/10.5334/jors.508
