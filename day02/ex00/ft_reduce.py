def ft_reduce(function_to_apply, list_of_inputs):
    item = list_of_inputs[0]
    for next_item in list_of_inputs[1:]:
        item = function_to_apply(item, next_item)
    return item
