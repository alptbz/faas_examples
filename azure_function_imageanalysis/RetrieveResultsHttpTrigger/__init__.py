import enum
import logging
import azure.functions as func
from azure.data.tables import TableServiceClient
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = os.environ["AzureWebJobsStorageDev"]
    service = TableServiceClient.from_connection_string(conn_str=connection_string)
    tableclient = service.get_table_client("imageresults")

    entitiesI = tableclient.query_entities("")

    entities = list(entitiesI)

    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(json.dumps(entities))