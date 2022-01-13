from utils import get_catalog_client
from azure.core.exceptions import AzureError, HttpResponseError

def main():
    try:
        client = get_catalog_client()
    except AzureError as e:
        print(e)

    keywords = "keywords"
    body_input={
        "keywords": keywords
    }
    try:
        response = client.discovery.query(search_request=body_input)
        print(response)
    except HttpResponseError as e:
        print(e)

if __name__ == '__main__':
    main()