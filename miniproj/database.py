import sqlite3
import os

def init_db():
    db_path = 'meditrack_final.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    # Create doctors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    # Create patients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        symptoms TEXT NOT NULL,
        disease TEXT,
        prescription TEXT
    )
    ''')

    # Create reports table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        file_name TEXT NOT NULL,
        file_path TEXT NOT NULL,
        ai_explanation TEXT,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create symptoms_disease table for simple suggestion logic
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS disease_map (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symptom TEXT NOT NULL,
        disease TEXT NOT NULL
    )
    ''')

    # Add default admin user if not exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")

    # Add some sample diseases for the checker
    cursor.execute("SELECT COUNT(*) FROM disease_map")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ('fever', 'Infection'),
            ('cough', 'Cold/Flu'),
            ('headache', 'Migraine/Stress'),
            ('stomach pain', 'Gastritis'),
            ('chest pain', 'Heart Related Issue'),
            ('rash', 'Allergy'),
            ('joint pain', 'Arthritis'),
            ('shortness of breath', 'Asthma/Lung Issue')
        ]
        cursor.executemany("INSERT INTO disease_map (symptom, disease) VALUES (?, ?)", sample_data)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
