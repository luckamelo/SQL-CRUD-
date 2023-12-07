import sqlite3

class Student:
    def __init__(self, student_id, nome, idade, mae, pai):
        self.student_id = student_id
        self.nome = nome
        self.idade = idade
        self.mae = mae
        self.pai = pai

def create_tables():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Criação da tabela de usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT)''')

    # Criação da tabela de estudantes
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id TEXT,
                      nome TEXT,
                      idade INTEGER,
                      mae TEXT,
                      pai TEXT)''')

    connection.commit()
    connection.close()

class StudentDatabase:
    def __init__(self):
        create_tables()

    def create_student(self, student_id, nome, idade, mae, pai):
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO students (student_id, nome, idade, mae, pai) VALUES (?, ?, ?, ?, ?)",
                       (student_id, nome, idade, mae, pai))

        connection.commit()
        connection.close()

    def read_student(self, student_id):
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
        result = cursor.fetchone()

        connection.close()

        if result:
            return Student(*result)
        else:
            return None

    def update_student(self, student_id, nome, idade, mae, pai):
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE students SET nome=?, idade=?, mae=?, pai=? WHERE student_id=?",
                       (nome, idade, mae, pai, student_id))

        connection.commit()
        connection.close()

    def delete_student(self, student_id):
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))

        connection.commit()
        connection.close()
