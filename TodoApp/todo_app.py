import streamlit as st

# create list to store tasks 
tasks = []

# function to add tasks 
def add_task():
    new_task = st.text_input("Enter the new task: ")
    if st.button('Add'):
        tasks.append(new_task)
        st.success("Task added successfully!")

# function to complete a task
def complete_task(index):
    tasks.pop(index)
    st.success("Task Completed")

# function to display tasks 
def show_tasks():
    for i, task in enumerate(tasks):
        st.checkbox(task, on_change=complete_task, args=(i,))

# main app
def main():
    st.title('TO-DO App')

     # Add task section 
    st.header('Add a Task')
    add_task()

    # Dispaly task 
    st.header('Your Tasks')
    show_tasks()

if __name__ == '__main__':
    main()