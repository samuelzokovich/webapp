# Inventory Management API with Azure AD

## Overview

This is a Python REST API application built with FastAPI for inventory management, using Azure Active Directory (Azure AD) for authentication and Azure Blob Storage for data storage.

## Features

- **Role-Based Access Control (RBAC)**: Different roles (e.g., Admin, Manager, Staff) with specific permissions.
- **Audit Logging**: Logs all operations (add, update, delete) along with user details for traceability.
- **Item Categories and Tags**: Categorize items and use tags for better organization and filtering.
- **CRUD Operations**: Create, Read, Update, and Delete inventory items.

## Project Structure
inventory-api/ │ ├── main.py # Main application file ├── azure_storage.py # Azure Blob Storage interaction ├── auth.py # Authentication with Azure AD └── schemas.py # Pydantic schemas for request/response validation

Copy code

## Prerequisites

- Python 3.7 or higher
- Azure Subscription
- Azure Storage Account
- Azure Active Directory setup for authentication

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd inventory-api
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
Install dependencies:

bash
Copy code
pip install fastapi uvicorn azure-storage-blob python-dotenv
Set up environment variables:

Create a .env file in the root directory and add your Azure Storage connection string:

plaintext
Copy code
AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
Run the application:

bash
Copy code
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

API Endpoints
POST /items/: Create a new item
GET /items/{item_id}: Retrieve an item by ID
GET /items/: List all items
Authentication
This API uses Azure AD for authentication. Include a valid Bearer token in the Authorization header for all requests.

Future Enhancements
Implement stock alerts for low stock levels.
Add support for barcode/QR code integration.
Generate reports and analytics for inventory management.
Integrate with Azure SQL or Cosmos DB for more complex data storage needs.
License
Licensed under the MIT License.
