# Remove duplicates from a list (8kyu)

def distinct(seq):
    no_duplicates = []  # Create an empty list
    for i in seq:  # Iterate the given list
        if i not in no_duplicates:  # Make sure to append elements that aren't already in our list
            no_duplicates.append(i)
        else:  # If the element is in the list we keep going
            continue
    return no_duplicates  # Return the list without duplicates
