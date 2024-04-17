import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data


def selection_sort(number_list, direction="vzestupne"):
    for idx in range(len(number_list)):
        for i in range(idx, len(number_list)):
            if direction == "vzestupne":
                if number_list[i] == min(number_list[idx:]):
                    number_list[idx], number_list[i] = number_list[i], number_list[idx]
                    break
            elif direction == "sestupne":
                if number_list[i] == max(number_list[idx:]):
                    number_list[idx], number_list[i] = number_list[i], number_list[idx]
                    break

    return number_list


def bubble_sort(number_list):
    for idx in range(len(number_list) - 1):
        i = 0
        while i < len(number_list) - 1:
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
            i += 1

    return number_list


# def insertion_sort(number_list):
#     sorted_i = 0
#     for idx in range(len(number_list)):
#         unsorted_i =


def main():
    numbers = read_data("numbers.csv")
    sort_selection = selection_sort(numbers["series_1"], "vzestupne")
    sort_bubble = bubble_sort(numbers["series_3"])
    # sort_insertion = insertion_sort(numbers["series_3"])
    print(sort_bubble)


if __name__ == '__main__':
    main()
