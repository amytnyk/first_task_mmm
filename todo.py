# main script
from datetime import date
import csv


def write_to_csv(dct):
    """
    the function writes the tasks into csv file
    :param dct:
    :return:
    """
    header = ["DATE"]
    with open("task_list.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for the_date, tasks in dct.items():
            row = the_date+tasks
            writer.writerow(row)
