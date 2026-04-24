from textAnalyzer import FullAnalyzer
from fileInZip import FileInZIP


def read_file(filename):

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def save_result(filename, data):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


def main():

    while True:

        try:

            filename = input("Введите имя файла: ")

            text = read_file(filename)

            analyzer = FullAnalyzer(text)

            result = analyzer.full_analysis()

            print(result)

            save_result("result_task2.txt", result)

            FileInZIP.zip_machen("result_task2.txt", "result_task2.zip")

            FileInZIP.get_zip_info("result_task2.zip")

        except FileNotFoundError:
            print("Файл не найден")

        except ValueError as e:
            print("Ошибка:", e)

        repeat = input("Повторить? (y/n): ")

        if repeat.lower() != "y":
            break
main()