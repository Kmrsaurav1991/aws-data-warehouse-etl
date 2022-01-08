import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
        This user-defined function uses the COPY command to execute a list of load queries that load  data from a 
        file in an s3 bucket into a stage table..
        inputs:
        -> cur: this is a cursor variable of the database
        -> conn: this is a connection variable of the database
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
        This user-defined function inserts data from the staging table into the final table according to the list of queries inserted.
        inputs:
        -> cur: this is a cursor variable of the database
        -> conn: this is a connection variable of the database
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
        This main start function of the program 
        It gets all DB credentials from the config file, establishes a connection to the database, pushes s3 files to stage tables , 
        pushes data to final tables from stage tables and closes the database connection after finishing all tasks.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()