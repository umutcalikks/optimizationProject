import numpy as np
from typing import Callable, Union, List
from exceptions import *

phi = 0.61803398875

FUNC_ARGS = Union[int, float, list, tuple, np.ndarray]
NUMBER = Union[int, float]

class Extremum:

    def __init__(self, x, method: str):
        self.value = x
        self.label = f"Extremum(at: '{x}', method: '{method}')"

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label

    def get(self):
        return self.value

class Optimizer:
    """
        A general purpose wrapper class for optimizing any function.
        Includes several methods, holds gathered extrema information.
    """

    def __init__(self, f: Callable, label: str = "Function f", alpha: NUMBER = 0.001, h=1e-05):
        self.f = f
        self.label = label
        self.h = h  # Pass in a default h to calculate derivatives. This may be an ndarray if you wish.
        self.alpha = alpha  # General purpose learning rate.
        self.found: List[Extremum] = []

    def __str__(self):
        return f"Optimizer: {self.label}"

    def __repr__(self):
        return f"Optimizer: {self.label}"

    def clear(self):
        """
            Clears the internal extrema list.
        """
        self.found.clear()

    def calculate(self, x: FUNC_ARGS):
        """
            Evaluates wrapped functions value at x.

            Args:
                x : The value to evaluate the function at. The
                    function may have more than one argument.
                    In that case, pass in as Union[list, tuple,
                    numpy.ndarray]

            Returns:
                f of x.
        """
        if isinstance(x, NUMBER):
            return self.f(x)
        elif isinstance(x, Union[list, tuple, np.ndarray]):
            return self.f(*x)  # Applies variable unpacking
        raise ArgumentError("Invalid type: int | float | list | tuple | numpy.ndarray")

    def derivative(self, x: FUNC_ARGS, h=None):
        """
            Evaluates the derivative of the wrapped function at x.

            Args:
                x : The value to evaluate the derivative at. The
                    function may have more than one argument.
                    In that case, pass in as Union[list, tuple,
                    numpy.ndarray]
                h : The limit parameter. Defaults to 1e-05.

            Returns:
                Derivative of f of x.
        """
        if h is None:
            h = self.h
        return (self.calculate(x + h) - self.calculate(x - h)) / (2 * h)

    def second_derivative(self, x: FUNC_ARGS, h=None):
        """
            Evaluates the derivative of the wrapped function at x.

            Args:
                x : The value to evaluate the derivative at. The
                    function may have more than one argument.
                    In that case, pass in as Union[list, tuple,
                    numpy.ndarray]
                h : The limit parameter. Defaults to 1e-05.

            Returns:
                Second derivative of f of x.
        """
        return (self.calculate(x + h) - 2 * self.calculate(x) + self.calculate(x - h)) / (h ** 2)

    def optimize(self, method: str = "newton", x: FUNC_ARGS = 0, iterations: int = 15, h=None, interval=None):
        """
            Optimizes the wrapped function given the method, and parameters.
            Parameters should be given exclusive to each method. Possible
            methods are "newton", "gradient" and "golden" corresponding to
            Newton-Raphson method, Gradient Descent and Golden Search in
            order.

            Args:
                method: Method to apply. Must be one of ["newton", "gradient", "golden"].
                    Defaults to "newton".
                x: Method specific x value to calculate the wrapped function.
                    If the method requires an initial value, it is the initial value.
                iterations: Total number of iterations to apply in the method
                    kernel. Defaults to 15.
                h: The h value to calculate derivatives with. Defaults to 1e-05.
                interval: The interval parameter to apply optimization on. Must be
                    a numpy.arange.

            Returns:
                Returns the calculated extremum point.
        """
        __method = method.lower()
        if __method == "newton":
            val = self.__newton(x, iterations, h)
            self.found.append(Extremum(val, "Newton-Raphson"))
            return val
        if __method == "gradient":
            val = self.__steepest_descent(x, iterations, h)
            self.found.append(Extremum(val, "Gradient Descent"))
            return val
        if __method == "golden":
            val = self.__golden_search(interval, iterations)
            self.found.append(Extremum(val, "Golden Search"))
            return val
        raise ArgumentError("Invalid choice: ['newton', 'gradient', 'golden']")

    def extrema(self):
        """
            Returns found extrema points of the wrapped function.
        """
        return self.found

    def is_convex(self, a: NUMBER, b: NUMBER, stepsize: NUMBER = 0.1):
        """
            Returns true if the wrapped function is voncex in the given
            interval, else False.

            Args:
                a: Low end of the interval
                b: High end of the interval
                stepsize: Step size to calculate convexity. Defaults to
                    0.1
        """
        fa = self.calculate(a)
        fb = self.calculate(b)

        for point in np.arange(0, 1, stepsize):
            line = point * fa + (1 - point) * fb
            func = self.calculate(point * a + (1 - point) * b)
            if func > line:
                return False
        return True

    def convexify(self, interval: np.arange, iterations: int = 15, stepsize: NUMBER = 1, decay: NUMBER = 0.9):
        """
            Tries to find a convex region in the given interval.

            Args:
                interval: Initial interval as a numpy.arange
                iterations: Total number of iterations to apply. Defaults
                    to 15.
                stepsize: The stepsize to decrease initial interval
                    at each iteration. Defaults to 1.
                decay: The decay coefficient to apply to stepsize at
                    each iteration. Defaults to 0.9.

            Returns:
                The found convex region as a numpy.arange. If there is no
                found convex interval, returns a numpy.arange at [0, 0].
        """
        if iterations < 1:
            raise ArgumentError("Argument off range: iterations > 1")

        __interval = interval

        for i in range(iterations):
            if not self.is_convex(__interval[0], __interval[-1], stepsize):
                a = __interval[0] + stepsize
                b = __interval[-1] - stepsize
                if b < a:
                    return np.arange(0, 0)  # No convex region was found.
                __interval = np.arange(a, b, stepsize)
                stepsize *= decay
            else:
                return __interval

    def __newton(self, x: FUNC_ARGS, iterations: int = 15, h=None) -> float:
        if h is None:
            h = self.h

        if iterations < 1:
            raise ArgumentError("Argument off range: iterations > 1")

        x0 = x
        for i in range(iterations):
            x0 = x0 - self.derivative(x0, h) / self.second_derivative(x0, h)

        return x0

    def __golden_search(self, interval: np.arange,
                      iterations: int = 15) -> list:  # So that the interval is copied and we do not modify the original interval

        x1, x2 = 0, 0  # Function globals, just to prevent redefinition at each iteration
        maxima = np.max(interval)
        minima = np.min(interval)
        point: float = 0

        for k in range(iterations):
            d = maxima - minima  # Always positive since we do max - min.
            factor = d * phi

            x1 = minima + factor
            x2 = maxima - factor
            if self.calculate(x2) > self.calculate(x1):
                minima = x2
                point = (x1 + x2) / 2
            else:
                maxima = x1
                point = (x1 + x2) / 2
        return point

    def __steepest_descent(self, x0: FUNC_ARGS, iterations: int = 15, h=None) -> list:
        point: float = 0
        x = x0
        for k in range(iterations):
            g = self.derivative(x, h)
            x -= self.alpha * g
            point = x

        return point



