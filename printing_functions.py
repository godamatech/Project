def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_model  = unprinted_designs.pop()
		print(f"Printing Model: {current_model}")
		completed_models.append(current_model)


def show_completed_models(completed_models):
	for completed_model in completed_models:
		print(completed_model)
