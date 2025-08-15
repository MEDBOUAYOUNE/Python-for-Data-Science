def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for multiple individuals based on lists of height (in meters) and weight (in kg).
    Args:
        height: List of heights in meters
        weight: List of weights in kilograms
    Returns:
        List of BMI values (kg/m^2)
    Raises:
        AssertionError: If lists are not equal length or not contain int or float
    """
    try:
        assert len(height) == len(weight), "Assertion error: lists are not equal length."
        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)) and isinstance(w, (int, float)), (
                "Assertion error: all values must be numbers"
                )
            assert h > 0 and w > 0, "Assertion error: height and weight must be positive values"
        return [weight[index] / (height[index] * height[index]) for index in range(len(height))]
    except AssertionError as error:
        print(error)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check for the Boday Mass Index limit based on a bmi list and a limit
    Args:
        bmi: List of bmi (kg/m^2)
        limit: an intger
    Returns:
        boolean list
    Raises:
        AssertionError: If list contains !int or !float.
    """
    try:
        for individual_bmi in bmi:
            assert isinstance(individual_bmi, (int, float)), "Assertion error: all values must be numbers."
        return [bmi[index] > limit for index in range(len(bmi))]
    except AssertionError as error:
        print(error)
