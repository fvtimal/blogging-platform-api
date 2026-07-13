from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    print(password)
    print(type(password))
    print(len(password))
    return pwd_context.hash(password)