from app import db

class Voiture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(50))
    annee_modele = db.Column(db.String(50))
    immatriculation = db.Column(db.String(50), unique=True)
    prix_location = db.Column(db.Integer)
    couleur = db.Column(db.String(50))
    nombre_porte = db.Column(db.Integer)
    nombre_siege = db.Column(db.Integer)
    type_carburant = db.Column(db.String(50))
    boite_vitesse = db.Column(db.String(50))
    kilometrage = db.Column(db.Integer)
