from . import db

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    image = db.Column(db.VARCHAR(300), nullable=False)
    
    def __repr__(self) -> str:
        return f'<Photo {self.title} {self.description}>'
#MODELOS DE DATOS

    



