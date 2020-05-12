# POSTGRES AND PANDAS ETL
## Context Problem
For a start-up with collections of data on songs and user activity on a music streaming app.
An analytics team is required to perform operations leading to discovery, interpretation, and communication of meaningful patterns in data, vto do this various queries has to be carried out on their data, which resides in a directory of JSON logs, as well as a directory with JSON metadata on the songs.
Currently, there isn't an easy way to carry out this query.

## Solution
The solution proposed in this repo is to create a Postgres database with tables designed to optimize queries on song play analysis
also create a database schema and ETL pipeline for this analysis. 
The following concepts of data engineering are brought into practice:

### Relational data modeling using Postgresql.
Queries and joins are particular in the tools of the analytics team, with the data being structured 
and not voluminous enough to require big data analytics tools such as Nosql, Spark. Hence, the use of relational data modeling.

### Fact and dimensional table modeling.
Since analytics is the major use case for this database and not trasanctional processes a
star schema is used, with fact and dimension tables.

### Extarct Transform and Load pipeline developed with Python,SQL and Pandas.
Data is extracted and transformed from the json log using python and pandas and loaded into the 
fact and dimension tables with sql queries.

## File Structure
1. *sql_queries.py* contains the sql queries used.
2. *create_tables.py* resets the database(drops and create table).
3. *connection_manger.py* contains context manager to help manage cursors and connections to the database, including decorators for error handling.
4. *etl.py* extracts, transforms and loads data  into tables.
5. *data*  folder, contains the data used.
