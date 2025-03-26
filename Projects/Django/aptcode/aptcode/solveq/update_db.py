import sqlite3
import re 
import os

# create a function to initialize the database
def init_questions_db():
    # open sqlite database file
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # create table problems if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS problems (title TEXT PRIMARY KEY, question TEXT, solution TEXT)")
    conn.commit()
    conn.close()

# create a function to update the database
def update_questions():
    # open sqlite database file
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # read questions from folder "problems", read all file starts with Assignment
    # and ends with .txt
    # for each file, read questions and answers
    # insert into database
    # close database

    # read all files from problems folder
    for file in os.listdir('problems'):
        if file.startswith('Assignment') and file.endswith('.txt'):
            with open(file, 'r') as f:
                data = f.read()
                # regular expression to extract title. Expression : Title = ''' <title> '''
                title = re.search(r'Title = \'\'\'(.*)\'\'\'', data).group(1)
                # regular expression to extract question. Expression : Question = ''' <question> '''
                question = re.search(r'Question = \'\'\'(.*)\'\'\'', data).group(1)
                # regular expression to extract solution. Expression : Solution = ''' <solution> '''
                solution = re.search(r'Solution = \'\'\'(.*)\'\'\'', data).group(1)
                # insert into database

                cursor.execute("INSERT INTO problems VALUES (?, ?, ?)", (title, question, solution))
                conn.commit()
    conn.close()
