FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list
    to-do items.
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath=FILEPATH, ):
    """ write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# when you don't want anything on a module to be executed use:
if __name__ == "__main__":
    print("Hello")
    print(get_todos())