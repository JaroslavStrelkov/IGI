from function import Function

from input_func import input_values

from exit_func import continue_program

from graficsArbeit import Plotter

from newFunc import StatisticsCalculator



def print_table(x, n, series_result, math_result, eps):

    print("-" * 90)
    print(f"| {'x':^10} "f"| {'n':^10} "f"| {'F(x)':^20} "f"| {'Math F(x)':^20} "f"| {'eps':^10} |")
    print("-" * 90)
    print(f"| {x:^10.5f} "f"| {n:^10} " f"| {series_result:^20.10f} "f"| {math_result:^20.10f} "f"| {eps:^10.10f} |")
    print("-" * 90)


def print_statistics(stats):

    print("\nStatistics:")

    for key, value in stats.items():
        print(f"{key}: {value}")


def main():

    while True:
        try:
            x, eps = input_values()
            function = Function(x, eps)

            result = (function.calculate())

            print_table(x,result["iterations"], result["series_result"], result["math_result"], eps)

            stats = (StatisticsCalculator.calculate(result["values"]))

            print_statistics(stats)

            Plotter.draw(eps)

            print("\nTotal calculations:", Function.total_calculations)

        except ValueError as error:
            print("Value error:", error)

        if not continue_program():
            break

main()