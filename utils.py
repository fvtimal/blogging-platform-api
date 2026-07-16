from passlib.context import CryptContext
from bson import ObjectId

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def is_valid_object_id(id:str):
    return ObjectId.is_valid(id)

# utils.py
def serialize_doc(doc: dict, id_fields: list[str] = None) -> dict:
    """Convert Mongo ObjectId fields to strings for JSON responses."""
    id_fields = id_fields or []
    doc["id"] = str(doc.pop("_id"))
    for field in id_fields:
        value = doc.get(field)
        if isinstance(value, list):
            doc[field] = [str(v) for v in value]
        elif value is not None:
            doc[field] = str(value)
    return doc