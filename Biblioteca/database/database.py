import mysql.connector

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root123",
                database="libra_tech",
                port=3307
            )
        return cls._instance

    def execute(self, query, params=None):
        cursor = self.connection.cursor()  # Criar um novo cursor sempre
        try:
            cursor.execute(query, params or ())
            result = cursor.fetchall()  # Buscar todos os resultados
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            print(f"Erro no banco de dados: {e}")
            return []
        finally:
            cursor.close()  # Fechar o cursor depois de cada operação
