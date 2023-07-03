# import psycopg2
# db_params = {
#     'host': 'localhost',
#     'port': 5432,
#     'database':'studentai',
#     'user': 'postgres',
#     'password': '123654'
# }
# def create_table():
#     connection = psycopg2.connect(**db_params)
    
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS studentu_info (
#     id SERIAL PRIMARY KEY,
#     vardas VARCHAR(100),
#     pavarde VARCHAR(100),
#     amzius INTEGER
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

#     for row in df():
#         cursor.execute('''
#             INSERT INTO studentu_info(vardas, pavarde, amzius)
#             VALUES (%s, %s, %s)
#             ''',
#             row.vardas, 
#             row.pavarde,
#             row.amzius
#             )

#     connection.commit()
#     cursor.close()
#     connection.close()