import sqlite3

class DB:
    def __init__(self):
        # Nom de ton fichier de base de données
        self.DB_FILE = 'todo.db' # C'est parfait ici

    def connect_db(self):
        """Établit une connexion à la base de données."""
        try:
            conn = sqlite3.connect(self.DB_FILE) # Utilise self.DB_FILE
            # Permet d'accéder aux colonnes par leur nom (comme un dictionnaire)
            conn.row_factory = sqlite3.Row
            # 'DB_FILE' n'est pas défini ici, il faut utiliser self.DB_FILE
            print(f"Connexion à la base de données {self.DB_FILE} établie.")
            return conn
        except sqlite3.Error as e:
            print(f"Erreur de connexion à la base de données : {e}")
            return None

    def create_table(self): # Renommé pour cohérence avec la convention snake_case
        """Crée la table 'tasks' si elle n'existe pas."""
        conn = self.connect_db()
        if conn: # S'assurer que la connexion a été établie
            try:
                cursor = conn.cursor() # Un curseur exécute les requêtes SQL
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        status TEXT DEFAULT 'en cours'
                    )
                """)
                conn.commit() # Valide les changements (pour CREATE, INSERT, UPDATE, DELETE)
                print("Table 'tasks' vérifiée/créée avec succès.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la création de la table : {e}")
            finally:
                conn.close() # Toujours fermer la connexion
        else:
            print("Impossible de créer la table : connexion à la base de données échouée.")
    # ... (importe et fonctions connect_db, create_tasks_table du dessus) ...

    def add_task(self,description):
        """Ajoute une nouvelle tâche à la table 'tasks'."""
        conn = self.connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
                # Le '?' est un placeholder. On passe la valeur dans un tuple.
                # C'est CRUCIAL pour éviter les injections SQL !
                conn.commit()
                print(f"Tâche '{description}' ajoutée avec succès. ID: {cursor.lastrowid}")
                return cursor.lastrowid # Retourne l'ID de la tâche nouvellement insérée
            except sqlite3.Error as e:
                print(f"Erreur lors de l'ajout de la tâche : {e}")
                return None
            finally:
                conn.close()
    # ... (importe et fonctions connect_db, create_tasks_table, add_task du dessus) ...

    def get_all_tasks(self):
        """Récupère toutes les tâches de la table 'tasks'."""
        conn = self.connect_db()
        tasks = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id, description, status FROM tasks ORDER BY id DESC")
                # `SELECT` les colonnes que tu veux. `*` pour toutes.
                # `ORDER BY id DESC` pour trier par ID décroissant (les plus récents d'abord)
                tasks = cursor.fetchall() # Récupère toutes les lignes de résultats
                # Ou `cursor.fetchone()` pour la première ligne
                print("Toutes les tâches récupérées.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la récupération des tâches : {e}")
            finally:
                conn.close()
        return tasks
    # ... (importe et fonctions précédentes) ...

    def update_task_status(self,task_id, new_status):
        """Met à jour le statut d'une tâche."""
        conn = self.connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
                conn.commit()
                print(f"Tâche ID {task_id} mise à jour au statut '{new_status}'.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la mise à jour de la tâche : {e}")
            finally:
                conn.close()
    # ... (importe et fonctions précédentes) ...

    def delete_task(self,task_id):
        """Supprime une tâche de la table 'tasks'."""
        conn = self.connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
                conn.commit()
                print(f"Tâche ID {task_id} supprimée avec succès.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la suppression de la tâche : {e}")
            finally:
                conn.close()
