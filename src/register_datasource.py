from utils import get_purview_client
from azure.core.exceptions import AzureError, HttpResponseError

def main():
    try:
        client = get_purview_client()
    except AzureError as e:
        print(e)


    storage_name = "<name of your Storage Account>"
    storage_id = "<id of your storage account>"
    rg_name = "<name of your resource group>",
    rg_location = "<location of your resource group>",
    reference_name_purview = "name of your purview account"
    
    body_input = {
            "kind": "AzureStorage",
            "properties": {
                "endpoint": f"https://{storage_name}.blob.core.windows.net/",
                "resourceGroup": rg_name,
                "location": rg_location,
                "resourceName": storage_name,
                "resourceId": storage_id,
                "collection": {
                    "type": "CollectionReference",
                    "referenceName": reference_name_purview #here we use the root collection
                },
                "dataUseGovernance": "Disabled"
            }
        }

    try:
        response = client.data_sources.create_or_update(ds_name, body=body_input)
        print(response)
        print(f"Data source {ds_name} successfully created or updated")
    except HttpResponseError as e:
        print(e)

if __name__ == '__main__':
    main()