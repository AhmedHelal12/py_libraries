import sqlite3
from pathlib import Path
sql_connection=sqlite3.connect(Path.home() / Path('Documents','to-do-list.db'))
crs=sqlite3.Cursor(sql_connection)

## creating the Table 
sql_commands=""" CREATE TABLE if not exists ToDoList(
id INTEGER PRIMARY KEY,
title VARCHAR(50),
description VARCHAR(150)
)
"""
crs.execute(sql_commands)

print("""
'a' => add a new task
'd' => delete a task
's' => show all tasks
'u' => update a task
'q' => quit the app
""")

## This function to check If a certain ID is exists or not
def check_id(id):
        my_id=int(id)
        crs.execute('SELECT id FROM ToDoList where id=?',(my_id,))

        if crs.fetchone() is None:
            raise ValueError('This ID is not exists')
        


## To Add a certain task
def add_task():
    ## get the last ID to increment to set a new one
    crs.execute('SELECT MAX(id) FROM ToDoList ')
    count=0
    fetchID=crs.fetchone()
    count = (fetchID[0] or 0) + 1 ## if no ids are there (id=0) we will increment 1 or if exists we will increment it too
    try:
        add_title=input('Enter the title of the task:')
        description=input('Enter the description of the task:')
        if add_title=='' or description=='':
            raise ValueError('Title and Description can not be empty')
        
        crs.execute('INSERT INTO ToDoList VALUES(?,?,?)',[count,add_title,description])
        sql_connection.commit()

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'An error occurred,{e}')

def delete_task():
    try:
        my_id=input('Please enter the ID of the desired task:').strip()
        check_id(my_id)
        crs.execute('DELETE FROM ToDoList WHERE id=?',(my_id,))
        sql_connection.commit()

    except ValueError as e:
        print(e)
    except Exception:
        print('The ID should be a number and within certain numbers')
    

def show_tasks():
    crs.execute('SELECT id,title,description FROM ToDoList ')

    try:
        fetchall=crs.fetchall()

        if len(fetchall)==0:
            raise Exception
        
        for x in fetchall:
            print(x)
    except Exception:
        print("No tasks to display")


def update_task():
    try:
        
        my_id=input('Enter the ID of the desired updated task:')
        ## raise An error If the input data is not a number
        if not my_id.isdigit():
            raise ValueError('ID must be a number.')
        

        check_id(my_id)

        updated_title=input('Update the title:')
        updated_description=input('Update the description:')
        
        ## if empty values are set we will raise an error
        if updated_title=='' or updated_description=='':
            raise ValueError('Can not update values to empty')
        crs.execute('UPDATE ToDoList SET title=?,description=? WHERE id=?',(updated_title,updated_description,my_id))
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    sql_connection.commit()


while True:
    print('##################################')
    user_input=input('please choose an option:').strip().lower()

    if user_input=='a':
        add_task()

    elif user_input=='d':
        delete_task()
        
    elif user_input=='s':
        show_tasks()

    elif user_input=='u':
        update_task()

    elif user_input=='q':
        break
    

sql_connection.close()