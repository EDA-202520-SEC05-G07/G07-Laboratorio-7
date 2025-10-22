def new_list():
    return {'elements': []}

def add_last(lst, element):
    lst['elements'].append(element)


def size(lst):
    return len(lst['elements'])


def get_element(lst, position):
    return lst['elements'][position - 1]


def is_empty(lst):
    return len(lst['elements']) == 0


def sub_list(lst, start, end):
    return {'elements': lst['elements'][start - 1:end]}


def iterator(lst):
    return iter(lst['elements'])
