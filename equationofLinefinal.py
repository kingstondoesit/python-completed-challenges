def get_input(prompt, allow_zero=True):
    """
    Prompts the user for input, converts it to a float, and handles invalid or empty input.
    
    Parameters:
        prompt (str): The prompt message to display to the user.
        allow_zero (bool): Whether to allow zero as a valid input.
        
    Returns:
        float or None: The converted float value or None if input is empty.
    """
    while True:
        value = input(prompt).strip()
        if value == "":
            return None
        try:
            value = float(value)
            if not allow_zero and value == 0:
                print("Slope (m) cannot be zero. Please provide a valid number or leave blank.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number or leave blank.")

def calculate_line():
    """
    Collects user inputs for the slope (m), y-intercept (c), and x-intercept (x0) to calculate
    the equation of a line in the form y = mx + c. 

    Returns:
        dict: A dictionary containing the line equation, slope, x-intercept, and y-intercept.
    """
    print("Please provide any two of the following values:")
    print("1. Slope (m)")
    print("2. Y-Intercept (c)")
    print("3. X-Intercept (x0)")
    print()

    while True:
        # Get user input for slope (m) and y-intercept (c)
        m = get_input("1. Enter the slope (m) if known (leave blank if unknown): ", allow_zero=False)
        c = get_input("2. Enter the y-intercept (c) if known (leave blank if unknown): ")
        
        # Determine if x0 is needed
        if m is not None and c is not None:
            # Both m and c are provided, no need for x0
            x0 = None
        elif m is not None or c is not None:
            # One of m or c is provided, need x0
            x0 = get_input("3. Enter the x-intercept (x0) if known (leave blank if unknown): ")
        else:
            # Neither m nor c is provided
            print("You need to provide exactly two values. At least one of m or c must be provided.")
            continue

        # Calculate the equation based on the provided variables
        if m is not None and c is not None:
            # Case 1: Both m and c provided
            equation = f"y = {m}x {'+' if c >= 0 else '-'} {abs(c)}"
            x_intercept = -c / m if m != 0 else 'undefined'

        elif m is not None and x0 is not None:
            # Case 2: m and x0 provided
            c = -m * x0
            equation = f"y = {m}x {'+' if c >= 0 else '-'} {abs(c)}"

        elif c is not None and x0 is not None:
            # Case 3: c and x0 provided
            m = -c / x0
            equation = f"y = {m}x {'+' if c >= 0 else '-'} {abs(c)}"

        else:
            # Incomplete data
            print("Incomplete data. Unable to determine the equation.")
            continue
        
        # Reassign c and x0 values
        y_intercept = c
        x_intercept = x0 if c is not None and c == 0 else -c / m if m is not None and m != 0 else None

        # Return the result
        return {
            "equation": equation,
            "slope": m,
            "x_intercept": x_intercept,
            "y_intercept": y_intercept
        }

# Main execution
result = calculate_line()
if isinstance(result, dict):
    print("Equation of the line:", result["equation"])
    print("Slope (m):", result["slope"])
    print("X-Intercept:", result["x_intercept"])
    print("Y-Intercept:", result["y_intercept"])
else:
    print(result)