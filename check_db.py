import sqlite3
DB='src/data/study_assistant.db'
conn=sqlite3.connect(DB)
c=conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='quiz_attempts'")
print('quiz_attempts exists:', bool(c.fetchone()))
c.execute('SELECT COUNT(*) FROM quiz_attempts')
count = c.fetchone()[0]
print('quiz_attempts count:', count)
conn.close()