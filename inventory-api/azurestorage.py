from azure.storage.blob import BlobServiceClient
import json

class AzureBlobStorage:
    def __init__(self, connection_string: str, container_name: str):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_name = container_name
        self.create_container()

    def create_container(self):
        try:
            self.blob_service_client.create_container(self.container_name)
        except Exception as e:
            print(f"Container already exists or error occurred: {e}")

    def upload_item(self, item_id: str, item_data: dict):
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=item_id)
        blob_client.upload_blob(json.dumps(item_data), overwrite=True)

    def download_item(self, item_id: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=item_id)
        try:
            blob_data = blob_client.download_blob().readall()
            return json.loads(blob_data)
        except Exception as e:
            print(f"Error downloading blob: {e}")
            return None

    def list_items(self):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        return [blob.name for blob in container_client.list_blobs()]