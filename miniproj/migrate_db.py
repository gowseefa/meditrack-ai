import sqlite3
import os

def migrate():
    db_path = r'c:\Users\Happy\Desktop\miniproj\database.db'
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if reports table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reports'")
    if not cursor.fetchone():
        print("Error: Table 'reports' not found in database.")
        conn.close()
        return

    # Check if ai_explanation exists
    cursor.execute("PRAGMA table_info(reports)")
    columns = [info[1] for info in cursor.fetchall()]
    
    if 'ai_explanation' not in columns:
        print("Adding 'ai_explanation' column...")
        cursor.execute("ALTER TABLE reports ADD COLUMN ai_explanation TEXT")
        conn.commit()
        print("Column added successfully.")
    else:
        print("'ai_explanation' column already exists.")
    
    conn.close()

if __name__ == "__main__":
    migrate()
