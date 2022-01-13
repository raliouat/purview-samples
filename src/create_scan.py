from utils import get_purview_client
from azure.core.exceptions import AzureError, HttpResponseError

def main():
    try:
        client = get_purview_client()
    except AzureError as e:
        print(e)
    
    ds_name = "<name of your registered data source>"
    scan_name = "<name of the scan you want to define>"
    reference_name_purview = "<name of your purview account>"

    body_input = {
            "kind":"AzureStorageMsi",
            "properties": { 
                "scanRulesetName": "AzureStorage", 
                "scanRulesetType": "System", #We use the default scan rule set 
                "collection": 
                    {
                        "referenceName": reference_name_purview, 
                        "type": "CollectionReference"
                    }
            }
        }

    try:
        response = client.scans.create_or_update(data_source_name=ds_name, scan_name=scan_name, body=body_input)
        print(response)
        print(f"Scan {scan_name} successfully created or updated")
    except HttpResponseError as e:
        print(e)

if __name__ == '__main__':
    main()