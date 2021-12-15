# main script


def print_deadlines(imp_date, to_do_dict):
    if imp_date not in to_do_dict:
        print(f"No deadlines for {imp_date}")
    else:
        current_tasks = to_do_dict.get(imp_date)
        print(f"Deadlines for {imp_date}: ")
        for task in current_tasks:
            pror_num = current_tasks.index(task)
            print(f"priority {pror_num}", end=" --> ")
            print(f"{task}", end="\n")


def exit_interface():
    decision = input("Do you need to add anything? Enter (yes/exit): ")
    while decision != "yes" and decision != "exit":
        decision = input("Do you need to add anything? Enter (yes/exit): ")
    if decision == "yes":
        pass
        # func to add new tasks + func to make new priority list
    else:
        print("Okay, see you later!")
        # func to write csv_file
