import psycopg2

connection = psycopg2.connect(
host="data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com",
user="demiuchiha_coderhouse",
password="0QNPf2e3tC",
database="data-engineer-database",
port=5439
)

connection.autocommit = True

def creartabla():
    cursor = connection.cursor()
    query="CREATE TABLE PersonajesMarvel (id INT IDENTITY(1,1) PRIMARY KEY, nombre VARCHAR(255),descripcion VARCHAR(MAX), comics_disponibles INT,series_disponibles INT);"
    cursor.execute(query)
    cursor.close()
    creartabla()