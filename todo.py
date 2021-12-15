"""
This file contains implementations of function that adds new tasks to tasks database.
"""

from datetime import date
import csv
import re

def add_new_task(descr:str, due_date:date, prio:int, todo_list:dict):
    """
    This function adds new task to dictionary {date:[]} with priority prio and description descr.
    Function should get valid arrguments (it is checked in add_new_task_interface function)
    If function iof given invalid arguments it will raise assertion error.
    Function returns dictionary of tasks.
    """
    if not due_date in todo_list.keys():
        todo_list[due_date] = []
    assert prio <= len(todo_list[due_date])
    todo_list[due_date].insert(prio, descr)
    return todo_list

def add_new_task_interface(todo_list:dict):
    """
    Function interacts with user using command prompt and adds new task (given by user) to todo_list.
    Returns changed todo_list with a new task
    """
    print('Input date of new task in format YYYY-MM-DD')
    due_date = None
    while None == due_date:
        s = input('>>> ')
        try:
            due_date = date.fromisoformat(s)
        except:
            print('Please input date in correct format YYYY-MM-DD.')
            continue
    print('Input description of the task!')
    desc = input('>>> ')
    new_prio = None
    if due_date in todo_list.keys():
        print('You already have existing deadlines for given date. Here they are, sorted by their priority')
        for (i, task) in enumerate(todo_list[due_date]):
            print(f'Prioity : {i + 1}, description : {task}')
        max_prio = len(todo_list[due_date])
        print(f'Input new priority in range [1; {max_prio}]')
        while new_prio == None:
            try:
                new_prio = int(input('>>>')) - 1
                if new_prio < 0 or new_prio >= max_prio:
                    new_prio = None
                    raise KeyError
            except:
                print(f'Please input new priority in correct range [1; {max_prio}]')
                continue
    else:
        new_prio = 0
    add_new_task(desc,due_date,new_prio,todo_list)
    print('Successfulli added new task to task manager!')
    return todo_list





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
    the_year = int(wanted_date.split("-")[0])
    the_month = int(wanted_date.split("-")[1])
    the_day = int(wanted_date.split("-")[2])
    for dates, tasks in dct.items():
        if dates == date(the_year, the_month, the_day):
            if len(tasks) > priority:
                del dct[dates][priority]
    return dct


def mark_as_done(dct):
    way = input("Type 1 if you want to find task by the date and priority"
                "Type 2 if you want to find task by the first word")
    if way == 2:
        first_word = input("Type the word you want to find the task by")
        new_dct = search_by_first_word(dct, first_word)
    elif way == 1:
        wanted_date = input("Type the date in format YYYY-MM-DD")
        priority = input("Type the priority of the task(starting from 0)")
        new_dct = search_by_date_priority(dct, wanted_date, priority)
    return new_dct


if __name__ == "__main__":
    dct = {}
    d = date(2002, 12, 31)
    dct[d] = ["sth", "sth1", "sth2"]
    write_to_csv(dct)
