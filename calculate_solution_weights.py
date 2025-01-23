def calculate_solution_weights(molecular_weights, solutions_needed):
    #generating an empty list 
    modified_list = []
    #lopping through the solutions_needed 
    for solution in solutions_needed:
        # splitting the solution into the chemical name and concentration
        chemical, concentration = solution.split('-')
        concentration = float(concentration[:-1])  # Remove 'M' and convert to float
        if chemical in molecular_weights:
            weight = molecular_weights[chemical]*concentration*1000
            updated_sol = f'{chemical}-{concentration}M-{weight:.2f}g'
            modified_list.append(updated_sol)
        else:
            modified_list.append('unknown')
    return modified_list
        
    
