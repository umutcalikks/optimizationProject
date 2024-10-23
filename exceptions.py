class ArgumentError(Exception):

    def __init__(self, hint: str = ""):
        super().__init__(f"ArgumentError: Invalid argument entry{': ' + hint if hint else '.'}")

