# # List of models that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Loop to print each model one by one from the list
# # After printing each model, the model is moved to the list of completed_models
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # List of printed models
# print("\nThe following models have been printed:")
# for _ in completed_models:
#     print(_)


def print_models(unprinted_designs, completed_models):
    # Loop to print each model one by one from the list
    # After printing each model, the model is moved to the list of completed_models
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")

        completed_models.append(current_design)

def show_completed_models(completed_models):
    # List of printed models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# List of models that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# [:] create a copy of the unprinted_designs list
print_models(unprinted_designs[:], completed_models)
# print(unprinted_designs)
# print(completed_models)
show_completed_models(completed_models)