import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (
    email TEXT UNIQUE,
    count INTEGER
)
''')

# Sample email data (simulating lines from a mailbox)
emails = [
    'alice@example.com',
    'bob@example.com',
    'alice@example.com',
    'carol@example.com',
    'bob@example.com',
    'alice@example.com',
    'dave@example.com',
    'carol@example.com',
    'bob@example.com',
    'alice@example.com',
    'eve@example.com',
    'frank@example.com',
    'alice@example.com',
    'bob@example.com',
    'carol@example.com'
]

# Insert or update counts
for email in emails:
    cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))

# Commit changes
conn.commit()

# Display top senders
print("📬 Top email senders:")
for row in cur.execute('SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'):
    print(f"{row[0]:<25} {row[1]}")

# Close connection
cur.close()