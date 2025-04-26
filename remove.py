# Removing elements (8kyu)

def remove_every_other(my_list):
    new_list = []  # Create an empty list
    for i in range(0, len(my_list), 2):
        new_list.append(my_list[i])  # Append only the elements with even index
    return new_list
