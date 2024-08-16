# import azure.functions as func
# import logging
# import pandas as pd

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="http_trigger")
# def http_trigger(req: func.HttpRequest):
#     logging.info('Python HTTP trigger function processed a request.')

#     try:
#         # Create a temporary DataFrame with test data
#         data = {
#             'user_id': [1, 2, 3, 4, 5],
#             'first_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
#             'last_name': ['Johnson', 'Williams', 'Martinez', 'Robinson', 'Clark'],
#             'email': ['alice.johnson@example.com', 'bob.williams@example.com', 'charlie.martinez@example.com', 'diana.robinson@example.com', 'evan.clark@example.com'],
#             'age': [25, 34, 28, 30, 27],
#             'city': ['Miami', 'Seattle', 'Denver', 'Boston', 'Austin']
#         }
#         df = pd.DataFrame(data)
#         logging.info("Temporary DataFrame created successfully")
        
#         # Process the DataFrame (e.g., return the first 10 rows)
#         result = df.head(10).to_json(orient='records')

#     except Exception as e:
#         logging.error(f"An error occurred: {str(e)}")
#         return func.HttpResponse(
#             "An error occurred while processing your request.",
#             status_code=500
#         )
    
#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(
#             f"Hello, {name}. This HTTP triggered function executed successfully. "
#             f"Here is the data: {result}",
#             status_code=200
#         )
#     else:
#         return func.HttpResponse(
#             f"This HTTP triggered function executed successfully. "
#             f"Here is the data: {result}",
#             status_code=200
#         )


# import azure.functions as func
# import logging
# import pyodbc
# import pandas as pd

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="http_trigger")
# def http_trigger(req: func.HttpRequest):
#     logging.info('Python HTTP trigger function processed a request.')

    
#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
            
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')
           

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. and connection is succesfull")

#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.and connection is succesfull",
#              status_code=200
#         )

import azure.functions as func
import logging
import pyodbc
import pandas as pd

# Define the connection string for the local SQL database
cnxn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=tcp:serveru123.database.windows.net,1433;'
    'DATABASE=DB123;'
    'UID=server123-UID;'
    'PWD=P@ssword'
)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest):
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Connect to the local SQL database
        conn = pyodbc.connect(cnxn_str)
        logging.info("Connection successful")
        
        # Fetch data from the SQL table
        df = pd.read_sql_query("SELECT * FROM Aftab", conn)
        
        # Close the connection
        conn.close()
        logging.info("Connection closed")
        
        # Process the fetched data (e.g., return the first 10 rows)
        result = df.head(10).to_json(orient='records')

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "An error occurred while processing your request.",
            status_code=500
        )
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully. "
            f"Here is the data: {result}",
            status_code=200
        )
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed successfully. "
            f"Here is the data: {result}",
            status_code=200
        )
