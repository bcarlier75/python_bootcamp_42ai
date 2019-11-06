def ft_map(function_to_apply, list_of_inputs):
    result = []
    for x in list_of_inputs:
        result.append(function_to_apply(x))
    return result
