
def print_grid(grid_size, grid_qty):
    """
    Generate a grid with specified cell size and cell quantity
    :param grid_size: integer
    :param grid_qty: integer
    :return: none
    """

    total_size = ((grid_size +1) * grid_qty) + 1
    i = 0
    while i < total_size:
        if i % (grid_size +1) == 0 or i == (total_size -1):
            grid_square = "+{}".format('-' * grid_size)
            print("{}+".format(grid_square * grid_qty))
        else:
            grid_square = "|{}".format(' ' * grid_size)
            print("{}|".format(grid_square * grid_qty))
        i += 1


grid_size = input("Cell size: ")
grid_qty = input("Cell quantity: ")
print_grid(grid_size, grid_qty)
