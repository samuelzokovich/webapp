from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here you would decode the token and get user info from Azure AD
    # For simplicity, let's assume the token contains user_id and role
    user_id = "extracted_user_id"  # Extract from token
    role = "extracted_role"  # Extract from token
    return {"user_id": user_id, "role": role}