import whateverisneededforsql
def getSQLData(fileName):
    DB = "TIS"

    # Database instance
    SERVER_NAME = "SQLBETAWARE01"

    # Database Connection
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=SQLBETAWARE01;DATABASE=TIS")

    # Cursor to execute the SQL QUERY
    cursor = conn.cursor()
    fd = open("C:\\Users\\PycharmProjects\\data_sql\\test_reg.sql", "r")
    sqlFile = fd.read()
    fd.close()
    # Execute the query to get data
    result = cursor.execute(sqlFile)
    return result.fetchall()