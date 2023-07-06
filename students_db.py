import psycopg2
from uzduotys06_29 import load_data

db_params = {
    'host': 'localhost',
    'port': 5432,
    'database':'studentai',
    'user': 'postgres',
    'password': '123654'
}
def create_table():
    connection = psycopg2.connect(**db_params)
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS studentu_info (
    id SERIAL PRIMARY KEY,
    vardas VARCHAR(100),
    pavarde VARCHAR(100),
    amzius INTEGER
    )
    """
    
    cursor = connection.cursor()
    cursor.execute(create_table_query)

    connection.commit()
    cursor.close()
    connection.close()

def insert_query():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    for _, row in load_data().iterrows():

        insert_data_into_tabble = f'''
        INSERT INTO studentu_info(vardas, pavarde, amzius)
        VALUES ('{row['vardas']}', '{row['pavarde']}', '{row['amzius']}')
        '''
        cursor = connection.cursor()
        cursor.execute(insert_data_into_tabble)
        connection.commit()
        cursor.close()
        connection.close()
    