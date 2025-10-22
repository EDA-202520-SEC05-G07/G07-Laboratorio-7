from DataStructures.Map import map_entry as me

def new_map(num_elements=10, load_factor=0.5):
    capacity = int(num_elements / load_factor)
    map_struct = {
        'table': [None] * capacity,
        'capacity': capacity,
        'size': 0,
        'load_factor': load_factor
    }
    return map_struct
def hash_function(key, capacity):
    """
    Calcula el índice hash de una llave.
    """
    return abs(hash(key)) % capacity


def rehash(map_struct):
    """
    Duplica la capacidad del mapa y reubica los elementos.
    """
    old_table = map_struct['table']
    new_capacity = map_struct['capacity'] * 2
    map_struct['table'] = [None] * new_capacity
    map_struct['capacity'] = new_capacity
    map_struct['size'] = 0

    for entry in old_table:
        if entry is not None:
            put(map_struct, me.get_key(entry), me.get_value(entry))

def put(map_struct, key, value):
    """
    Inserta o actualiza un par (key, value) en el mapa.
    """
    index = hash_function(key, map_struct['capacity'])
    initial_index = index

    while map_struct['table'][index] is not None:
        current_entry = map_struct['table'][index]
        if me.get_key(current_entry) == key:
            # Si la llave ya existe, se actualiza el valor
            current_entry['value'] = value
            return
        index = (index + 1) % map_struct['capacity']
        if index == initial_index:
            raise Exception("El mapa está lleno")
    entry = me.new_map_entry(key, value)
    map_struct['table'][index] = entry
    map_struct['size'] += 1
    if (map_struct['size'] / map_struct['capacity']) > map_struct['load_factor']:
        rehash(map_struct)


def get(map_struct, key):

    index = hash_function(key, map_struct['capacity'])
    initial_index = index

    while map_struct['table'][index] is not None:
        entry = map_struct['table'][index]
        if me.get_key(entry) == key:
            return me.get_value(entry)
        index = (index + 1) % map_struct['capacity']
        if index == initial_index:
            break
    return None


def remove(map_struct, key):
    """
    Elimina una llave del mapa.
    """
    index = hash_function(key, map_struct['capacity'])
    initial_index = index

    while map_struct['table'][index] is not None:
        entry = map_struct['table'][index]
        if me.get_key(entry) == key:
            map_struct['table'][index] = None
            map_struct['size'] -= 1
            return
        index = (index + 1) % map_struct['capacity']
        if index == initial_index:
            break


def size(map_struct):
    """
    Retorna el número de elementos del mapa.
    """
    return map_struct['size']


def is_empty(map_struct):
    """
    Retorna True si el mapa está vacío.
    """
    return map_struct['size'] == 0
