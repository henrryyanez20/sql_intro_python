import csv, sqlite3

def create_schema():
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("""
                DROP TABLE IF EXISTS t;
            """)

    c.execute("""
                CREATE TABLE t (
                    [titulo] TEXT NOT NULL, 
                    [cantidad_paginas] INTEGER, 
                    [autor] TEXT
                );""")
    conn.commit()
    conn.close()


def fill():
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    
    with open('libreria.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['titulo'], i['cantidad_paginas'], i['autor']) for i in dr]

    c.executemany("""
            INSERT INTO t (titulo, cantidad_paginas, autor)
            VALUES (?,?,?);""", to_db)
    conn.commit()
    conn.close()

def fetch():
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM t')
    data = c.fetchall()
    print(data)



if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch()  # Ver todo el contenido de la DB
  #fetch(3)  # Ver la fila 3
  #fetch(20)  # Ver la fila 20

  # Buscar autor
  #print(search_author('Relato de un naufrago'))

