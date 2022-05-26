def is_int(str):
    """Is string integer"""

    try:
        int(str)
        return True
    except ValueError:
        return False
