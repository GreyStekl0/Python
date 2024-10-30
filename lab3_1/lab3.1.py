import sqlite3

con = sqlite3.connect("video_catalog.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Видео (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    название TEXT NOT NULL,
    автор TEXT NOT NULL,
    длительность REAL,
    категория TEXT
)
""")

def add_video(название, автор, длительность, категория):
    cur.execute("INSERT INTO Видео (название, автор, длительность, категория) VALUES (?, ?, ?, ?)",
                (название, автор, длительность, категория))
    con.commit()

def add_videos(video_list):
    cur.executemany("INSERT INTO Видео (название, автор, длительность, категория) VALUES (?, ?, ?, ?)", video_list)
    con.commit()

def show_videos():
    print("Список всех видеозаписей:")
    cur.execute("SELECT * FROM Видео")
    videos = cur.fetchall()
    for video in videos:
        print(video)

array_video = [
    ("Помни", "Кристофер Нолан", 1.88, "детектив"),
    ("Оппенгеймер", "Кристофер Нолан", 3.0, "Документальный"),
    ("Дюнкерк", "Кристофер Нолан", 1.76, "Документальный"),
    ("Пираты Карибского моря: Проклятие Чёрной жемчужины", "Гор Вербински", 2.38, "боевик"),
    ("Сто лет тому вперёд", "Александр Андрющенко", 2.36, "Фантастика")
]

add_videos(array_video)

show_videos()


cur.close()
con.close()
