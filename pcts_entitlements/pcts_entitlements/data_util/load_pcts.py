import pyodbc
import pandas as pd


def connect_to_pcts():
    """
    Connects to PCTS and returns a connection object
    """
    server = 'azss-dcp-02-ext.database.windows.net'
    database = 'PCTS'
    driver = '{ODBC Driver 18 for SQL Server}' 

    # Build connection string
    conn_str = f'''
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    Authentication=ActiveDirectoryInteractive;
    Encrypt=yes;
    TrustServerCertificate=no;
    '''
    try:
        #try connecting and returning connection object
        conn = pyodbc.connect(conn_str)
        print("Connected!")
        return conn 
    
    except Exception as e: #Throw error if unable to connect
        print("Error connecting to database:", e)


def pcts_query(query):
    """
    Takes in a SQL query and returns a Pandas DataFrame of the results
    """ 
  
    try:
        conn = connect_to_pcts()
        results = pd.read_sql(query, conn)
        return results
    except Exception as e:
        print("Query failed:", e)

