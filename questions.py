import sqlite3
from sqlite3 import Error

DEFAULT_QUESTIONS = [
    {
        "question": "What is the diameter of a basketball hoop in inches?",
        "options": ["15", "16", "18"],
        "correct_option": 3,
        "category": "general"
    },
    {
        "question": "How many players are allowed on the court from each team in a basketball game?",
        "options": ["4", "5", "6"],
        "correct_option": 2,
        "category": "general"
    },
    {
        "question": "Which player has won the most NBA championships in history?",
        "options": ["Michael Jordan", "LeBron James", "Bill Russell"],
        "correct_option": 3,
        "category": "general"
    },
    {
        "question": "How many quarters are there in a standard basketball game?",
        "options": ["2", "3", "4"],
        "correct_option": 3,
        "category": "general"
    },
    {
        "question": "Which team has won the most NBA championships as of 2022?",
        "options": ["Los Angeles Lakers", "Boston Celtics", "Chicago Bulls"],
        "correct_option": 2,
        "category": "general"
    }
]

# Create SQLite database and connect to it
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Successfully connected to {db_file}')
    except Error as e:
        print(e)
    return conn

# Create a table to store the questions
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(e)

# Insert a question into the table
def insert_question(conn, question):
    sql = ''' INSERT INTO questions(question, options, correct_option, category)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (question["question"], ','.join(question["options"]), question["correct_option"], question["category"]))
    conn.commit()
    return cur.lastrowid

# SQLite database file
database = r"questions.db"

# SQL statement to create the questions table
sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS questions (
                                        id integer PRIMARY KEY,
                                        question text NOT NULL,
                                        options text NOT NULL,
                                        correct_option integer NOT NULL,
                                        category text
                                    ); """

# Create a database connection
conn = create_connection(database)

# Create the questions table
if conn is not None:
    create_table(conn, sql_create_questions_table)
else:
    print("Error! cannot create the database connection.")

# Insert questions into the table
if conn is not None:
    for q in DEFAULT_QUESTIONS:
        insert_question(conn, q)
else:
    print("Error! cannot create the database connection.")
