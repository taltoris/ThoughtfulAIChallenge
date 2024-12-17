def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts packages into STANDARD, SPECIAL, or REJECTED stacks based on volume and mass.

    Args:
    width (float): The width of the package in cm.
    height (float): The height of the package in cm.
    length (float): The length of the package in cm.
    mass (float): The mass of the package in kg.

    Returns:
    str: The name of the stack where the package should be dispatched.
    """

    # Calculate the volume of the package
    volume = width * height * length

    # Check if the package is bulky
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])

    # Check if the package is heavy
    is_heavy = mass >= 20

    # Determine the stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example usage
print(sort(100, 100, 100, 10))  # STANDARD
print(sort(150, 100, 100, 10))  # SPECIAL
print(sort(100, 100, 100, 20))  # SPECIAL
print(sort(200, 200, 200, 30))  # REJECTED
