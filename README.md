# classical-genetic-algorithm
Implementation of the classical genetic algorithm

### Install dependencies
```bash
pip3 install -r requirements.txt
```

### Run the genetic algorithm GUI
`python main.py`

### Run hyperparameter search
Choose the function which hyperparameters you want to search and define the search space in the `source/config/functions/[function].yaml` file (or add your own function). 
Then run the following command:<br>
`python search.py functions=[function]`

### Used benchmarks
- https://gitlab.com/luca.baronti/python_benchmark_functions
- https://github.com/thieu1995/opfunu/tree/master <br>
Van Thieu, N. (2024). Opfunu: An Open-source Python Library for Optimization Benchmark Functions. Journal of Open Research Software, 12(1), 8. https://doi.org/10.5334/jors.508
