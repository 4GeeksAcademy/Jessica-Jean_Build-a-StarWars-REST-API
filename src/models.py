from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
favorite_characters = db.Table('favorite_characters',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('character_id', db.Integer, db.ForeignKey('characters.id'))
)
favorite_planets = db.Table('favorite_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'))
)
class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_characters= db.relationship("Character", secondary= favorite_characters)
    favorite_planets= db.relationship("Planet", secondary= favorite_planets)
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            # do not serialize the password, its a security breach
        }
class Character(db.Model):
    __tablename__= "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(10))  
    mass = db.Column(db.String(10))    
    hair_color = db.Column(db.String(50))  
    skin_color = db.Column(db.String(50))  
    eye_color = db.Column(db.String(50))   
    birth_year = db.Column(db.String(10))  
    gender = db.Column(db.String(10))



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(10))
    rotation_period = db.Column(db.String(10))
    orbital_period = db.Column(db.String(10))
    gravity = db.Column(db.String(50))
    population = db.Column(db.String(20))
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.String(10))


    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }