import sqlite3


def _executar(query):
    db_path = './geek.university'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    resultado = None

    try:
        cursor.execute(query)
        resultado = cursor.fetchall()  # LISTA DE TUPLAS
        connection.commit()
    except Exception as error:
        print(f'Erro na execução da query: {error}')

    connection.close()

    return resultado
