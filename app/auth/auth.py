import secrets
import logging
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.config import settings

security = HTTPBasic()

logging.basicConfig(level=logging.INFO)

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    logging.info(f"Attempting authentication with username: {credentials.username}")
    correct_username = secrets.compare_digest(credentials.username, settings.BASIC_AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, settings.BASIC_AUTH_PASSWORD)
    if not (correct_username and correct_password):
        logging.warning(f"Failed authentication for username: {credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    logging.info(f"Successful authentication for username: {credentials.username}")
    return credentials.username
