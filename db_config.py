# import psycopg2

# db_params = {
#     'host': 'localhost',
#     'port': 5432,
#     'database':'aruodas',
#     'user': 'postgres',
#     'password': '123654'
# }
# def create_table():
#     connection = psycopg2.connect(**db_params) #** du asterixai perduoda dictionary (db_params) reiksmes i connectiona
    
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS properties (
#     id SERIAL PRIMARY KEY,
#     kaina INTEGER,
#     lokacija VARCHAR(500),
#     plotas VARCHAR(100)
#     )
#     """
    
#     cursor = connection.cursor()
#     cursor.execute(create_table_query)

#     connection.commit()
#     cursor.close()
#     connection.close()

# def insert_query(data):
#     connection = psycopg2.connect(**db_params)
#     cursor = connection.cursor()

#     insert_data_into_table = """
#     INSERT INTO properties(kaina, lokacija, plotas)
#     VALUES (%s, %s, %s)
#     """
#     cursor.executemany(insert_data_into_table, data)

#     connection.commit()
#     cursor.close()
#     connection.close()

# def take_database_info():
#     connection = psycopg2.connect(**db_params)
#     cursor = connection.cursor()
#     select_query = """
#     SELECT kaina, lokacija, plotas
#     FROM properties
#     """
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return rows
