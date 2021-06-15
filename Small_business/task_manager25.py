#Management tool for Tasks in a small business
#Made changes to format of original tasks.txt from task 20

#Python regular expression and datetime modules imported for later use
#User signin initialised to False and loop through text file to seperate usernames

import re
import datetime

today = datetime.datetime.now()

#function for new user registration option for Admin only
def reg_user():
    while True:
        user = input("Create new username or enter 'quit' to exit: ").lower()
        if user == "quit":
            break
            
        user_names = ""

        with open("user.txt", "r") as users:
            for line in users:
                text = line.strip()
                text = text.split(",")
                user_names += text[0]
                        
            if user in user_names:
                print(f"{user.title()} already exists.")
            else:
                print(f"New username: {user.title()}")
            #loop while user not logged in to signin with username and password and relevant error messages for incorrect inp
                pin = input("Please create a new password: ")
                pin2 = input("Re-enter new password: ")
                if pin != pin2:
                    print("Password does not match, re-enter new password.")   
                else:
                    print("Password confirmed! New username created.\n")
                    with open("user.txt", "a+") as users:
                        users.write(f"\n{user},{pin}")
                    users.close()

#function to add a new task and task information   
def add_task():
    user_assigned = input("\nEnter username of the person you are assigning task to: ").lower()
    task_title = input("Enter the title of the task: ")
    describe = input("Describe the task assigned: ")
    date_assigned = input("What is the current date of task assignment (yyyy-mm-dd): ")
    due_date = input("When is the due date for the task (yyyy-mm-dd): ")
    print("Task added.")

    with open("tasks.txt", "a+") as tasks:
        tasks.write(f"\n{user_assigned},{task_title},{date_assigned},{due_date},No,{describe}")
        
    tasks.close()

#function to view all tasks' information in the business
#empty row created due to editing the completedness of tasks later hence if/else statement
def view_all():
    with open("tasks.txt", "r") as tasks:
        for row in tasks:
            field = row.strip().split(",")
            task_info = (f"Username: \t{field[0]}.\nTask title: \t{field[1]}\nDate Assigned: \t{field[2]}."+ 
                f"\nDue Date: \t{field[3]}.\nCompleted: \t{field[4]}.\nDescription: \t{field[5]}.\n")
            print(task_info)

    tasks.close()

#options to edit tasks(change user or due date) or mark them as complete
#only Tasks that have not yet been completed can be edited
def taskEdit(): 
    #function for changes to mark tasks as Complete with Yes/No
    def edited(complete):

        userTask = task_lines[task_count].strip().split(",")
        new_text = task_lines[task_count].replace(userTask[4], complete)
            
        with open("tasks.txt", "r") as tasks:
            updated = tasks.read().replace(task_lines[task_count].strip(), new_text)
                
            with open("tasks.txt", "a+") as update:
                update.write(updated.strip())

    #function to assign a new username to the task
    def edit_user(user_change):
        userName = task_lines[task_count].strip().split(",")
        new_name = task_lines[task_count].replace(userName[0], new_user)
        
        print(f"Task assigned to {new_user}")
    
        with open("tasks.txt", "r") as tasks:
            user_update = tasks.read().replace(task_lines[task_count].strip(), new_name)
            
            with open("tasks.txt", "a+") as update:
                update.write(user_update)
        
    #function to change the due date of selected task
    def edit_time(user_change):
        userDate = task_lines[task_count].strip().split(",")
        new_date = task_lines[task_count].replace(userDate[3], new_time)

        with open("tasks.txt", "r") as tasks:
            time_update = tasks.read().replace(task_lines[task_count].strip(), new_date)

            with open("tasks.txt", "a+") as testing:
                testing.write(time_update)
            
    #program to edit task by marking it complete or changing assigned user or due date            
    edit = input("Would you like to edit a task? 'Yes' or return to the menu? (-1)\n").title()
    if edit == "Yes":
        task_count = int(input("Enter the Task Number?\n"))
        task_count = task_count - 1
        with open("tasks.txt", "r") as tasks:
            task_lines = tasks.readlines()
            for line in task_lines:
                print(user_tasks)
                break

        task_edit = input("Would you like to Mark task as complete(M) or Edit task (E)? M/E").title()
        if task_edit == "M":    
            complete = input("Has this task been completed? Yes/No \n").title()
            if complete == "Yes":
                edited(complete)
            elif complete == "No":
                edited(complete)
        
        elif task_edit == "E":
            if re.search("No", line):
                user_change = input("Would you like to assign task to new username (A) or Change Due date (D) \n").title()         
                if user_change == "A":
                    new_user = input("Assign new user: ").title()
                    edit_user(user_change)
                elif user_change == "D":
                    new_time = input("Enter new Date: ").title()
                    edit_time(user_change)
            else:
                print("Task already completed.")
        else:
            print("Please choose from options provided.")

#Tasks for username input printed out
def view_mine():
    username = input("Username: ").lower()
    task_num = 0
    with open("tasks.txt", "r") as tasks:
        print(f"All the tasks assigned to {username}: ")
        for row in tasks:
            field = row.strip().split(",")
            task_num += 1
                
            if username == field[0]:
                user_tasks = (f"{task_num}.\nTask title: \t{field[1]}\nDate Assigned: \t{field[2]}."+ 
                        f"\nDue Date: \t{field[3]}.\nCompleted: \t{field[4]}.\nDescription: \t{field[5]}.\n")
                print(user_tasks)

                #insert  edittask function here
                
    tasks.close()    

#task overview function to display all statistics for all the tasks
def task_view():

    with open("tasks.txt", "r") as tasks:
        task_list = tasks.readlines()

        task_count = 0
        complete = 0
        incomplete = 0
        over_due = 0
        
    for task in task_list:
        field = task.strip().split(",")
        if not task.strip():
            pass

        else:
            task_count += 1
            task_num = task_count

            if re.search("Yes", task):
                complete += 1
                done = complete

            if re.search("No", task):
                incomplete += 1
                not_done = incomplete

                notdone = not_done/task_num 
                percent_notdone = notdone*100

            overdue = field[3]
            if overdue < str(today) and re.search("No", task):
                over_due += 1
                past_due = over_due

                pastdue = past_due/task_num
                percent_due = pastdue*100

    task_overview = (f"\nThere are {task_num} tasks in total.\nThere are {done} tasks complete.\nThere are {not_done} tasks incomplete." +
    f"\nThere are {past_due} tasks not completed and overdue.\n{round(percent_notdone, 2)}% Of tasks are incomplete." +
    f"\n{round(percent_due, 2)}% Of tasks are overdue.")
    print(task_overview)
    with open("task_overview.txt", "a+") as view:
        view.write(str(today) + "\n")
        view.write(task_overview)
#user_overview to display statistics for each user's tasks
def user_view():

    with open("user.txt", "r") as users:

        lines = users.readlines()
        user_count = len(lines)

    username = input("Username: ").title()            
    with open("tasks.txt", "r") as tasks:
        task_list = tasks.readlines()

        task_count = 0
        user_task = 0
        complete = 0
        incomplete = 0
        over_due = 0

#Percentage variables set to 0 to be able to be used outside if statements for final print output
        user_percent = 0
        user_overview = 0
        done_percent = 0
        percent_done = 0
        percent_due = 0

        for task in task_list:
            if not task.strip():
                pass
            else:
                field = task.strip().split(",")    
                task_count += 1
                task_num = task_count

                #if statement to access only the user's tasks
                # Total percentages of user's tasks, completed, incomplete and overdue respectively
                if username == field[0]:
                    user_task += 1
                    user_total = user_task
                    users_total = user_total / task_num
                    user_percent = round(users_total * 100 , 2)
                        
                    if re.search("Yes", task):
                        complete += 1
                        done = complete
                        task_done = done / user_total
                        done_percent = round(task_done * 100 , 2)
                        
                    if re.search("No", task):
                        incomplete += 1
                        not_done = incomplete
                        notdone = not_done / user_total
                        percent_notdone = round(notdone * 100 , 2)
                                
                    overdue = field[3]
                    if overdue < str(today) and re.search("No", task):
                        over_due += 1
                        past_due = over_due
                        pastdue = past_due / user_total
                        percent_due = round(pastdue * 100 , 2)
                
        user_overview = (f"Total users:\t{user_count}\nTotal tasks: \t{task_num}\nTasks for {username.title()}: " + 
                        f"\nTotal assigned:\t{user_total}\nOf total tasks:\t{user_percent}%\nCompleted: \t{done_percent}%" + 
                        f"\nIncomplete: \t{percent_notdone}%\nOverdue: \t{percent_due}%")
        print(user_overview)

        with open("user_overview.txt", "a+") as f:
            f.write(user_overview)
                                                                                        
        f.close()               
        users.close()
        tasks.close()    

#function to create and display user and task overview text files reports
def reports():
    task_view()
    user_view()
#function to display statistics of the tasks
def stats():
    with open("user.txt", "r") as users:

        lines = users.readlines()
        user_count = len(lines)
                
    with open("tasks.txt", "r") as tasks:
        task_list = tasks.readlines()

        task_count = 0
        for task in task_list:
            if not task.strip():
                pass
            else:
                field = task.strip().split(",")
                task_count += 1
                task_num = task_count
        print(f"There are {user_count} users and {task_num} tasks in total.")
    users.close()
    tasks.close()

#function for when user exists the program 
def logout():
    print("User logged out.")

def adminChoice():
    print("\nPlease select one of the following options: ")
    options = input("r - register user.\nds - display statistics.\na - add task.\nva - view all tasks.\nvm - view my tasks.\ngr - generate reports" + " \ne - exit.\n").lower()

    if options == "r":
        reg_user()
    elif options == "ds":
        stats()
    elif options == "a":
        add_task()
    elif options == "va":
        view_all()
    elif options == "vm":
        view_mine()
        taskEdit()
    elif options == "gr":
        reports()
    elif options == "e":
        logout()
    else:
        print("Incorrect selection. Chose from the given options.")

def Choice():
    print("\nPlease select one of the following options: ")
    options = input("a - add task.\nva - view all tasks.\nvm - view my tasks.\ne - exit.\n").lower()

    if options == "a":
        add_task()
    elif options == "va":
        view_all()
    elif options == "vm":
        view_mine()
        taskEdit()
    elif options == "e":
        logout()
    else:
        print("Incorrect selection. Chose from the given options.")

#Log in the user to run the program
user_names = ""
user_passwords = ""
    
logged_in = False

with open("user.txt", "r") as users:
    for line in users:
        text = line.strip()
        text = text.split(",")
        user_names += text[0]
        user_passwords += text[1]

#loop while user not logged in to signin with username and password and relevant error messages for incorrect inputs
while logged_in == False:
    username = input("Enter username: ")
    if username not in user_names:
        print(f"{username} does not exist.")
    else:
        password = input("Enter your password: ")        
        if password in user_passwords:
            print(f"Correct password, {username} logged in.")
            logged_in = True
            #while loop for the actual program so admin can have their own menu and other users have limited menu options
            while logged_in:
                if username == "admin":
                    adminChoice()
                elif username != "admin":
                    Choice()
        else:
            print("Incorrect password.")    
            
users.close()