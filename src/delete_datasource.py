from utils import get_purview_client
from azure.core.exceptions import AzureError, HttpResponseError

def main():
    try:
        client = get_purview_client()
    except AzureError as e:
        print(e)

    ds_name = "<name of the registered data source you want to delete>"
    try:
        response = client.data_sources.delete(ds_name)
        print(response)
        print(f"Data source {ds_name} successfully deleted")
    except HttpResponseError as e:
        print(e)

if __name__ == '__main__':
    main()