# Training on Say hello! (7kyu)

def greet(name):
    if (name == "") or (name == None):  # Make sure that the input is correct
        return None
    else:
        return f"hello {name}!"  # Return the greeting
