import bcrypt

def hash_user_input(user_input: str) -> bytes:
    return bcrypt.hashpw(user_input.encode(), bcrypt.gensalt())

def authenticate(user_input: str, db_pw: bytes) -> bool:
    return bcrypt.checkpw(user_input.encode(), db_pw)