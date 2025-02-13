Python REST API Inventory Management Application with Azure AD

Overview

This project is a Python REST API application for inventory management, utilizing FastAPI and Azure Active Directory (Azure AD) for authentication and authorization.

Project Setup

1. Clone the repository and navigate to the project folder:

git clone <repository-url>
cd inventory-api

2. Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install project dependencies:

pip install fastapi uvicorn msal pyjwt pydantic azure-identity sqlalchemy

Configuration

Edit the main.py file and replace the placeholders with your Azure AD credentials:

TENANT_ID – Your Azure AD tenant ID

CLIENT_ID – Your application (client) ID

CLIENT_SECRET – Your client secret

Running the Application

Use the following command to start the FastAPI server:

uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000.

API Endpoints

GET /items – Retrieve all items

POST /items – Add a new item

PUT /items/{item_id} – Update an item

DELETE /items/{item_id} – Delete an item

Azure AD Authentication

The application uses MSAL to handle authentication.

Users must include a valid Azure AD token in the Authorization header (as a Bearer token) for all requests.

Future Enhancements

Integrate a database (e.g., Azure SQL, Cosmos DB).

Add detailed token validation and role-based access control.

Include logging and monitoring with Azure services.

License

This project is licensed under the MIT License.
