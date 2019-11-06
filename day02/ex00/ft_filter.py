def ft_filter(function_to_apply, list_of_inputs):
    if not list_of_inputs:
        return []
    if function_to_apply is not None:
        return [x for x in list_of_inputs if function_to_apply(x)]
    elif function_to_apply is None:
        return [x for x in list_of_inputs if function_to_apply is None]
