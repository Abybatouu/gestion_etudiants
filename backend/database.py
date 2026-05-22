import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="gestion_etudiants",
            user="abiba",
            password="passer123"
        )
        return connection
    except Exception as e:
        print(f"Erreur de connection à la base de données: {e}")
        return None

def creer_tables():
    connection = connect_to_db()
    if not connection:
        print("Impossible de se connecter à la base de données.")
        return
    try:
        cursor = connection.cursor()
        with open('donnees/creation_base.sql', 'r') as f:
            sql_script = f.read()
            cursor.execute(sql_script)
        connection.commit()
        print("Tables créées avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création des tables: {e}")
    finally:
        cursor.close()
        connection.close()
    
creer_tables()