# 🔹 Task 10: Create a File-Based To-Do List
# 🔹 Build a file-based To-Do list application where the user can:

# Add tasks.
# View all tasks.
# Mark tasks as completed.
# Delete tasks.

print("""
      
. Add Task
. View List
. Mark Task as Done
. Delete Task
. Exit
      
""")
isCond = True
while isCond:
    taskOption = input("Write an Option :").replace(" ",'')
    if not taskOption:
        print("Plz , Enter an Option")
    else:

        if taskOption.lower() == "Add Task".lower().replace(" ",''):

            taskInput = input("Enter a Task : ")
            # isCompeleted = input("Do you comple your task (yes | no) : ")
            if not taskInput :
                print("Enter a Task and also give the confirmation of task completed or not.")
            else:
                #add the task in task.txt file
                with open("tasks.txt","a") as taskFile:
                    taskFile.write(f"{taskInput}\n")

        elif taskOption.lower() == "Mark Task as Done".lower().replace(" ",''):
            completeTask = input("Enter the Task you completed : ") 
            if completeTask:
                with open("tasks.txt","r") as completedFile:
                    taskList = completedFile.read().splitlines()
                    #filter the list to remove that task
                    updatedTask = [task for task in taskList if task.lower().replace(" ",'') != completeTask.lower().replace(" ",'')]
                    print(updatedTask)
                    #now add that task with ✅
                    updatedTask.append(f"{completeTask} ✅ \n")

                    #update the tasks.txt file also with the complete mark
                    with open("tasks.txt","w",encoding="utf-8") as markCompleteFile:
                        for task in updatedTask:
                            markCompleteFile.write(f"{task}\n")
            else:
                print("❌ No task entered.")

         # #for delete a task
        elif taskOption.lower() == "Delete Task".lower().replace(" ", ''):
            deleteTask = input("Enter the Task That You Want to Delete: ").replace(" ",'')
    
            if deleteTask:
                with open("tasks.txt", "r") as forDeleteFile:
                    taskList = forDeleteFile.read().splitlines()  # Correctly reads tasks as a list

                updatedTasks = [task for task in taskList if task.replace(" ",'').lower() != deleteTask.lower()]  # Remove selected task

                with open("tasks.txt", "w") as forDeleteFileTwo:
                    for task in updatedTasks:
                        forDeleteFileTwo.write(f"{task}\n")  # Write back updated tasks
                print(f"✅ Task '{deleteTask}' has been deleted.")
    
            else:
                print("❌ No task entered. Please try again.")


        elif taskOption.lower() == "View List".lower().replace(" ",''):
        
            #for view the list
            isCheckList = input("Do You Want to View the List (yes | no) : ")
            if isCheckList.lower() == "yes":
                with open("tasks.txt","r") as viewList:
                 print(viewList.read())
            else:
                continue
        elif taskOption.lower() == "Exit".lower().replace(" ",''):
            break
        else:
            break

                

            


            
