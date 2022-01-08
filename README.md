data-warehouse
------------
Summary
--------
This project combines a song list-to-log file with song metadata for ease of analysis. Redshift clusters are created using the Python SDK and the data pipeline built into Python, and SQL prepares a data schema designed for analysis. The JSON data is copied from the S3 bucket to the Redshift staging table and then pasted into the star schema that contains the fact and dimension tables. Analyzing the Songplays fact table Queries are easy, with easy access to additional fields in the four dimension tables: User, Song, Artist, and Time. Star schemas are suitable for this application because they are easy to denormalize, keep queries simple, and aggregate fast.

Database Schema
----------------
Below are all  the fact and dimension tables created for this project.

Dimension Tables:

users
columns: user_id, first_name, last_name, gender, level
songs
columns: song_id, title, artist_id, year, duration
artists
columns: artist_id, name, location, lattitude, longitude
time
columns: start_time, hour, day, week, month, year, weekday

Fact Table:
songplays
columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Files
------
delete the create_tables.py table and create a new table 
dwh.cfg Configuration Redshift Cluster and Data Import 
etl.py Copy the data from the staging table and use the star schema  
 sql_queries.py
 staging and star schema to make the fact table. And paste into the dimension table-delete the created table 
 Copy JSON data from S3 to a Redshift staging table 
 Insert staging table data into fact and dimension tables in the star schema.
 

To run the project:
------------------
1. Update the dwh.cfg file with the Amazon Redshift cluster credentials and the IAM role that can access the cluster.
2. Run python create_tables.py: It will create the database and all of the required tables.
   >>python3 create_tables.py
3. Run python etl.py : Starts a pipeline that reads data from a file and populates a table.
   >>python3 etl.py

