from utils import get_purview_client
from azure.core.exceptions import AzureError, HttpResponseError
import uuid
def main():
    try:
        client = get_purview_client()
    except AzureError as e:
        print(e)

    ds_name = "<name of your registered data source>"
    scan_name = "<name of your created scan>"
    run_id = uuid.uuid4() #unique id of the new scan
    
    ds_name = "mys"
    scan_name = "myscan"
    run_id = uuid.uuid4() 

    print(body_input)
    try:
        response = client.scan_result.run_scan(data_source_name=ds_name, scan_name=scan_name, run_id=run_id)
        print(response)
        print(f"Scan {scan_name} successfully started")
    except HttpResponseError as e:
        print(e)

if __name__ == '__main__':
    main()