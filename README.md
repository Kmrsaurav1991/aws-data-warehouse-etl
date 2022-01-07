data-warehouse
------------
Summary
--------
This project combines a song list-to-log file with song metadata for ease of analysis. Redshift clusters are created using the Python SDK and the data pipeline built into Python, and SQL prepares a data schema designed for analysis. The JSON data is copied from the S3 bucket to the Redshift staging table and then pasted into the star schema that contains the fact and dimension tables. Analyzing the Songplays fact table Queries are easy, with easy access to additional fields in the four dimension tables: User, Song, Artist, and Time. Star schemas are suitable for this application because they are easy to denormalize, keep queries simple, and aggregate fast.

Files
------
delete the create_tables.py table and create a new table 
dwh.cfg Configuration Redshift Cluster and Data Import 
etl.py Copy the data from the staging table and use the star schema  
 sql_queries.py
 staging and star schema to make the fact table. And paste into the dimension table-delete the created table 
 Copy JSON data from S3 to a Redshift staging table 
 Insert staging table data into fact and dimension tables in the star schema.
 
Drop and recreate tables

$ python create_tables.py
Run ETL pipeline

$ python etl.py