import os
import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWKClient

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Replace with your Azure AD tenant ID and application ID
        tenant_id = os.getenv("AZURE_TENANT_ID")
        app_id = os.getenv("AZURE_APP_ID")
        jwks_url = f"https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys"

        # Fetch the public keys from Azure AD
        jwk_client = PyJWKClient(jwks_url)
        signing_key = jwk_client.get_signing_key_from_jwt(token)

        # Decode the token
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=app_id,
            issuer=f"https://login.microsoftonline.com/{tenant_id}/v2.0"
        )

        user_id = payload.get("sub")
        role = payload.get("roles", ["user"])[0]  # Default to "user" role if not present

        return {"user_id": user_id, "role": role}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail="Invalid token claims")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Example usage in a FastAPI endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
