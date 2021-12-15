# main script
from datetime import date
import csv
import re


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


def search_by_first_word(dct, first_word):
    pattern = f"^{first_word}"
    for the_date, tasks in dct.items():
        for the_task in tasks:
            if re.search(pattern, the_task):
                dct[the_date].remove(the_task)
    return dct


def search_by_date_priority(dct, wanted_date, priority):
    the_year = wanted_date.split("-")[0]
    the_month = wanted_date.split("-")[1]
    the_day = wanted_date.split("-")[2]
    for dates, tasks in dct.items():
        if dates==


def mark_as_done(dct):
    way = input("Type 1 if you want to find task by the date and priority"
                "Type 2 if you want to find task by the first word")
    if way == 2:
        first_word = input("Type the word you want to find the task by")
        search_by_first_word(dct, first_word)
    elif way == 1:
        wanted_date = input("Type the date in format YYYY-MM-DD")
        priority = input("Type the priority of the task")




if __name__ == "__main__":
    dct = {}
    d = date(2002, 12, 31)
    dct[d] = ["sth", "sth1", "sth2"]
    write_to_csv(dct)
