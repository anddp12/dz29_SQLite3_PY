import sqlite3

class Author:
    def __init__(self, first_name=str, last_name=str, country=str, date_birth=str, date_death=str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_birth = date_birth
        self.date_death = date_death

# authors = [
#     Autor("Jack", "London", "USA", "1876-01-12", "1916-12-22"),
#     Autor("Alexandre", "Dumas", "France", "1802-07-24", "1870-12-05"),
#     Autor("Honore", "de Balzac", "France", "1799-05-20", "1850-08-18"),
#     Autor("Jules", "Verne", "France", "1828-02-08", "1905-03-24"),
#     Autor("Franz", "Kafka", "Austria-Hungary", "1883-07-03", "1924-06-03")
# ]

authors = [
    ("Jack", "London", "USA", "1876-01-12", "1916-12-22"),
    ("Alexandre", "Dumas", "France", "1802-07-24", "1870-12-05"),
    ("Honore", "de Balzac", "France", "1799-05-20", "1850-08-18"),
    ("Jules", "Verne", "France", "1828-02-08", "1905-03-24"),
    ("Franz", "Kafka", "Austria-Hungary", "1883-07-03", "1924-06-03")
]

with sqlite3.connect("hw29db.db") as connection:
    cursore = connection.cursor()
    cursore.execute('DROP TABLE IF EXISTS Authors')
    cursore.execute('''
        CREATE TABLE "Authors" (
            "id"	INTEGER,
            "first_name"    TEXT,
            "last_name"    TEXT,
            "country"    TEXT,
            "date_birth"	TEXT,
            "date_death"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    ''')
    cursore.executemany("INSERT INTO Authors (first_name, last_name, country, date_birth, date_death) VALUES (?, ?, ?, ?, ?);", authors)

class Book:
    def __init__(self, title=str, year_publishing=int) -> None:
        self.title = title
        self.year_publishing = year_publishing

# books = [
#     Book("Transformation (compilation)", 2016),
#     Book("Process (compilation)", 2015),
#     Book("Mysterious Island", 2016),
#     Book("The Children of Captain Grant", 2016),
#     Book("Gobsek", 2013),
#     Book("Father Goriot", 2019),
#     Book("Count of Monte Cristo", 2017),
#     Book("Three Musketeers", 2021),
#     Book("White Fang", 2014),
#     Book("Sea wolf", 2021)
# ]

books = [
    ("Transformation (compilation)", 2016),
    ("Process (compilation)", 2015),
    ("Mysterious Island", 2016),
    ("The Children of Captain Grant", 2016),
    ("Gobsek", 2013),
    ("Father Goriot", 2019),
    ("Count of Monte Cristo", 2017),
    ("Three Musketeers", 2021),
    ("White Fang", 2014),
    ("Sea wolf", 2021)
]

with sqlite3.connect("hw29db.db") as connection:
    cursore = connection.cursor()
    cursore.execute('DROP TABLE IF EXISTS Books')
    cursore.execute('''
        CREATE TABLE "Books" (
            "id"	INTEGER,
            "title"    TEXT,
            "year_publishing"    INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    ''')
    cursore.executemany("INSERT INTO Books (title, year_publishing) VALUES (?, ?);", books)

# cursore.execute('SELECT * FROM Books')
# all_books = cursore.fetchall()
# print(all_books)

# cursore.execute('SELECT * FROM Authors')
# all_authors = cursore.fetchall()
# print(all_authors)

with sqlite3.connect("hw29db.db") as connection:
    cursore = connection.cursor()
    cursore.execute('DROP TABLE IF EXISTS Author_book')
    cursore.execute('''
        CREATE TABLE "Author_book" (
            "id"	INTEGER,
	        "book_id"	INTEGER,
	        "author_id"	INTEGER,
	        PRIMARY KEY("id" AUTOINCREMENT),
	        FOREIGN KEY("book_id") REFERENCES "Books"("id"),
	        FOREIGN KEY("author_id") REFERENCES "Authors"("id")
        );
    ''')
