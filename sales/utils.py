import uuid

def genertate_code():
    code=str(uuid.uuid4()).replace('-', '')[:12]

    return code
    