"""
Stefan Proell 2021

You can use the following snippet for connecting to Aurora Databases via SSH.

You need to set the environment variables shown below and use a virtual environment (`venv`).
You can create the `venv` using the Makefile with the command `make venv`.

You will need to enable TLS1 for Ubuntu by using a configuration script for openssl.
The script is stored in `openssl.cfg` in this git repository.
You need to provide an absolute path to it in the variable `OPENSSL_CONF`.

Add the following variables to the run time environment and make sure you are connected to the
AWS cluster using the connection scripts provided by the
[AWS connections repository](git@bitbucket.org:cropster/aws_connections.git)
Please always use a reader instance when retrieving data and ensure that you use the right ports.

Example
    OPENSSL_CONF=/full/path/to/config/openssl.cfg
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_USER=alice
    DB_PASSWORD=SECRET
    DB_NAME=sakila

"""
import mysql.connector
import sqlalchemy as sqlalchemy
from mysql.connector.constants import ClientFlag
import pandas as pd

import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

sql_query = """
SELECT
    last_name
FROM sakila.actor
ORDER BY actor_id DESC
LIMIT 10
"""

def get_connection_config():
    """
    Required environment variables: 

    OPENSSL_CONF=/full/path/to/config/openssl.cfg
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_USER=alice
    DB_PASSWORD=SECRET
    DB_NAME=sakila

    :return: db_config_dict
    """
    if(os.getenv('DB_PASSWORD') != None):
        mysql_config = {
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME'),
            'client_flags': [ClientFlag.SSL]
        }
        return mysql_config
    else:
        print("You need to set the env variables")
        exit(1)

if __name__ == "__main__":
    mysql_config = get_connection_config()

    """Use a cursor object
    
    You can retrieve data by using a cursor object and iterate over the results.
    Close cursors and connections when done.
    """

    mysql_connection = mysql.connector.connect(**mysql_config)

    cursor = mysql_connection.cursor()
    cursor.execute(sql_query)

    for (_username) in cursor:
        logging.info("Actor: {}".format(last_name))

    cursor.close()
    mysql_connection.close()

    """Use Pandas for retrieving data
    
    The more convenient way of retrieving data is to use Pandas.
    It will return a data frame and you can easily paginate large result sets in a loop.
    
    """
    mysql_connection = mysql.connector.connect(**mysql_config)
    for chunk in pd.read_sql_query(con=mysql_connection, sql=sql_query, chunksize = 5):
        logging.info("last_name: {}".format(chunk['last_name']))

    exit(0)
