# Modifying a list in a function

# When you pass a list to a function, the function can modify the list.
# Any changes made to the list inside the function’s body are permanent,
# allowing you to work efficiently even when you’re dealing with large amounts of data.

# Start with designs that need to be printed

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed designs
print(f"\nThe following models have been completed:")
for completed_model in completed_models:
   print(f"\t{completed_model}")

# This code can be reorganised by writing two functions
# First function prints the designs; the second will summarise the prints


def print_models(designs_unprinted, models_completed):
    """
    Simulate printing to each design, until none are left.
    Move each design to completed_models after printing.
    """
    while designs_unprinted:
        design_current = designs_unprinted.pop()
        print(f"Printing model: {design_current}")
        models_completed.append(design_current)


def show_completed_models(models_completed):
    """Show all the designs that were printed."""
    print(f"\nThe following designs have been completed:")
    for model_completed in models_completed:
        print(f"\t{model_completed}")


designs_unprinted = ['phone case', 'robot pendant', 'dodecahedron']
models_completed = []

print_models(designs_unprinted, models_completed)
show_completed_models(models_completed)


# If we need to print more designs in the future then we simply call print_models() again


# Preventing a function from modifying a list
# To do this, pass the function a copy of the list
# The function therefore only affects the copy of the list
# Send a copy of the list by doing --- > function_name(list_name[:])
# If we didn't want to empty the list in the last program we would do this:
# print_models(designs_unprinted[:], models_completed)


designs_unprinted = ['phone case', 'robot pendant', 'dodecahedron']
models_completed = []

print_models(designs_unprinted[:], models_completed)
show_completed_models(models_completed)

print(designs_unprinted)    # As you can see, the list was not affected but it still did the job
