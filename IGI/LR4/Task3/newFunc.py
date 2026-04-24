from statistics import (
    mean,
    median,
    mode,
    variance,
    stdev,
    StatisticsError
)


class StatisticsCalculator:

    @staticmethod
    def calculate(data):

        try:
            mode_value = mode(data)

        except StatisticsError:

            mode_value = ("No unique mode")

        return {
            "mean": mean(data),
            "median": median(data),
            "mode": mode_value,
            "variance": (
                variance(data)
                if len(data) > 1
                else 0),

            "std_deviation": (
                stdev(data)
                if len(data) > 1
                else 0
                )
        }