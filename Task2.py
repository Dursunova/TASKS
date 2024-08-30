import requests
import pymysql

connection = pymysql.Connect(
    host='localhost',
    user='root',
    password='12345',
    db='movie',
    port=3308,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


MOVIE = input("Enter the name of the film: ")
API_KEY = "5d9df2b8"
url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"

r = requests.get(url).json()

title = r.get('TITLE')
released = r.get('RELEASED')
genre = r.get('GENRE')
director = r.get('DIRECTOR')


def create_ex():
    with connection:
      with connection.cursor() as cursor:
         sql = """
         CREATE TABLE IF NOT EXISTS TASK2(
         TITLE VARCHAR(50) NOT NULL,
         RELEASED date,
         DIRECTOR VARCHAR(50) NOT NULL,
         GENRE VARCHAR(50)
         )
         """
         cursor.execute(sql)
      connection.commit()

# create_ex()

def insert_ex(title,released,director,genre):
   with connection:
      with connection.cursor() as cursor:
         sql = "INSERT INTO movie (title,released,director,genre) VALUES (%s,%s,%s,%s)"
         cursor.execute(sql,(title,released,director,genre))
      connection.commit()



if title and released and director and genre:
    movie = r.query.filter_by(title=title, released=released, director=director, genre=genre).first()
    
    if movie:
        print(title,'\n', released,'\n', director,'\n', genre)
    else:
        print('no response')
else:
    print('Error. No such movie found.')