from flask import Flask, request,flash, render_template, url_for, redirect,send_from_directory
from flaskext.mysql import MySQL
import mysql.connector
import os
from flask import session
from builtins import enumerate

from werkzeug.utils import secure_filename




app = Flask(__name__)
mysql = MySQL()



app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flasky'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/inscriptionC', methods=['GET', 'POST'])
def inscriptionC():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        np = request.form['np']
        telephone = request.form['telephone']
        email = request.form['email']
        mdp = request.form['mdp']
        # Connecter à la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
        # Ajouter les données à la base de données
        query = "INSERT INTO utilisateurs (np, telephone,  email, mdp) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (np, telephone, email, mdp))
        conn.commit()

        return redirect(url_for('loginC'))
    return render_template('inscriptionC.html')


@app.route('/loginC', methods=['GET', 'POST'])
def loginC():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        mdp = request.form['mdp']
        # Connecter à la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
        # Vérifier les données dans la base de données
        query = "SELECT * FROM utilisateurs WHERE email = %s AND mdp = %s"
        cursor.execute(query, (email, mdp))
        data = cursor.fetchone()
        if data is not None:
            return redirect(url_for('accueilC'))
        else:
            return render_template('loginC.html', error=True)
    return render_template('loginC.html')


@app.route('/accueilC', methods=['GET', 'POST'])
def accueilC():
    if request.method == 'POST':
        nom_complet = request.form['nom_complet']
        num_piece = request.form['num_piece']
        num_permis = request.form['num_permis']
        antecedent = request.form['antecedent']
        paiement = request.form['paiement']
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "INSERT INTO authentic (nom_complet, num_piece, num_permis, antecedent, paiement) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nom_complet, num_piece,  num_permis, antecedent, paiement))
        conn.commit()
        # cursor.close()
        return redirect(url_for('service'))
    return render_template('accueilC.html')



@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        ville_depart= request.form['ville_depart']
        date_depart = request.form['date_depart']
        date_retour = request.form['date_retour']
        nombre_passagers = request.form['nombre_passagers']
        nombre_jours = request.form['nombre_jours']
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "INSERT INTO location (ville_depart, date_depart, date_retour, nombre_passagers, nombre_jours) VALUES (%s, %s, %s, %s, %s)" 
        cursor.execute(query, (ville_depart, date_depart, date_retour, nombre_passagers, nombre_jours))
        conn.commit()
        return redirect(url_for('paiement'))
    return render_template('location.html')



@app.route('/paiement') 

def paiement():
    return render_template('paiement.html')




@app.route("/reçuC")
def reçuC():
    return render_template("reçuC.html")


@app.route('/inscriptionL', methods=['GET', 'POST'])
def inscriptionL():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        np = request.form['np']
        telephone = request.form['telephone']
        email = request.form['email']
        mdp = request.form['mdp']
        # Connecter à la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
        # Ajouter les données à la base de données
        query = "INSERT INTO proprio (np, telephone,  email, mdp) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (np, telephone, email, mdp))
        conn.commit()

        return redirect(url_for('loginL'))
    return render_template('inscriptionL.html')


@app.route('/loginL', methods=['GET', 'POST'])
def loginL():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        mdp = request.form['mdp']
        # Connecter à la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
        # Vérifier les données dans la base de données
        query = "SELECT * FROM proprio WHERE email = %s AND mdp = %s"
        cursor.execute(query, (email, mdp))
        data = cursor.fetchone()
        if data is not None:
            return redirect(url_for('accueilL'))
        else:
            return render_template('loginL.html', error=True)
    return render_template('loginL.html')




UPLOAD_FOLDER = './static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg' 'jpg' , 'jpeg' , 'jfif' , 'pjpeg' , 'pjp', 'png', 'webp'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/accueilL', methods=['GET', 'POST'])
def accueilL():
    if request.method == 'POST':
        marque = request.form['marque']
        annee_modele = request.form['annee_modele']
        immatriculation = request.form['immatriculation']
        couleur = request.form['couleur']
        nombre_porte = request.form['nombre_porte']
        nombre_siege = request.form['nombre_siege']
        type_carburant = request.form['type_carburant']
        boite_vitesse = request.form['boite_vitesse']
        kilometrage = request.form['kilometrage']
        prix_location = request.form['prix_location']
        file = request.files['img']

        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return "File type not allowed. Please select a JPEG or JPG file."
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO infos_vehicule (marque, annee_modele, immatriculation, couleur, nombre_porte, nombre_siege, type_carburant, boite_vitesse, kilometrage,prix_location, img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (marque, annee_modele, immatriculation, couleur, nombre_porte, nombre_siege, type_carburant, boite_vitesse, kilometrage, prix_location, filename))
        conn.commit()
        # cursor.close()
        return redirect(url_for('acceder'))
    return render_template('accueilL.html')




@app.route('/voiture/<int:vehicule_id>')
def voiture(vehicule_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM infos_vehicule WHERE id_vehicule=%s", (vehicule_id,))
    vehicule = cursor.fetchone()
    return render_template('voiture.html', vehicule=vehicule)

app.secret_key = "bonjour"



@app.route('/service', methods=['GET', 'POST'])
def service():
    conn = mysql.connect()
    cursor = conn.cursor()
    if 'offset' not in session:
        session['offset'] = 0
    if request.method == 'POST':
        if request.form.get('voir_plus'):
            session['offset'] += 9
        if request.form.get('voir_moins') and session['offset'] >= 9:
            session['offset'] -= 9
    cursor.execute("SELECT * FROM infos_vehicule ORDER BY id_vehicule DESC LIMIT 9 OFFSET %s", (session['offset'],))
    vehicules = cursor.fetchall()
    return render_template('service.html', vehicules=vehicules)



@app.route('/tableau_utilisateurs', methods=['GET'])
def tableau_utilisateurs():
        # Connecter à la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
        # Récupérer les données des deux tables
        query = "SELECT utilisateurs.np, utilisateurs.telephone, utilisateurs.email, \
                authentic.num_piece, authentic.num_permis, authentic.antecedent \
                FROM utilisateurs \
                INNER JOIN authentic ON utilisateurs.np = authentic.nom_complet"
        cursor.execute(query)
        data = cursor.fetchall()
        # Fermer la connexion
        cursor.close()
        conn.close()
        # Afficher les données dans un tableau HTML
        return render_template('tableau_utilisateurs.html', data=data)




# @app.route('/commandes', methods=['GET'])
# def commandes():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT ville_depart, date_depart, date_retour, nombre_passagers, nombre_jours FROM location")
#     commandes = cursor.fetchall()
#     cursor.close()
#     return render_template('commandes.html', commandes=commandes)


@app.route('/validation_commande')
def validation_commande():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM location")
    locations = cursor.fetchall()
    conn.close()
    return render_template('validation_commande.html', locations=locations)


@app.route('/admin')
def admin():
 return render_template('admin.html')



@app.route('/commandes', methods=['GET', 'POST'])
def commandes():
    
    return render_template('commandes.html')




@app.route('/acceder', methods=['GET', 'POST'])
def acceder():
    if request.method == 'POST':
        # Récupérer la valeur de l'immatriculation à partir du formulaire
        immatriculation = request.form['immatriculation']
        
        # Vérifier si l'immatriculation existe dans la base de données
        conn = mysql.connect()
        cursor = conn.cursor()
    
        query = "SELECT * FROM location WHERE immatriculation = %s"
        cursor.execute(query, (immatriculation,))
        vehicule = cursor.fetchone()
        
        if vehicule is not None:
            # Rediriger vers la page de commandes
            return redirect(url_for('admin', immatriculation=immatriculation))
        else:
            # Afficher un message d'erreur si l'immatriculation n'existe pas
            message = "L'immatriculation n'existe pas dans la base de données."
            return render_template('acceder.html', message=message)
    else:
        # Afficher la page d'accès si la méthode n'est pas une requête POST
        return render_template('acceder.html')


if __name__ == '__main__':
 app.run(debug=True)
