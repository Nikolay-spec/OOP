some_item
list_of_items


class ProductAlreadyExists:
    if some_item in list_of_items:
        raise IndexError('Item already exists')

