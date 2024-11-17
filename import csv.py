import csv
import sqlite3
import sqlalchemy

# Step 1: Create and Write to `test.csv`
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open('test.csv', 'wt') as outfile:
    outfile.write(text)

# Step 2: Read and Print from `test.csv`
with open('test.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)

# Step 3: Create and Write to `books2.csv`
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books2.csv', 'wt') as outfile:
    outfile.write(text)

# Step 4: Set up SQLite Database
db = sqlite3.connect('books.db')
curs = db.cursor()

# Create Table
curs.execute('''CREATE TABLE IF NOT EXISTS book (title TEXT, author TEXT, year INTEGER)''')
db.commit()

# Insert Data into SQLite Database
ins_str = 'INSERT INTO book VALUES (?, ?, ?)'
with open('books2.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], int(book['year'])))
db.commit()

# Step 5: Query SQLite Database
# Query 1: Order by Title
sql = 'SELECT title FROM book ORDER BY title ASC'
for row in db.execute(sql):
    print(row[0])

# Query 2: Custom Order Ignoring "The"
sql = '''SELECT title FROM book
         ORDER BY CASE
             WHEN title LIKE "The %" THEN SUBSTR(title, 5)
             ELSE title
         END'''
for row in db.execute(sql):
    print(row[0])

# Query 3: Order by Year
sql = 'SELECT * FROM book ORDER BY year'
for row in db.execute(sql):
    print(', '.join(map(str, row)))

# Step 6: Using SQLAlchemy for Querying
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'SELECT title FROM book ORDER BY title ASC'
rows = conn.execute(sql)
for row in rows:
    print(row[0])
