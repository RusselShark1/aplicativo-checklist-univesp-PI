# DB - Veiculos

import sqlite3

banco = sqlite3.connect('db_carros')

cursor = banco.cursor()

""" cursor.execute("CREATE TABLE veiculos(modelo text,placa text, km_final integer)") """

cursor.execute("INSERT INTO veiculos VALUES('Fiorino', 'CIY4H17', 35000)")
cursor.execute("INSERT INTO veiculos VALUES('Fiorino', 'CIY5H18', 45000)")
cursor.execute("INSERT INTO veiculos VALUES('Fiorino', 'BDY4H17', 70000)")
cursor.execute("INSERT INTO veiculos VALUES('Fiorino', 'LDP4H24', 10000)")

banco.commit()

""" cursor.execute("SELECT * FROM veiculos")
print(cursor.fetchall()) """