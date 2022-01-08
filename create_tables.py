import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    '''This user define function to drop all tables which has created .
   inputs:
   ->cur: this is a cursor variable of the database
   ->conn: this is a connection variable of the database
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
        This user define function to create all required tables.
        inputs:
        -> cur: this is a cursor variable of the database
        -> conn: this is a connection variable of the database
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
     This main function uses the  credentials in the configuration file to connect to the database, then drop and rebuild the required tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
    
    