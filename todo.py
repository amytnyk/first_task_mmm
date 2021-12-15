# main script
from datetime import date
import csv


def write_to_csv(dct):
    """
    the function writes the tasks into csv file
    :param dct:
    :return:
    """
    num_tasks = find_busiest(dct)
    header = ["DATE"]
    for i in range(num_tasks):
        header.append(f"TASK {i}")
    with open("task_list.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for the_date, tasks in dct.items():
            row = [the_date] + tasks
            writer.writerow(row)


def find_busiest(dct):
    max_tasks = 0
    for key, value in dct.items():
        num_tasks = len(value)
        if num_tasks > max_tasks:
            max_tasks = num_tasks
    return max_tasks


if __name__ == "__main__":
    dct = {}
    d = date(2002, 12, 31)
    dct[d] = ["sth", "sth1", "sth2"]
    write_to_csv(dct)
