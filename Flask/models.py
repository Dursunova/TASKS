from extensions import db


class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    released = db.Column(db.String(20), nullable=False)
    director = db.Column(db.String(100), nullable= False)
    genre = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f'<Movie{self.title}>'