from fastapi import FastAPI, Depends, HTTPException
from azurestorage import AzureBlobStorage
from typing import List
import schemas, auth
import os

app = FastAPI()

# Initialize Azure Blob Storage
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "inventory-items"
storage = AzureBlobStorage(AZURE_CONNECTION_STRING, CONTAINER_NAME)

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, current_user: dict = Depends(auth.get_current_user)):
    item_id = f"{item.name}-{current_user['user_id']}"  # Unique ID for the item
    item_data = item.model_dump()
    storage.upload_item(item_id, item_data)
    return {**item_data, "id": item_id}

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: str, current_user: dict = Depends(auth.get_current_user)):
    item_data = storage.download_item(item_id)
    if item_data is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**item_data, "id": item_id}

@app.get("/items/", response_model=List[schemas.Item])
def list_items(current_user: dict = Depends(auth.get_current_user)):
    items = storage.list_items()
    return [{"id": item_id, "name": item_id.split('-')[0]} for item_id in items]
