# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer into a list


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine
temperatures = [0, 40, 100]
converted = []

