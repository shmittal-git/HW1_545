
1. extract_parameter.py file can be run on the terminal by calling:
>python  #for activating python environment.

2. Once you are in python environment, call the following command to run the function:
>extract_parameter("distillation", "humidity", 1)

3. Now you can define molecular weights and solutions_needed variables:
>molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

> solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']


4. You can run calculate_solution_weights.py file by:
> calculate_solution_weights(molecular_weights, solutions_needed)
