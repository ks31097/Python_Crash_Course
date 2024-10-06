from module_printing_models import print_models, show_completed_models

# List of models that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# [:] create a copy of the unprinted_designs list
print_models(unprinted_designs[:], completed_models)
# print(unprinted_designs)
# print(completed_models)
show_completed_models(completed_models)