def find_max_min(my_list = None):
    """ This function takes a list of numbers, and returns an array containing
    the min and max number, respectively, or its length if all the list items
     are of the same value.
    First the input is confirmed to be list.
    The list is then checked to ensure it is none empty and that all its items
     are numbers.
     An appropriate responce is returned for all these senarios.
    """
    if my_list is None:
        return "Please enter a list of numbers"
    
    if not isinstance(my_list, list):
        return "Only lists allowed "
    
    """A list of could numbers could be that of a mixture of the numbers i.e integers and floats.
    Checking to ensure it is only numbers is necessary. In this case, I would prefer just the floats and the integers, thus the list should only contaiin these two and the new list that is checked"""
    number_list = [item for item in my_list if isinstance(item, (int, float))]
    if not my_list == number_list:
        return "The argument list contains none digit item(s). "

    if max(my_list)==min(my_list):
        return [len(my_list)]
    return [ min(my_list), max(my_list) ]