from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Form for Pet that is available for adoption."""
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True
                )
    name = db.Column(db.String(50), 
                     nullable=False, 
                     unique=True
                    )
    species = db.Column(db.String(50), 
                        nullable=False, 
                        unique=False
                    )
    photo_url = db.Column(db.String(500), 
                          nullable=True, 
                          unique=False
                        )
    age = db.Column(db.Integer, 
                    nullable=True, 
                    unique=False
                )
    notes = db.Column(db.String(500), 
                      nullable=True, 
                      unique=False
                    )
    available = db.Column(db.Boolean, 
                          nullable=False, 
                          unique=False, 
                          default=True
                        )
    
    
    
