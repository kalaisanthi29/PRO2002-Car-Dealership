"""Firebase authentication"""
from pathlib import Path
from typing import Optional
import firebase_admin
from firebase_admin import credentials, auth, exceptions

# Hides the file credentials
CREDENTIALS_FILE = Path(__file__).resolve().parent / "serviceAccountKey.json"

# We use the course example for now from module 4.8
# However, we can change this if there is any better approach out there for these functions.
def initialize_firebase():
    """initialize the firebase SDK"""
    try:
        firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(CREDENTIALS_FILE)
        firebase_admin.initialize_app(cred)

def verify_token(id_token: str) -> Optional[dict]:
    """verifies the token"""
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded
    except exceptions.FirebaseError:
        return None
