from sqlalchemy import create_engine, text


def get_db_connection_str(db_config):
    # connection string zbudowany z konfiguracji
    return f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"


# def get_db_connection_str(db_config):
#     # connection string zbudowany z konfiguracji
#     return "sqlite:///lokalna_baza.sqlite"


def db_connect_open(db_config):
    # connection string zbudowany z konfiguracji
    conn_str = get_db_connection_str(db_config)

    # budujemy silnik bazodanowy
    engine = create_engine(conn_str)

    # podłączamy się do konkretnej bazy danych
    connection = engine.connect()
    return connection


def db_connect_close(connection):
    # zamknięcie połączenia z bazą
    connection.close()


def get_sql_results(db_config, sql_query):
    connection = db_connect_open(db_config)

    results = connection.execute(text(sql_query))
    connection.commit()

    db_connect_close(connection)

    return list(results)
