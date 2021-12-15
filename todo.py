"""
This file contains implementations of function that adds new tasks to tasks database.
"""

from datetime import date

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

