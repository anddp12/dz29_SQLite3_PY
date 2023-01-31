import sqlite3

class Author:
    def __init__(self, first_name=str, last_name=str, country=str, date_birth=str, date_death=str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_birth = date_birth
        self.date_death = date_death

# author = [
#     Autor("Jack", "London", "USA", "1876-01-12", "1916-12-22"),
#     Autor("Alexandre", "Dumas", "France", "1802-07-24", "1870-12-05"),
#     Autor("Honore", "de Balzac", "France", "1799-05-20", "1850-08-18"),
#     Autor("Jules", "Verne", "France", "1828-02-08", "1905-03-24"),
#     Autor("Franz", "Kafka", "Austria-Hungary", "1883-07-03", "1924-06-03")
# ]

author = [
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
    cursore.executemany("INSERT INTO Authors (first_name, last_name, country, date_birth, date_death) VALUES (?, ?, ?, ?, ?);", author)
