from flask import render_template,url_for
from models import Movie
from app import app

@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

@app.route('/movies/<int:movie_id>')
def movie(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('movie.html', movie=movie)