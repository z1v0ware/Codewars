# Remove duplicates from a list

def distinct(seq):
    no_duplicates = []
    for i in seq:
        if i not in no_duplicates:
            no_duplicates.append(i)
        else:
            continue
    return no_duplicates
